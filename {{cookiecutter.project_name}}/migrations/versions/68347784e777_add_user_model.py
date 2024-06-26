"""add user model

Revision ID: 68347784e777
Revises: 
Create Date: 2023-07-07 23:43:24.103992

"""
from alembic import op
import sqlalchemy as sa

from src.utils import GUID

# revision identifiers, used by Alembic.
revision = '68347784e777'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', GUID(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
