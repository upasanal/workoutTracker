const API_URL = "http://52.54.255.219:8000";
// deployed API connect to Amazon RDS PostgresSQL instance using Amazon EC2 Server!

// Create a new workout
document.getElementById("workoutForm").addEventListener("submit", async function(event) {
  event.preventDefault();
// async = imp for UI to continue to be responsive, processes run in the back
  const workout = {
    date_time: (document.getElementById("date_time").value),  // Local date and time
    distance: parseFloat(document.getElementById("distance").value), 
    duration: parseInt(document.getElementById("duration").value, 10), //integer conversion
    route: document.getElementById("route").value || null,
    heart_rate: document.getElementById("heart_rate").value ? parseInt(document.getElementById("heart_rate").value, 10) : null, //convert into integer
    photo_url: document.getElementById("photo_url").value || null
  };
  
  console.log("Submitting workout:", workout);

  try {
    // Fetch the weather for Chapel Hill specifically (hard coded in terms of simplicity rn)
    const weather = await fetchWeatherData();

    workout.weather = weather;


    const response = await fetch(`${API_URL}/workouts/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(workout) //javascript to json convert
    });
    //API call to create workout

    if (response.ok) {
      alert("Workout added successfully!");
      getWorkouts();  // Refreshes the workout list, the create and get all workouts in the API are not connected obvi, it is a front end feature!
    } else {
      alert("Failed to add workout.");
    }
  } catch (error) {
    console.error("Error:", error);
  }
});


async function fetchWeatherData() {
  const latitude = 35.9132; // Chapel Hill latitude
  const longitude = -79.0558; // Chapel Hill longitude
  const url = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`;
// uses Open Meteo that requires no key, does current_weather not based on user entered date/time but i am just going with it for
// the sake of time 
  try {
    const response = await fetch(url);
    const weatherData = await response.json();

    if (weatherData && weatherData.current_weather) {
      const temperatureCelsius = weatherData.current_weather.temperature;
      const temperatureFahrenheit = (temperatureCelsius * 9/5) + 32;  // Convert to Fahrenheit bc the API response is in celsius
      return `${temperatureFahrenheit}°F`; 
    }
  } catch (error) {
    console.error("Error fetching weather data:", error);
  }

  return "Weather data unavailable";
}

// get the workouts, display in table!
async function getWorkouts() {
  try {
    const response = await fetch(`${API_URL}/workouts/`);
    // fetch defaults to get when no other method specified
    const workouts = await response.json();

    // Clear the table before adding new data
    const tableBody = document.getElementById("workoutTableBody");
    tableBody.innerHTML = "";

    workouts.forEach(workout => {
      const localDateTime = new Date(workout.date_time).toLocaleString();
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${workout.id}</td>
        <td>${workout.distance}</td>
        <td>${workout.duration}</td>
        <td>${localDateTime}</td>  
        <td>${workout.route ? workout.route : ''}</td>
        <td>${workout.heart_rate ? workout.heart_rate : ''}</td>
        <td>${workout.photo_url ? `<a href="${workout.photo_url}" target="_blank">Photo</a>` : ''}</td>
        <td>${workout.weather ? workout.weather : 'N/A'}</td>  <!-- Weather column -->
        <td><button onclick="deleteWorkout(${workout.id})">Delete</button></td>
      `;
      tableBody.appendChild(row);
    });
  } catch (error) {
    console.error("Error:", error);
  }
}

// Delete a workout by ID
async function deleteWorkout(workoutId) {
  try {
    const response = await fetch(`${API_URL}/workouts/${workoutId}`, {
      method: "DELETE"
    });

    if (response.ok) {
      alert("Workout deleted successfully!");
      getWorkouts(); // Refreshes the workout list, the create and get all workouts in the API are not connected obvi, it is a front end feature!
    } else {
      alert("Failed to delete workout.");
    }
  } catch (error) {
    console.error("Error:", error);
  }
}
