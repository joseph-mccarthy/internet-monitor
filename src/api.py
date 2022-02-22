from datetime import datetime, timedelta
from database import Base, db_session, engine
from sqlalchemy import func
from models.result import Result
from flask import Flask
from marshmallow import Schema, fields
from flask_cors import CORS, cross_origin

def init_db():

    Base.metadata.create_all(bind=engine)
    print("Initialized the db")

def init_api():
    app = Flask(__name__)
    CORS(app)

    class ObjectSchema(Schema):
     id = fields.Int()
     download = fields.Float()
     upload = fields.Float()
     ping = fields.Float()
     timestamp = fields.DateTime()


    object_schema = ObjectSchema()


    @app.route("/results")
    def results():
        result = db_session.query(Result).all()
        return object_schema.dumps(result, many=True)

    @app.route("/latest")
    def latest():
        result = db_session.query(Result).order_by(Result.id.desc()).first()
        return object_schema.dumps(result, many=False)

    @app.route("/today")
    def last_day():
        delta = datetime.now() - timedelta(days = 1)
        result =  db_session.query(Result).filter(func.DATE(Result.timestamp) >= delta).all()
        return object_schema.dumps(result, many=True)

    app.run(debug=True,host="0.0.0.0");



def main():

    init_db()
    init_api()


if __name__ == '__main__':
    main() 