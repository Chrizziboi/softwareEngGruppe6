import pytest
from backend.users.user import user
from app import user1
def test_create_user():
    user = user1
    assert user.userID == 1
    assert user.username == "bruker"
