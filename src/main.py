import subprocess
import json 
from database import Base, db_session, engine
from models.result import Result
from dateutil.parser import parse

def init_db():

    Base.metadata.create_all(bind=engine)
    print("Initialized the db")

def main():

    init_db()

    response = subprocess.Popen('speedtest-cli --json', shell=True, stdout=subprocess.PIPE).stdout.read()
    test_data = json.loads(response)

    result:Result = Result()
    result.download = test_data['download']
    result.upload = test_data['upload']
    result.ping = test_data['ping']
    result.timestamp = parse(test_data['timestamp'])

    db_session.add(result)
    db_session.commit()

if __name__ == '__main__':
    main()