from core.main_app import app


if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port="9900",
        debug=True
    )
