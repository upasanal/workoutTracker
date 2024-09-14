# Runner Boi - Workout Tracker API + Basic Frontend Full Stack Web App

## Description

The **Workout Tracker API** is a FastAPI-based REST API designed to allow users to track their running workouts. Users can create, retrieve, and delete workout records. The API also fetches real-time weather data from the Open-Meteo API for Chapel Hill at the time of the workout. This feature is still in development though, as right now it uses the current time open API that just returns weather data for the time of submission, and not filtered by the date and time entered by user.

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
- **Amazon EC2**: Server for hosting the API.
- **Open-Meteo API**: External API for real-time weather data that doesn't require API key(was easier for me to use with time constraints)
- **HTML,CSS JavaScript**: Simple frontend to interact with the API.

## API Endpoints

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

and then oppening the link then doing /docs to interact with the API. 



