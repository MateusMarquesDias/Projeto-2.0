from flask import Flask, jsonify
import redis
import mysql.connector

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
db = mysql.connector.connect(
    host="mysql",
    user="my_user",
    password="my_password",
    database="my_database"
)

@app.route('/')
def hello():
    cache.incr('hits')
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM my_table")
    result = cursor.fetchone()[0]
    return jsonify({
        'message': 'Hello Docker Swarm!',
        'redis_hits': int(cache.get('hits')),
        'mysql_records': result
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
