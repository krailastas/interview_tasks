import redis
from django.conf import settings

redis_cache = redis.Redis(host=settings.REDIS_URL, port=6379, db=0)
