
m flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import requests
import os
from dotenv import load_dotenv  # Import dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

# Fetch sensitive credentials from environment variables
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

# OpenWeatherMap API Key
OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

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
    user_id = data['user_id']
    location = data['location']
    weather_condition = data['weather_condition']

    # Fetch weather data
    weather = get_weather(location)
    if weather['condition'] == weather_condition:
        # Send email notification
        send_email(data['email'], 'Weather Alert', f"Alert: {weather_condition} expected in {location}.")

    cursor.execute("""
        INSERT INTO notifications (user_id, date_sent, weather_condition, delivery_status)
        VALUES (%s, NOW(), %s, 'Pending')
    """, (user_id, weather_condition))
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

# Function to send email via SendGrid
def send_email(to_email, subject, content):
    message = Mail(
        from_email='your_email@example.com',
        to_emails=to_email,
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

# Function to send SMS via Twilio
def send_sms(to_number, message_body):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=to_number
    )
    print(message.sid)

if __name__ == '__main__':
    app.run(debug=True)

