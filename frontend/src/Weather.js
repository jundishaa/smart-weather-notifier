import React, { useState } from 'react';

const Weather = () => {
    const [location, setLocation] = useState('');
    const [weather, setWeather] = useState(null);
    const [error, setError] = useState('');

    const fetchWeather = async () => {
        try {
            // Use the environment variable for the API URL
            const apiUrl = process.env.REACT_APP_WEATHER_API_URL;
            const response = await fetch(`${apiUrl}?location=${location}`);
            const data = await response.json();
            if (response.ok) {
                setWeather(data);
                setError('');
            } else {
                setError(data.error || 'Failed to fetch weather data');
            }
        } catch (error) {
            setError('Error fetching weather data');
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetchWeather();
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={location}
                    onChange={(e) => setLocation(e.target.value)}
                    placeholder="Enter location"
                />
                <button type="submit">Get Weather</button>
            </form>

            {error && <p>{error}</p>}
            {weather && (
                <div>
                    <h3>Weather in {weather.location}</h3>
                    <p>Temperature: {weather.temperature}°C</p>
                    <p>Condition: {weather.condition}</p>
                </div>
            )}
        </div>
    );
};

export default Weather;

