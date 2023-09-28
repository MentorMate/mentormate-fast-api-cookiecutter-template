import uuid
from abc import ABC, abstractmethod

import factory
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.types import TypeDecorator, CHAR


class DBSessionMixinInterface(ABC):
    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass


class SQLAlchemySessionMixin(DBSessionMixinInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


class GUID(TypeDecorator):
    """Platform-independent GUID type.
    Uses PostgreSQL's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.
    """
    impl = CHAR
    cache_ok = True

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value).int
            else:
                # hexstring
                return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            if not isinstance(value, uuid.UUID):
                value = uuid.UUID(value)
            return value


class AsyncFactory(factory.alchemy.SQLAlchemyModelFactory):
    @classmethod
    async def _create(cls, model_class, *args, **kwargs):
        instance = super()._create(model_class, *args, **kwargs)
        async with cls._meta.sqlalchemy_session as session:
            await session.commit()
        return instance

    @classmethod
    async def create_batch(cls, size, **kwargs):
        """This async wrapper of create_batch create a batch of instances of the given class,
            with overridden attrs.

        Args:
            size (int): the number of instances to create

        Returns:
            object list: the created instances
        """
        return [await cls.create(**kwargs) for _ in range(size)]

    @classmethod
    def set_session(cls, session: AsyncSession):
        cls._meta.sqlalchemy_session = session
