from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from core.models import User

users_app = Blueprint(
    'users_app',
    __name__,
    static_folder='../static',
    url_prefix='/users')


@users_app.route("/")
def users_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)

@users_app.route("/<int:user_id>/")
def user_details(user_id: int):
    
    try:
        users = User.query.filter_by(id=user_id).one_or_none()
    except:
        raise NotFound(f"Пользователь #{user_id} не существует!")
    
    return render_template('users/details.html', user=users)
