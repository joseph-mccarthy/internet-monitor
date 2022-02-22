from datetime import datetime, timedelta
from database import Base, db_session, engine
from sqlalchemy import func
from models.result import Result
from flask import Flask
from flask_cors import CORS, cross_origin
from models.resultSchema import ResultSchema

def init_db():

    Base.metadata.create_all(bind=engine)
    print("Initialized the db")

def init_api():
    app = Flask(__name__)
    CORS(app)

    result_schema = ResultSchema()


    @app.route("/daily-average")
    def daily_average():
        result = db_session.query(Result).all()
        return result_schema.dumps(result, many=True)

    @app.route("/latest-result")
    def latest_result():
        result = db_session.query(Result).order_by(Result.id.desc()).first()
        return result_schema.dumps(result, many=False)

    @app.route("/graph")
    def graph():
        delta = datetime.now() - timedelta(days = 1)
        result =  db_session.query(Result).filter(func.DATE(Result.timestamp) >= delta).all()
        return result_schema.dumps(result, many=True)

    app.run(debug=True,host="0.0.0.0");



def main():

    init_db()
    init_api()


if __name__ == '__main__':
    main() 