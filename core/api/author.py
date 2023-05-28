from flask_combo_jsonapi import ResourceDetail, ResourceList
from combojsonapi.event.resource import EventsResource

from core.schemas import AuthorSchema
from core.models.database import db
from core.models import Author, Article


class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {"count": Article.query.filter(Article.author_id == kwargs["id"]).count()}


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    events = AuthorDetailEvents
    data_layer = {
        "session": db.session,
        "model": Author,
    }
