from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from .baseapi import AbstractScheduleAPI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orders.db"
db = SQLAlchemy(app)
bus = bootstrap.bootstrap()


class FlaskSchedulingAPI(AbstractScheduleAPI):
    """
    Flask
    """

    def __init__(self) -> None:
        super().__init__()

    @app.route("/")
    def index(self):
        return f"Scheduling API"

    @app.route("/api/one/<id>")
    def one(self, id):
        return f"The provided id is {id}"

    @app.route("/api/all")
    def all(self):
        return f"all records"

    @app.route("/api/first/<property>/<value>/<sort>")
    def first(self, filter, value, sort):
        return f"the first "
        pass

    def many(self, filter, value, sort):
        pass

    def add(oeder):
        pass

    def delete(order):
        pass

    def update(order):
        pass
