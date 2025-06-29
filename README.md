# 📅✨ Event Scheduler API

A simple 🐍 **Python Flask REST API** for scheduling events with full CRUD and search functionality — backed by persistent **JSON** storage. 💾

---

## 🚀 Features

- ➕ **Create** new events  
- 📋 **View** all events (sorted by start time)  
- ✏️ **Update** existing events  
- 🗑️ **Delete** events  
- 🔍 **Search** events by title or description  

---

## 🔧 Technologies Used

- 🐍 **Python 3.x**
- ⚡ **Flask**

---

## 📂 Setup Instructions

```bash
# 1️⃣ Clone the repository
git clone https://github.com/JiteshShelke/event-scheduler-api.git
cd event-scheduler-api

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the application
python app.py
```

> 🌐 App will run at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔗 API Endpoints

### ✅ Health Check

`GET /health`

📄 **Response:**
```json
{
  "status": "Event Scheduler API is running"
}
```

---

### 📋 Get All Events

`GET /events`

📄 **Returns:** All events, sorted by `start_time`.

---

### ➕ Create an Event

`POST /events`

📥 **Request Body Example:**
```json
{
  "title": "Team Meeting",
  "description": "Discuss project requirements",
  "start_time": "2025-06-29 10:00",
  "end_time": "2025-06-29 11:00"
}
```

📄 **Response:**
```json
{
  "message": "Event created",
  "event": { ... }
}
```

---

### ✏️ Update an Event

`PUT /events/{id}`

📥 **Request Body Example:**
```json
{
  "title": "Updated Meeting",
  "description": "Updated description",
  "start_time": "2025-06-29 11:00",
  "end_time": "2025-06-29 12:00"
}
```

📄 **Response:**
```json
{
  "message": "Event updated",
  "event": { ... }
}
```

---

### 🗑️ Delete an Event

`DELETE /events/{id}`

📄 **Response:**
```json
{
  "message": "Event deleted"
}
```

---

### 🔍 Search Events

`GET /events/search?q=meeting`

📄 **Response:**
```json
{
  "results": [ ... ],
  "count": 1
}
```

---

## 🧪 Example API Calls & Outputs

### 📋 GET All Events

`GET http://127.0.0.1:5000/events`

📤 Output:
```json
[
  {
    "id": 1,
    "title": "Team Meeting",
    "description": "Discuss project requirements",
    "start_time": "2025-06-29 10:00",
    "end_time": "2025-06-29 11:00"
  }
]
```

---

### ➕ POST Create Event

`POST http://127.0.0.1:5000/events`

📥 Input (JSON):
```json
{
  "title": "Team Meeting",
  "description": "Discuss project requirements",
  "start_time": "2025-06-29 10:00",
  "end_time": "2025-06-29 11:00"
}
```

📤 Output:
```json
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
```

---

## 📦 Dependencies

- ⚡ Flask

📥 Install:
```bash
pip install Flask
```

---

## 📁 Project Structure

```
event-scheduler-api/
├── app.py               # Main Flask app
├── events.json          # JSON storage file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🌐 GitHub Repository

🔗 [https://github.com/JiteshShelke/event-scheduler-api](https://github.com/JiteshShelke/event-scheduler-api)

---

## ✨ Author

👤 **Jitesh Shelke**

---
