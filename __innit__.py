from app import app


def clever_function():
    return "HELLO"


app.jinja_env.globals.update(clever_function=clever_function)
