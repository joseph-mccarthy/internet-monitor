from datetime import datetime
import subprocess
import json
from time import sleep 
from database import Base, db_session, engine
from models.result import Result
from dateutil.parser import parse

def init_db():

    Base.metadata.create_all(bind=engine)
    print("Initialized the db")

def main(minutes):

    init_db()

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

if __name__ == '__main__':
    main(2)