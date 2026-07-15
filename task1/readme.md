# 🗳️ Real-Time Online Voting System

A **Real-Time Online Voting System** built using **Node.js, SQLite, HTML, CSS, and JavaScript**. The application allows users to create polls, participate in voting, and view live voting updates. Multiple users can vote on the same poll, and the final results are declared only after the poll expires, ensuring fairness during the voting period.

---

## 📌 Features

- Create polls with multiple voting options.
- Multiple users can vote on the same poll.
- Each user can vote only once per poll.
- Real-time vote updates using WebSockets.
- Polls have an expiry time.
- Results are declared only after the voting period ends.
- Data is permanently stored using SQLite.
- Simple and responsive user interface.
- REST API-based backend architecture.

---

## 🚀 Technologies Used

### Backend
- Node.js
- HTTP Module
- SQLite
- WebSocket
- Crypto Module

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- SQLite

---

## 📂 Project Structure

```
Voting-System/
│
├── server.js             # Main backend server
├── database.js           # Database operations
├── polls.db              # SQLite database
├── package.json          # Project dependencies
├── package-lock.json
│
├── public/
│   ├── index.html        # Main webpage
│   ├── style.css         # Styling
│   └── client.js         # Frontend logic
│
└── README.md
```

---

## ⚙️ How It Works

1. A user creates a poll by entering:
   - Poll question
   - Voting options
   - Poll expiry date and time

2. The poll is stored in the SQLite database.

3. Multiple users can access the same poll and cast their votes.

4. Each user is allowed to vote only once for a particular poll.

5. During the voting period:
   - Votes are recorded securely.
   - Live vote count is updated for connected users using WebSockets.
   - Final results remain hidden until the poll expires.

6. Once the poll reaches its expiry time:
   - Voting is automatically closed.
   - The final results are displayed to all users.

---

## 🔄 Workflow

```
User
   │
   ▼
Frontend (HTML/CSS/JS)
   │
   ▼
REST API (server.js)
   │
   ▼
Database (SQLite)
   │
   ▼
Store Poll / Store Vote
   │
   ▼
WebSocket Broadcast
   │
   ▼
Connected Users
```

---

## 📡 REST API Endpoints

| Method | Endpoint | Description |
|----------|--------------------------|--------------------------------|
| GET | `/api/polls` | Retrieve all polls |
| GET | `/api/polls/:id` | Retrieve a specific poll |
| POST | `/api/polls` | Create a new poll |
| POST | `/api/polls/:id/vote` | Cast a vote |
| GET | `/api/polls/:id/results` | View poll results (available after poll expiry) |

---

## 💾 Database Schema

### Polls
- Poll ID
- Question
- Created Date
- Expiry Date

### Options
- Option ID
- Poll ID
- Option Text
- Vote Count

### Votes
- Vote ID
- Poll ID
- Option ID
- Voter Identity

---

## 🔐 Security Features

- One vote per user per poll.
- Duplicate voting prevention.
- Server-side validation of all requests.
- Unique Poll IDs generated using the Crypto module.
- Secure handling of voting data.
- Results remain hidden until the poll expires.

---

## 📊 Real-Time Updates

The application uses **WebSockets** to provide instant updates.

Whenever a vote is cast:

- The database is updated.
- Connected clients receive live vote count updates.
- Users do not need to refresh the page.

---

## 📋 Prerequisites

Install:

- Node.js (v18 or later)
- npm (Node Package Manager)

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/voting-system.git
```

Navigate to the project folder:

```bash
cd voting-system
```

Install dependencies:

```bash
npm install
```

Start the server:

```bash
npm start
```

Open your browser:

```
http://localhost:3000
```

---

## 🎯 Future Enhancements

- User authentication and login.
- Admin dashboard for poll management.
- Anonymous voting option.
- Email notifications for poll results.
- Graphical result visualization.
- Export poll results as PDF or Excel.
- Mobile-responsive improvements.
- Role-based access control.

---

## 👨‍💻 Authors

Developed as a Project-Based Learning (PBL) project demonstrating:

- Backend Web Development
- REST APIs
- SQLite Database Management
- Real-Time Communication using WebSockets
- HTTP Server Development
- Client–Server Architecture

---

## 📜 License

This project is developed for educational and academic purposes. You are free to use, modify, and extend it for learning and non-commercial use.

---

## ⭐ Acknowledgements

Special thanks to the open-source community and the Node.js ecosystem for providing the libraries and tools used in this project.
