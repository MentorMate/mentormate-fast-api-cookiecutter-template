import pytest

from src.auth.security import get_password_hash, verify_password


@pytest.mark.auth
def test_get_password_hash():
    # Arrange
    password_string = "password"

    # Act
    password_hash_one = get_password_hash(password_string)
    password_hash_two = get_password_hash(password_string)

    # Assert
    assert isinstance(password_hash_one, str)
    assert isinstance(password_hash_two, str)
    assert password_hash_one != password_hash_two


@pytest.mark.auth
def test_verify_password():
    # Arrange
    password_string = "password"

    # Act
    password_hash = get_password_hash(password_string)

    # Assert
    assert verify_password(password_string, password_hash)
