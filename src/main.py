import subprocess
import json 

def main():
    response = subprocess.Popen('speedtest-cli --json', shell=True, stdout=subprocess.PIPE).stdout.read()
    test_data = json.loads(response)
    print(test_data['download'])
    print(test_data['upload'])
    print(test_data['ping'])
    print(test_data['timestamp'])


if __name__ == '__main__':
    main()