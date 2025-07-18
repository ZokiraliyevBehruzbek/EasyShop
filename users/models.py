from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=128)
    created_at = fields.DatetimeField(auto_now_add=True)
    # is_active = fields.BooleanField(default=True)
    # updated_at = fields.DatetimeField(auto_now=True)
    is_superuser = fields.BooleanField(default=False)
    

    def __str__(self):
        return self.username
