import time
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

def get_visit_count():
    retries = 5
    while True:
        try:
            return r.incr('hits')
        except redis.exceptions.ConnectionError as e:
            if retries == 0:
                raise e
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def show_visit_count():
    visit_count = get_visit_count()
    return '### App visitor count Docker v.0.0.2 #####\nThis is the {} visitor.\n'.format(visit_count)
