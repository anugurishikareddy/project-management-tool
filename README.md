# 📋 Project Management Tool

A full-stack Project Management Tool developed to help users manage projects, tasks, comments, and notifications in one place.

The application provides a simple dashboard where users can log in, create projects, manage tasks, add comments, and view notifications.

## 🚀 Features

* 🔐 User Login & Authentication
* 📁 Create and View Projects
* 📝 Create and Manage Tasks
* 📌 Task Status Management
* ⭐ Task Priority Management
* 💬 Add Comments to Tasks
* 💭 View Comments
* 🔔 Notifications
* 🌐 REST API Backend
* 🔌 WebSocket Configuration for Real-Time Communication
* 📊 Simple Dashboard Interface

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Django
* Django REST Framework
* Django Channels

### Database

* SQLite

### Authentication

* Token/JWT-based authentication

### Real-Time Communication

* WebSocket
* Django Channels
* ASGI

## 📂 Project Structure

```text
project-management-tool/
│
├── backend/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── core/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── consumers.py
│   │   ├── routing.py
│   │   ├── urls.py
│   │   └── tests.py
│   │
│   ├── manage.py
│   └── db.sqlite3
│
└── frontend/
    └── index.html
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/anugurishikareddy/project-management-tool.git
```

### 2. Open the Backend Folder

```bash
cd project-management-tool
cd backend
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows:

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install django djangorestframework channels daphne
```

## ▶️ Run the Project

From the `backend` folder:

```powershell
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 🔑 Authentication

Users can log in through the dashboard.

After successful authentication, the access token is stored in the browser and used for authenticated API requests.

## 📡 API Endpoints

### Authentication

```text
POST /api/register/
POST /api/token/
POST /api/login/
```

### Projects

```text
GET  /api/projects/
POST /api/projects/
```

### Tasks

```text
GET  /api/tasks/
POST /api/tasks/
```

### Comments

```text
GET  /api/comments/
POST /api/comments/
```

### Notifications

```text
GET /api/notifications/
```

### WebSocket Test

```text
GET /api/websocket-test/
```

WebSocket route:

```text
ws://127.0.0.1:8000/ws/tasks/
```

## 💬 Comments

Users can add comments to a specific task by entering the Task ID and comment content.

Example:

```json
{
    "task": 1,
    "content": "Working on the project dashboard."
}
```

## 📌 Task Management

Tasks contain information such as:

* Task title
* Description
* Project
* Assigned user
* Status
* Priority
* Due date
* Created date
* Updated date

### Task Status

```text
todo
progress
done
```

### Task Priority

```text
low
medium
high
```

## 🔔 Notifications

The application provides a notification section where users can view notifications related to project and task activities.

## 🔌 WebSocket

Django Channels is configured for WebSocket communication.

The WebSocket consumer is responsible for accepting connections and sending real-time messages.

WebSocket endpoint:

```text
/ws/tasks/
```

The project also contains a WebSocket test endpoint:

```text
/api/websocket-test/
```

## 🧪 Testing

The application can be tested by performing the following operations:

1. Login
2. Create a project
3. Create a task
4. View tasks
5. Add a comment
6. Refresh comments
7. View notifications
8. Test the WebSocket endpoint

## 🎯 Future Enhancements

* Real-time task updates
* Real-time notifications
* Task assignment interface
* Due-date reminders
* File attachments
* Advanced project dashboard
* Search and filtering
* Improved user profiles
* Deployment to cloud platforms

## 👩‍💻 Developer

**Anugu Rishika Reddy**

B.Tech – Computer Science & Engineering

## 📄 License

This project is developed for educational and learning purposes.
