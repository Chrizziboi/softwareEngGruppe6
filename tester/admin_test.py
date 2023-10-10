import pytest
from app import admin1
from backend.users.admin import admin

def test_create_admin():
    admin = admin1
    assert admin.adminID == 1
    assert admin.adminname == "admin"
