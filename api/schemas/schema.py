from voluptuous import Schema
from voluptuous import ALLOW_EXTRA

user = Schema({
    "email": str,
    "password": str,
    "id": str
},
    extra=ALLOW_EXTRA,
    required=True
)

result = Schema({
    "result": {
        "expires": str,
        "title": str,
        "token": str,
        "user": {
            "id": int,
            "name": str,
            "news_last_seen":"2022-03-23 11:46:52"}}}
)