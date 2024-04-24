# Standard Library
import decimal
import json
import uuid
from datetime import date, datetime
from typing import Any

# Third Party Stuff
from pydantic import BaseModel, HttpUrl
from pytz import timezone

from core.settings import settings


class EnvelopeResponse(BaseModel):
    success: Any | None = None
    message: Any | None = None
    data: Any | None = None

def create_envelope_response(data, success=None, message=None):
    return EnvelopeResponse(data=data, success=success, message=message).model_dump()



def get_current_date_time_to_app_standard() -> datetime:
    return datetime.now(timezone(settings.TIME_ZONE))


def get_current_date_time_utc() -> datetime:
    return datetime.now(timezone(settings.TIME_ZONE_UTC))


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)

        if isinstance(obj, datetime):
            return obj.isoformat()

        if isinstance(obj, date):
            return obj.isoformat()

        if isinstance(obj, decimal.Decimal):
            return float(obj)

        return json.JSONEncoder.default(self, obj)
