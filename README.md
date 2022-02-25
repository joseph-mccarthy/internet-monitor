# Internet Monitor

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=joseph-mccarthy_internet-monitor&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=joseph-mccarthy_internet-monitor)

![Project Image](banner.png)

## Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

Created this small and simple application to keep my Internet Service Provider honest. It's writtent in Python made up of two components. The first component is the speed test which is run every 30 minutes, and uses the [speedtest.net cli](https://www.speedtest.net/apps/cli) and stores the result in local sqlite database. The second component is a simple API that allows a client of choice to pull the data for the latest result, average of the last 24 hours and finally one for graphing.

## Technologies

- Python
- Flask
- SqlAlchemy
- Docker
- [Speedtest.net CLI](https://www.speedtest.net/apps/cli)

[Back To The Top](#internet-monitor)

---

## How To Use

There are two options to use this software. Can run with just python by checking out the repository or use the docker image.

### Python

To use this method you'll require at least Python 3.7 install on your machine

```sh
git clone git@github.com:joseph-mccarthy/internet-monitor.git
curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash
apt-get install speedtest
cd internet-monitor
pip3 install -r requirements.txt
./local-start.sh
```

### Docker

There is also a provided Docker image that runs both the speed test and the api with an exposed port of **5000**

```sh
docker pull joemccarthy/internet-monitor:latest
docker run -d -p 5000:5000 joemccarthy/internet-monitor:latest
```

### API Reference

The API exposes three endpoints for the data saved in the database

#### /latest

```json
{
    "download": 3296755.0,
    "upload": 2175216.0,
    "ping": 62.496,
    "time": 1645789388.759391
}
```

### /last-day

```json
{
    "download": {
        "high": 3852744.0,
        "average": 3629769.4166666665,
        "low": 3296755.0
    },
    "upload": {
        "high": 2331189.0,
        "average": 1883408.0416666667,
        "low": 1215527.0
    },
    "ping": {
        "high": 62.496,
        "average": 16.989,
        "low": 12.594
    }
}
```

#### /graph

```json
[
    {
        "id": 1,
        "download": 3364494.0,
        "upload": 1085589.0,
        "ping": 15.426,
        "time": 1645710501.983828
    },
    {
        "id": 2,
        "download": 3330109.0,
        "upload": 822428.0,
        "ping": 17.148,
        "time": 1645712303.276396
    },
    {
        "id": 3,
        "download": 3316571.0,
        "upload": 1076903.0,
        "ping": 15.835,
        "time": 1645714140.544144
    },
    {
        "id": 4,
        "download": 3261149.0,
        "upload": 1134400.0,
        "ping": 15.76,
        "time": 1645715986.757451
    }
]
```

[Back To The Top](#internet-monitor)

---

## Roadmap

- [ ] [#1](../../issues/1) Delete data after 30 days
- [ ] [#2](../../issues/2) Filter by date
- [ ] [#3](../../issues/3) Send Notifications

[Back To The Top](#internet-monitor)

---

## References

- [Speed Test CLI](https://www.speedtest.net/apps/cli)
- [Docker Hub Registry for Application](https://hub.docker.com/r/joemccarthy/internet-monitor)

[Back To The Top](#internet-monitor)

---

## License

Copyright (c) 2022 Joseph McCarthy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

[Back To The Top](#internet-monitor)

---

## Author Info

- [GitHub](https://github.com/joseph-mccarthy)
- [Website](https://joseph-mccarthy.github.io/)

[Back To The Top](#internet-monitor)
