import React from 'react';
import { Link } from 'react-router-dom';
import { Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Settings from './pages/Settings';
import NotificationHistory from './pages/NotificationHistory';
import Weather from './Weather';
import RegistrationForm from './RegistrationForm';


function App() {
console.log('API URL:', process.env.REACT_APP_API_URL);
console.log('API Key:', process.env.REACT_APP_API_KEY);
    return (
        <div className="App">
            <header className="App-header">
                <h1>Smart Weather Notifier</h1>
                <nav>
                    <Link to="/">Dashboard</Link> |{" "}
                    <Link to="/settings">Settings</Link> |{" "}
                    <Link to="/history">Notification History</Link>
                </nav>
            </header>
            <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/settings" element={<Settings />} />
                <Route path="/history" element={<NotificationHistory />} />
            </Routes>
            <Weather /> {/* Assuming this is your weather display component */}
        </div>
    );
}

export default App;

