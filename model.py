from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, BigInteger
import os
from dotenv import load_dotenv
load_dotenv()


database_uri = os.environ.get("DB_URI")

db = SQLAlchemy()


def setup_db(app, database_uri=database_uri):
    with app.app_context():
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
        db.app = app
        db.init_app(app)
        db.create_all()


class Country(db.Model):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    common_name = Column(String)
    continent = Column(String)
    population = Column(BigInteger)
    currency = Column(String)
    cca3 = Column(String(3))
    official_language = Column(String)

    def __init__(self, common_name, continent, population, currency, cca3, official_language):
        self.common_name = common_name
        self.continent = continent
        self.population = population
        self.currency = currency
        self.cca3 = cca3
        self.official_language = official_language

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "Common Name": self.common_name,
            "Population": self.population,
            "Currency": self.currency,
            "CCA3": self.cca3,
            "Official Language": self.official_language
        }


class Continent(db.Model):
    __tablename__ = "continents"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
