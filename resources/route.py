from flask import Flask, jsonify


class Hello:
    vic = Flask(__name__)

    @vic.route('/vic/', methods=["GET", "POST"])
    def hello(self):
        return jsonify({"name": "Thabo"})
