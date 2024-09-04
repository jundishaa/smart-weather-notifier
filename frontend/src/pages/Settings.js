import React, { useState } from 'react';

function Settings() {
	  const [location, setLocation] = useState('');
	  const [condition, setCondition] = useState('rain');
	  const [alertTime, setAlertTime] = useState('');
	  const [notificationMethod, setNotificationMethod] = useState('email');

	  const handleSubmit = (event) => {
		      event.preventDefault();
		  console.log({ location, condition, alertTime, notificationMethod });
		    };
	 return (
		     <div>
		       <h2>Settings</h2>
		       <form onSubmit={handleSubmit}>
		         <div>
		           <label>
		             Location:
		             <input
		               type="text"
		               value={location}
		               onChange={(e) => setLocation(e.target.value)}
		               required
		             />
		           </label>
		         </div>
		         <div>
		           <label>
		             Weather Condition:
		             <select
		               value={condition}
		               onChange={(e) => setCondition(e.target.value)}
		             >
		               <option value="rain">Rain</option>
		               <option value="snow">Snow</option>
		               <option value="temperature_drop">Temperature Drop</option>
		             </select>
		           </label>
		         </div>
		         <div>
		           <label>
		             Alert Time (e.g., 08:00 AM):
		             <input
		               type="time"
		               value={alertTime}
		               onChange={(e) => setAlertTime(e.target.value)}
		               required
		             />
		           </label>
		         </div>
		         <div>
		           <label>
		             Notification Method:
		             <select
		               value={notificationMethod}
		               onChange={(e) => setNotificationMethod(e.target.value)}
		             >
		               <option value="email">Email</option>
		               <option value="sms">SMS</option>
		             </select>
		           </label>
		         </div>
		         <button type="submit">Save Settings</button>
		       </form>
		     </div>
		   );
}

export default Settings;


