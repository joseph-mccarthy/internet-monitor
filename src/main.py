from datetime import datetime
from distutils.log import debug
import subprocess
import json
from time import sleep 
from database import Base, db_session, engine
from models.result import Result
from dateutil.parser import parse
from flask import Flask
import threading
from marshmallow import Schema, fields

def init_db():

    Base.metadata.create_all(bind=engine)
    print("Initialized the db")

def init_api():
    app = Flask(__name__)
    
    class ObjectSchema(Schema):
     id = fields.Int()
     download = fields.Float()
     upload = fields.Float()
     ping = fields.Float()
     timestamp = fields.DateTime()




    @app.route("/results")
    def results():
        result = db_session.query(Result).all()
        object_schema = ObjectSchema()
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
    main(2)