# 🌦️ Smart Weather Notifier
## Table of Contents
1. [Project Overview](#project-overview)
2. [Inspiration](#inspiration)
3. [Features](#features)
4. [Architecture](#architecture)
5. [API Endpoints](#api-endpoints)
6. [Technologies Used](#technologies-used)
7. [Setup and Installation](#setup-and-installation)
8. [Screenshots](#screenshots)
9. [Challenges](#challenges)
10. [Next Iterations](#next-iterations)
11. [Contributors](#contributors)

## 🚀 Project Overview

**Smart Weather Notifier** is a web application designed to provide users with personalized weather notifications based on their preferences. Whether you're a commuter wanting a heads-up about rain or an event planner needing daily forecasts, this app has you covered. Through simple user inputs, the app fetches real-time weather data from the OpenWeatherMap API and sends customized alerts via Brevo email notifications when conditions like rain, snow, or temperature drops are expected. 

This project was developed in a month as part of my portfolio to demonstrate my ability to build a full-stack application from scratch, integrating both front-end and back-end technologies, and using third-party APIs for real-world data.

## 🎯 Motivation

The inspiration behind this project stemmed from my personal need for reliable weather updates. As someone who often travels and plans events, I realized that receiving weather updates via notifications could make day-to-day activities more manageable. Instead of checking weather apps regularly, I wanted to create something that proactively informs users about upcoming weather changes, enabling them to plan ahead.

I also wanted to challenge myself with integrating a third-party API, setting up a database, and sending notifications—all things I hadn't worked with before. 

---

## 🛠️ Technologies Used

**Frontend:**
- React.js – For building a responsive and dynamic user interface.
- CSS – To enhance the visual appeal and responsiveness of the app.

**Backend:**
- Flask (Python) – For handling API requests, managing user preferences, and processing weather data.
- MySQL – For storing user preferences and historical weather data.
- Brevo – For sending email notifications to users based on their weather preferences.
- OpenWeatherMap API – For fetching real-time weather information.

---

## 🖼️ Features

### 1. **Real-time Weather Data**
   - Users can search for their desired location and instantly view weather data such as temperature, humidity, and weather conditions.

### 2. **Custom Weather Alerts**
   - Users can subscribe to receive notifications for specific weather conditions (rain, snow, etc.) for their selected location.

### 3. **Brevo Email Notifications**
   - Notifications are sent via email, thanks to integration with the Brevo API, alerting users when their specified weather condition is detected.

### 4. **Notification History**
   - Users can review their past notifications, helping them track previous weather alerts and conditions.

---

## 📈 Architecture Overview

Here’s a visual representation of the system architecture:

```plaintext
[ User ] <--> [ Frontend (React.js) ] <--> [ Backend (Flask) ] <--> [ MySQL Database ]
                  |
                  V
          [ OpenWeatherMap API ]
                  |
                  V
      [ Brevo for Email Notifications ]
```

- **Frontend:** React.js provides an intuitive interface for setting weather alerts, while managing user preferences and weather data.
- **Backend:** Flask handles API requests, processes weather data, stores user preferences, and triggers notifications.
- **Database:** MySQL stores user data, including preferences and past notifications.
- **OpenWeatherMap API:** Supplies real-time weather data.
- **Brevo:** Delivers email notifications based on the user's selected weather conditions.

---

## ⚙️ How It Works (Behind the Scenes)

When a user enters their preferred location and weather condition, the following steps take place:

1. **Weather Fetching:** The React frontend sends a request to the Flask backend to retrieve the weather data from the OpenWeatherMap API.
2. **Condition Matching:** The backend checks if the current weather condition matches the user's preferences stored in the MySQL database.
3. **Trigger Notifications:** If the conditions are met, the Flask backend sends a request to Brevo, which delivers an email to the user notifying them of the weather alert.
4. **Storing Notifications:** Each notification is logged in the MySQL database for future reference.

### **Why MySQL?**
Initially, the project was designed with PostgreSQL, but I decided to switch to MySQL because of my familiarity with it and its integration with Flask. MySQL’s simplicity allowed me to rapidly develop the database and integrate it smoothly with the rest of the application.

### **Algorithm Explanation**
The backend uses a simple matching algorithm. Once the weather data is fetched, it compares the user’s saved preferences (rain, snow, etc.) with the current weather conditions. If there’s a match, the notification is triggered. This approach is straightforward and effective for an MVP, but I plan to enhance it in the future by adding more granular conditions, like setting thresholds for temperature or humidity.

---

## 🧠 Challenges & Learning

Throughout the development process, I encountered various challenges:

- **API Integration:** Fetching data from the OpenWeatherMap API involved handling both location-based queries and error scenarios, such as invalid locations or API rate limits.
- **Database Management:** Managing user preferences and historical data in MySQL required efficient schema design and careful handling of relationships between tables.
- **Notification Service:** Integrating with Brevo for the first time presented its own learning curve. Initially, I struggled with authentication and formatting email content, but the documentation helped me get through it.

Despite these challenges, I was able to create a fully functional MVP. In future iterations, I aim to introduce SMS notifications, offer more customization for alerts, and refine the user interface to enhance usability.

---

## 🛠️ Setup & Installation

Follow these steps to set up the project locally:

### Prerequisites:
- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)
- MySQL Database
- Brevo account (for sending emails)

### 1. **Backend Setup (Flask)**
```bash
# Clone the repository
git clone https://github.com/your-username/smart-weather-notifier.git

# Navigate to the backend directory
cd backend

# Create a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install required packages
pip install -r requirements.txt

# Set up MySQL database and apply migrations
flask db upgrade

# Start the Flask server
flask run
```

### 2. **Frontend Setup (React)**
```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

---

## 🎨 Screenshots

| Dashboard          | Notification Subscription |
|--------------------|---------------------------|
| ![Dashboard](images/dashboard.png) | ![Subscription](images/subscription.png) |

---

## 🌟 Future Plans

- **SMS Notifications:** Implement SMS notifications via Twilio.
- **Additional Weather Metrics:** Add options to track additional weather metrics like wind speed or air quality.
- **UI/UX Enhancements:** Improve the frontend design for a more modern and user-friendly experience.
- **Mobile App:** Convert the web app into a cross-platform mobile app using React Native.

---

## 💬 Feedback

I’m constantly looking to improve this project, so if you have any feedback or suggestions, feel free to open an issue or reach out to me at jundiyusuf10@gmail.com.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- **Brevo** for providing a simple API for sending email notifications.
- **OpenWeatherMap** for real-time weather data.
- **ALX Software Engineering Program** for the guidance and inspiration.

