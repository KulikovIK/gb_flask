from core.main_app import make_app


if __name__ == '__main__':
    app = make_app()
    app.run(
        host="127.0.0.1",
        port="9900",
        debug=True
    )
