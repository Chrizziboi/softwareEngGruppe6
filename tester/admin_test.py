import pytest
from app import admin1
from backend.users.admin import admin

def test_create_admin():
    admin1 = admin(1, "admin")

    assert admin1.adminID == 1
    assert admin1.adminname == "admin"
