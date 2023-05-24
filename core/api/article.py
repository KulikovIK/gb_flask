from flask_combo_jsonapi import ResourceDetail, ResourceList

from core.schemas import ArticleSchema
from core.models.database import db
from core.models import Article


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }
