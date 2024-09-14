# RunnerBoi - Workout Tracker API + Basic Frontend Full Stack Web App
<img width="1008" alt="Screenshot 2024-09-14 at 5 33 51 AM" src="https://github.com/user-attachments/assets/9c264870-d940-4685-a0ba-64fdbfb1d32d">

## Description

The **RunnerBoi API** is a FastAPI-based REST API designed to allow users to track their running workouts. Users can create, retrieve, and delete workout records. The API also fetches real-time weather data from the Open-Meteo API for Chapel Hill at the time of the workout. This feature is still in development though, as right now it uses the current time open API that just returns weather data for the time of submission, and not filtered by the date and time entered by user.

The backend connects to a **PostgreSQL** database hosted on **Amazon RDS** and is deployed on an **Amazon EC2** server instance. The frontend built using HTML+CSS+JS interacts with the API to display and manage the workouts.

## Features

- **Create a Workout**: Users can log a new workout including details like distance, duration, route, heart rate, and a photo URL.
- **Fetch Weather Data**: The app fetches the current weather data for Chapel Hill (hard-coded longitude and latitude) and stores it with the workout.
- **Get All Workouts**: Users can get a list of all workouts, along with relevant details. 
- **Delete Workouts**: Users can delete a workout by its ID.
- **Frontend**: Interacts with API, allows user to manipulate database

## Technologies Used

- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Pydantic**: Data validation in FastAPI.
- **Amazon RDS**: Cloud-hosted PostgreSQL database.
<img width="756" alt="Screenshot 2024-09-14 at 5 36 40 AM" src="https://github.com/user-attachments/assets/cc09aae2-52a3-4f25-96d4-61a3811744e0">

- **Amazon EC2**: Server for hosting the API.
  <img width="892" alt="Screenshot 2024-09-14 at 5 36 06 AM" src="https://github.com/user-attachments/assets/3b7a9542-a2f9-4a95-b1bb-79cdfc14ec40">
- **Open-Meteo API**: External API for real-time weather data that doesn't require API key(was easier for me to use with time constraints)
<img width="1081" alt="Screenshot 2024-09-14 at 5 37 16 AM" src="https://github.com/user-attachments/assets/f70f1c0d-faf1-4246-b8af-04067574dc1c">
- **HTML,CSS JavaScript**: Simple frontend to interact with the API.

## API Endpoints
<img width="1128" alt="Screenshot 2024-09-14 at 5 35 20 AM" src="https://github.com/user-attachments/assets/90faf0ea-1c91-4ed2-9bd2-88a1d08283a2">

### Create a Workout

- **Endpoint**: `/workouts/`
- **Method**: `POST`
- **Request Body**: 
{
  "date_time": "2024-09-14T07:28:09.159Z",
  "duration": 7,
  "distance": 8,
  "route": "string",
  "heart_rate": 0,
  "photo_url": "string",
  "weather": "string"
}

### Get a Workout by ID

- **Endpoint**: `/workouts/{workout_id}`
- **Method**: `GET`
- **Parameters**: 
workout_id: int

### Get All Workouts

- **Endpoint**: `/workouts/`
- **Method**: `GET`
- **Parameters**: 
None

### Delete a Workout by ID

- **Endpoint**: `/workouts/{workout_id}`
- **Method**: `DELETE`
- **Parameters**: 
workout_id: int

## How To
If my EC2 server is running actively, then you can access the FAST API docs through:

http://52.54.255.219:8000/docs

and you can access the connected full stack web app through: 

http://52.54.255.219:8000/static/index.html

Else, you can just test the API by pip installing the requirements.txt and then running the api through your local by doing a command like:

uvicorn work_api:app --reload

and then opening the link then doing /docs to interact with the API. 



