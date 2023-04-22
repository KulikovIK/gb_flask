from core.main_app import make_app, db


app = make_app()

@app.cli.command("init-db", help="create main db")
def init_db():
    db.create_all()
    print("db is done")

@app.cli.command("create-users")
def create_users():
    from core.models import User
    admin = User(username="admin", is_staff=True)
    james = User(username="james")

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print("users is done! created users:", admin, james)