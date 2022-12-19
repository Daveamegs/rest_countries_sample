from flask import Flask, jsonify, abort
from model import setup_db, Country


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    @app.route("/")
    def index():
        return "Hi, welcome!!!, please make a request to the following endpoint to retrieve the names of the countries and their attributes 'localhost:5000/countries'"

    @app.route("/countries", methods=["GET"])
    def countries():
        data = Country.query.all()

        if len(data) == 0:
            abort(404)

        country_data = [dat.format() for dat in data]

        return jsonify({
            "success": True,
            "data": country_data,
            "length": len(data)
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error_code": 404,
            "error_message": "resource not found"
        }), 404

    return app
