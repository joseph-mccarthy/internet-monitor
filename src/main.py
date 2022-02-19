from datetime import datetime, timedelta, date
import subprocess
import json
from time import sleep 
from database import Base, db_session, engine
from sqlalchemy import func
from models.result import Result
from dateutil.parser import parse
from flask import Flask
import threading
from marshmallow import Schema, fields
from flask_cors import CORS, cross_origin

def init_db():

    Base.metadata.create_all(bind=engine)
    print("Initialized the db")

def init_api():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    class ObjectSchema(Schema):
     id = fields.Int()
     download = fields.Float()
     upload = fields.Float()
     ping = fields.Float()
     timestamp = fields.DateTime()


    object_schema = ObjectSchema()


    @app.route("/results")
    @cross_origin()
    def results():
        result = db_session.query(Result).all()
        return object_schema.dumps(result, many=True)

    @app.route("/latest")
    @cross_origin()
    def latest():
        result = db_session.query(Result).order_by(Result.id.desc()).first()
        return object_schema.dumps(result, many=False)

    @app.route("/today")
    @cross_origin()
    def last_day():
        delta = datetime.now() - timedelta(days = 1)
        result =  db_session.query(Result).filter(func.DATE(Result.timestamp) >= delta).all()
        return object_schema.dumps(result, many=True)


    app.run(debug=True);


def speed_test(minutes):
    while True:
        print(datetime.now().isoformat() + "\t Testing Internet Speed")
        response = subprocess.Popen('speedtest-cli --json', shell=True, stdout=subprocess.PIPE).stdout.read()
        test_data = json.loads(response)

        result:Result = Result()
        result.download = test_data['download']
        result.upload = test_data['upload']
        result.ping = test_data['ping']
        result.timestamp = parse(test_data['timestamp'])

        db_session.add(result)
        db_session.commit()
    
        sleep(minutes * 60)
def main(minutes):

    init_db()

    speed_test_thread = threading.Thread(target=speed_test, args=(minutes,))
    speed_test_thread.start()

    init_api()


if __name__ == '__main__':
    main(2) # TODO make this a command line argument else default to 30 minutes