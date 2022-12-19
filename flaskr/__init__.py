from flask import Flask, jsonify, abort
from model import setup_db, Country


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    @app.route("/")
    def index():
        data = Country.query.all()

        contry_one = [dat.format() for dat in data]
        return jsonify({
            "data": contry_one,
            "length": len(data)
        })

    @app.route("/countries", methods=["GET"])
    def countries():
        # countries = Country.query.all()

        # if len(countries) == 0:
        #     abort(404)

        return jsonify({
            "success": True,
            # "data": [data for data in countries]
        })

    return app
