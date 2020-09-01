from datetime import datetime
import time
import json

from flask import Blueprint, make_response, jsonify, Response, request
from .models import Event
from .utils import weekly, monthly
from flask_restful import Resource, reqparse
from . import db
from sqlalchemy import func, between


class Info(Resource):
    def get(self) -> Response:
        queryset = Event.query.all()

        response = jsonify(
            [
                {
                    "id": row.id,
                    "asin": row.asin,
                    "brand": row.brand,
                    "event_id": row.event_id,
                    "source": row.source,
                    "stars": row.stars,
                    "timestamp": row.timestamp,
                }
                for row in queryset
            ]
        )

        return response


class Tmimeline(Resource):
    def get(self, d_type="usual", grouping="monthly", *filters) -> Response:
        args = request.args

        startDate = int(
            time.mktime(datetime.strptime(args["startDate"], "%Y-%m-%d").timetuple())
        )
        endDate = int(
            time.mktime(datetime.strptime(args["endDate"], "%Y-%m-%d").timetuple())
        )

        queryset = (
            db.session.query(Event.timestamp, func.count(Event.timestamp))
            .filter((startDate <= Event.timestamp) & (Event.timestamp <= endDate))
            .group_by(Event.timestamp)
            .all()
        )
        response = [
            {
                "date": datetime.utcfromtimestamp(int(row[0])).strftime("%Y-%m-%d"),
                "value": int(row[1]),
            }
            for row in queryset
        ]
        if args["Grouping"] == "weekly":
            response = weekly(7, response)
        elif args["Grouping"] == "bi-weekly":
            response = weekly(14, response)
        elif args["Grouping"] == "monthly":
            response = monthly(response)
        return {"timeline": response}
