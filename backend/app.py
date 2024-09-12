
m flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import requests

# OpenWeatherMap API Key
OPENWEATHERMAP_API_KEY = "92cffacb7424016e5cccbf19a528de7b"

app = Flask(__name__)
CORS(app)

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="jundi",
    password="jundi",
    database="smart_weather_db"
)
cursor = db.cursor()

@app.route('/')
def home():
    return "Welcome to the Smart Weather Notifier Backend"

# Get user settings (preferences)
@app.route('/api/settings/<int:user_id>', methods=['GET'])
def get_settings(user_id):
    cursor.execute("SELECT * FROM weather_preferences WHERE user_id = %s", (user_id,))
    preferences = cursor.fetchall()
    return jsonify(preferences)

# Update user settings (preferences)
@app.route('/api/settings', methods=['PUT'])
def update_settings():
    data = request.json
    cursor.execute("""
        REPLACE INTO weather_preferences (user_id, location, condition, alert_time)
        VALUES (%s, %s, %s, %s)
    """, (data['user_id'], data['location'], data['condition'], data['alert_time']))
    db.commit()
    return jsonify({'status': 'Settings updated'})

# Get user notification history
@app.route('/api/history/<int:user_id>', methods=['GET'])
def get_history(user_id):
    cursor.execute("SELECT * FROM notifications WHERE user_id = %s", (user_id,))
    history = cursor.fetchall()
    return jsonify(history)

# Subscribe to weather notifications
@app.route('/api/notifications', methods=['POST'])
def subscribe_notifications():
    data = request.json
    cursor.execute("""
        INSERT INTO notifications (user_id, date_sent, weather_condition, delivery_status)
        VALUES (%s, NOW(), %s, 'Pending')
    """, (data['user_id'], data['weather_condition']))
    db.commit()
    return jsonify({'status': 'Subscribed to notifications'})

# Get current weather data from OpenWeatherMap API
@app.route('/api/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')  # Example: 'London'
    if not location:
        return jsonify({'error': 'Location is required'}), 400

    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHERMAP_API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

    weather_data = response.json()

    return jsonify({
        'location': weather_data['name'],
        'temperature': weather_data['main']['temp'],
        'condition': weather_data['weather'][0]['description']
    })

if __name__ == '__main__':
    app.run(debug=True)

