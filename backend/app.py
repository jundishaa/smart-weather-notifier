from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
        return "Welcome to the Smart Weather Notifier Backend"

if __name__ == '__main__':
        app.run(debug=True)

db = mysql.connector.connect(
            host="localhost",
            user="jundi",
            password="jundi",
            database="smart_weather_db"
            )

cursor = db.cursor()
@app.route('/api/settings/<int:user_id>', methods=['GET'])
def get_settings(user_id):
        cursor.execute("SELECT * FROM weather_preferences WHERE user_id = %s", (user_id,))
        preferences = cursor.fetchall()
        return jsonify(preferences)

    @app.route('/api/settings', methods=['PUT'])
    def update_settings():
            data = request.json
            cursor.execute("""
                REPLACE INTO weather_preferences (user_id, location, condition, alert_time)
                VALUES (%s, %s, %s, %s)
                """, (data['user_id'], data['location'], data['condition'], data['alert_time']))
                db.commit()
     return jsonify({'status': 'Settings updated'})

 @app.route('/api/history/<int:user_id>', methods=['GET'])
 def get_history(user_id):
         cursor.execute("SELECT * FROM notifications WHERE user_id = %s", (user_id,))
         history = cursor.fetchall()
         return jsonify(history)

     @app.route('/api/notifications', methods=['POST'])
     def subscribe_notifications():
         data = request.json
         cursor.execute("""
              INSERT INTO notifications (user_id, date_sent, weather_condition, delivery_status)
              VALUES (%s, NOW(), %s, 'Pending')
            """, (data['user_id'], data['weather_condition']))
              db.commit()
         return jsonify({'status': 'Subscribed to notifications'})




