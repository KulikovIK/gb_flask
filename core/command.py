from core.main_app import db
from wsgi import app
import os

@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


# @app.cli.command("create-users")
# def create_users():
#     """
#     Run in your terminal:
#     flask create-users
#     > done! created users: <User #1 'admin'> <User #2 'james'>
#     """
#     from blog.models import User
#     admin = User(username="admin", is_staff=True)
#     james = User(username="james")
#     db.session.add(admin)
#     db.session.add(james)
#     db.session.commit()
#     print("done! created users:", admin, james)

@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from core.models import User

    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"
    db.session.add(admin)
    db.session.commit()
    print("created admin:", admin)
