import time
import redis
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
def get_page_count():
    retries = 3
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
@app.route('/')
def helloWorld():
    count = get_page_count()
    return 'Hello World! You have been here {} times.\n'.format(count)
if __name__ == "__main__":
    app.run(debug=True)
