from datetime import datetime, timedelta
import json
from database import Base, db_session, engine
from sqlalchemy import func
from models.result import Result
from flask import Flask, Response
from flask_cors import CORS


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Initialized the db")


def init_api():
    app = Flask(__name__)
    CORS(app)

    @app.route("/last-day")
    def daily_average():
        delta = datetime.now() - timedelta(days=1)
        result = db_session.query(Result).filter(
            func.DATE(Result.timestamp) >= delta).all()

        download_data = []
        upload_data = []
        ping_data = []

        for item in result:
            download_data.append(item.download)
            upload_data.append(item.upload)
            ping_data.append(item.ping)

        response = {
            "download": {
                "high": max(download_data),
                "average": sum(download_data) / len(download_data),
                "low": min(download_data)
            },
            "upload": {
                "high": max(upload_data),
                "average": sum(upload_data) / len(upload_data),
                "low": min(upload_data)
            },
            "ping": {
                "high": max(ping_data),
                "average": sum(ping_data) / len(ping_data),
                "low": min(ping_data)
            }
        }

        return Response(json.dumps(response),  mimetype='application/json')

    @app.route("/latest")
    def latest_result():
        result = db_session.query(Result).order_by(Result.id.desc()).first()
        response = {
            "download": result.download,
            "upload": result.upload,
            "ping": result.ping,
            "time": result.timestamp.timestamp()
        }
        return Response(json.dumps(response),  mimetype='application/json')

    @app.route("/graph")
    def graph():
        delta = datetime.now() - timedelta(days=30)
        result = db_session.query(Result).filter(
            func.DATE(Result.timestamp) >= delta).all()

        json_list = []

        for item in result:
            json_list.append({
                "id": item.id,
                "download": item.download,
                "upload": item.upload,
                "ping": item.ping,
                "time": item.timestamp.timestamp()
            })

        return Response(json.dumps(json_list),  mimetype='application/json')

    app.run(debug=True, host="0.0.0.0")


def main():
    init_db()
    init_api()


if __name__ == "__main__":
    main()
