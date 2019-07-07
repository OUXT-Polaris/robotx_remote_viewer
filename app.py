import os
from os.path import join, dirname

from flask import Flask,render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_mqtt import Mqtt

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['MQTT_BROKER_URL'] = os.environ.get('MQTT_BROKER_URL')
app.config['MQTT_BROKER_PORT'] = int(os.environ.get('MQTT_BROKER_PORT'))
app.config['MQTT_USERNAME'] = os.environ.get('MQTT_USERNAME')
app.config['MQTT_PASSWORD'] = os.environ.get('MQTT_PASSWORD')
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host=os.environ.get('APP_IP'), port=os.environ.get('APP_PORT'))