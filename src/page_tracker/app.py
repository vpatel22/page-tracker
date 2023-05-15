import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    """
    The home function that returns the number of page views from Redis (if available)
    """
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}", 500
    return f"This page has {page_views} page views"


@cache
def redis():
    """
    Returns the redis client using the url for the given env
    """
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
