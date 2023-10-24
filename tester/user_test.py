import pytest
from backend.users.user import user
from app import user1
def test_create_user():
    user1 = user(1,"user")

    assert user1.userID == 1
    assert user1.username == "user"
