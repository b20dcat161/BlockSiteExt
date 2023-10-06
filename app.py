# app.py
from flask import Flask, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
@app.route('/url_log', methods=['POST'])
def collect_url():
    try:
        data = request.json
        url = data.get('url')
        print("Received data:",data)
        print('Received URL:', url)
        now = datetime.now()
        current_date = now.date()
        print(current_date)
        with open('url_logs.txt', 'a') as file:
            current_time = now
            file.write('{'+f'"time":"{current_time}","current_url":"{url}","write":"yes"'+'}\n')
        return {'message': 'Received and processed URL successfully', 'blockornot':'block'}, 200
    except Exception as e:
        print('Error when receiving and processing the URL:', e)
        return {'error': 'Error when receiving and processing the URL.'}, 500

if __name__ == '__main__':
    app.run()
