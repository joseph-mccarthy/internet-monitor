from datetime import datetime
import subprocess
from models.result import Result
from dateutil.parser import parse
import json
from database import Base, db_session, engine
from time import sleep


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