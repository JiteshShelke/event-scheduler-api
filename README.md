# Event Scheduler API

A simple Python Flask REST API for scheduling events with create, read, update, delete, and search functionalities, including persistent JSON storage.

## 🚀 Features

- Create new events
- View all events (sorted by start time)
- Update existing events
- Delete events
- Search events by title or description
- Health check endpoint

## 🔧 Technologies Used

- Python 3.x
- Flask

## 📂 Setup Instructions

1. Clone the repository:

   git clone https://github.com/JiteshShelke/event-scheduler-api.git
   cd event-scheduler-api

2. Install dependencies:

   pip install -r requirements.txt

3. Run the application:

   python app.py

The server will start at:

   http://127.0.0.1:5000

## 🔗 API Endpoints

### Health Check

GET /health

Response:

{
  "status": "Event Scheduler API is running"
}

### Get all events

GET /events

Returns all events sorted by start time.

### Create an event

POST /events

Body example:

{
  "title": "Team Meeting",
  "description": "Discuss project requirements",
  "start_time": "2025-06-29 10:00",
  "end_time": "2025-06-29 11:00"
}

Response:

{
  "message": "Event created",
  "event": { ... }
}

### Update an event

PUT /events/{id}

Body example:

{
  "title": "Updated Meeting",
  "description": "Updated description",
  "start_time": "2025-06-29 11:00",
  "end_time": "2025-06-29 12:00"
}

Response:

{
  "message": "Event updated",
  "event": { ... }
}

### Delete an event

DELETE /events/{id}

Response:

{
  "message": "Event deleted"
}

### Search events

GET /events/search?q=meeting

Response:

{
  "results": [ ... ],
  "count": 1
}

## 📝 Example Commands and Outputs

### Get all events

Send GET request via Postman or browser to http://127.0.0.1:5000/events

Output:

[
  {
    "id": 1,
    "title": "Team Meeting",
    "description": "Discuss project requirements",
    "start_time": "2025-06-29 10:00",
    "end_time": "2025-06-29 11:00"
  }
]

### Create an event

Send POST request to http://127.0.0.1:5000/events with the example JSON body above.

Output:

{
  "message": "Event created",
  "event": {
    "id": 2,
    "title": "Team Meeting",
    "description": "Discuss project requirements",
    "start_time": "2025-06-29 10:00",
    "end_time": "2025-06-29 11:00"
  }
}

## 📌 Dependencies

- Flask

Install via:

pip install Flask

## 📁 File Structure

event-scheduler-api/
├── app.py
├── events.json
├── requirements.txt
└── README.md

## 🔗 GitHub Repository

https://github.com/JiteshShelke/event-scheduler-api

## ✨ Author

Jitesh Shelke

## 💡 Note

For production deployment, use a production WSGI server like Gunicorn instead of the Flask development server.
