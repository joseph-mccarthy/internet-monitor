from datetime import datetime
import subprocess
from time import sleep
from models.result import Result
import json
from database import Base, db_session, engine
from schedule import every, repeat, run_pending


def init_db():
    Base.metadata.create_all(bind=engine)


@repeat(every(30).minutes)
def run_speed_test():
    init_db()

    json_data = speed_test_cli()
    result = populate_model(json_data)

    db_session.add(result)
    db_session.commit()


def populate_model(json_data):
    result: Result = Result()
    result.download = json_data['download']
    result.upload = json_data['upload']
    result.ping = json_data['ping']
    result.timestamp = datetime.now()
    return result


def speed_test_cli():
    print_message("Speed Test Started")
    response = subprocess.Popen(
        'speedtest-cli --json', shell=True, stdout=subprocess.PIPE).stdout.read()
    json_data = json.loads(response)
    return json_data


def print_message(message: str):
    print(datetime.now().strftime("%d/%m/%Y-%H:%M:%S") + "\t" + message)


if __name__ == '__main__':
    run_speed_test()
    while True:
        run_pending()
        sleep(1)
