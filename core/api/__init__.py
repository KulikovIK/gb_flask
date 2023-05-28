from flask_combo_jsonapi import Api
from combojsonapi.spec import ApiSpecPlugin
from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin

from core.api.article import ArticleDetail, ArticleList
from core.api.author import AuthorDetail, AuthorList
from core.api.tag import TagDetail, TagList
from core.api.user import UserDetail, UserList


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Article": "Article API",
            "Author": "Author API",
            "Tag": "Tag API",
            "User": "User API",
        }
    )

    return api_spec_plugin


def init_api(app):
    event_plugin = EventPlugin()
    api_spec_plugin = create_api_spec_plugin(app)
    permission_plugin = PermissionPlugin(strict=False)
    api = Api(
        app=app,
        plugins=[
            api_spec_plugin,
            event_plugin,
            permission_plugin,
        ],
    )

    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>/", tag="Author")
    api.route(TagList, "tag_list", "/api/tags/")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/")
    api.route(UserList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")

    return api
