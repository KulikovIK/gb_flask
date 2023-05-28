from flask_combo_jsonapi import ResourceDetail, ResourceList

from core.schemas import UserSchema
from core.models.database import db
from core.models import User
from core.permissions.user import UserPermission


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_get": [UserPermission],
    }
