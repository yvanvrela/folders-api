from flask import Flask
from app.handlers.errors_handler import page_not_found


def register_handlers(app: Flask) -> None:
    app.register_error_handler(404, page_not_found)
