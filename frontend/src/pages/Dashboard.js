import React, { useEffect, useState } from 'react';

function Dashboard() {
	  const [settings, setSettings] = useState(null);

	useEffect(() => {
		    const dummySettings = {
			          location: 'New York',
			          condition: 'rain',
			          alertTime: '08:00 AM',
			          notificationMethod: 'email',
			        };
		    setSettings(dummySettings);
		  }, []);

	  return (
		      <div>
		        <h2>Dashboard</h2>
		        {settings ? (
				        <div>
				          <p><strong>Location:</strong> {settings.location}</p>
				          <p><strong>Condition:</strong> {settings.condition}</p>
				          <p><strong>Alert Time:</strong> {settings.alertTime}</p>
				          <p><strong>Notification Method:</strong> {settings.notificationMethod}</p>
				        </div>
				      ) : (
					              <p>Loading settings...</p>
					            )}
		      </div>
		    );
}

export default Dashboard;
