import redis
from celery import shared_task
import time

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@shared_task
def generate_csv(self):
    time.sleep(10)
    result = 'http://www.google.com'
    redis_client.publish(self.request.id, result)
