# 🛡 Cyber Incident Reporting and Awareness Platform

A web-based cybersecurity platform that allows users to **report cyber incidents, track threats, and improve cybersecurity awareness**.  
The system provides an **admin dashboard with analytics and monitoring tools** to help manage reported incidents effectively.

This project was built using **Python Flask, SQLite, HTML, CSS, JavaScript, and Chart.js**.

---

# 📌 Project Overview

Cyber attacks such as phishing, malware, and ransomware are increasing rapidly. Many users do not know how to report incidents or understand cyber threats.

This platform provides:

- A **centralized system to report cyber incidents**
- **Admin monitoring dashboard**
- **Incident analytics and visualization**
- **Cybersecurity awareness resources**
- **Cybersecurity chatbot assistance**

---

# ✨ Features

## 👤 User Features

- User Registration and Login
- Report Cyber Incidents
- View Reported Incidents
- Search Incidents
- Cybersecurity Awareness Page
- Cybersecurity Chatbot

---

## 🛡 Admin Features

- Secure Admin Login
- View All Reported Incidents
- Search Incidents
- Update Incident Status
- Monitor Security Analytics

Admin dashboard includes:

- Incident Severity Chart
- Incident Status Chart
- Attack Type Chart
- Total Incident Statistics

---

# 📊 Dashboard Analytics

The admin dashboard displays visual security insights using **charts**.

### Incident Severity
Shows distribution of:
- Low
- Medium
- High
- Critical incidents

### Incident Status
Shows incident progress:
- Open
- Investigating
- Resolved

### Attack Types
Shows reported attack categories such as:
- Phishing
- Malware
- Ransomware
- Data Breach
- Unauthorized Access

Charts are implemented using **Chart.js**.

---

# 🤖 Cybersecurity Chatbot

The platform includes a **basic chatbot assistant** that answers cybersecurity questions.

Example questions:

- What is phishing?
- What is malware?
- What is ransomware?
- How to protect passwords?
- What should I do if my account is hacked?

The chatbot provides **simple awareness guidance for common cyber threats**.

---

# 🗄 Database Structure

The system uses **SQLite database**.

## Users Table

| Column | Description |
|------|-------------|
| id | User ID |
| name | User name |
| email | User email |
| password | User password |
| role | user / admin |

---

## Incidents Table

| Column | Description |
|------|-------------|
| id | Incident ID |
| incident_type | Type of attack |
| title | Incident title |
| incident_date | Date of incident |
| severity | Low / Medium / High / Critical |
| affected_system | Affected device/system |
| reporter | Person reporting |
| description | Incident details |
| status | Open / Investigating / Resolved |

---

# 🛠 Technologies Used

Backend:
- Python
- Flask

Frontend:
- HTML
- CSS
- JavaScript

Database:
- SQLite

Charts:
- Chart.js

---

# 📂 Project Structure

```
Cyber-Incident-Reporting-Platform
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── admin_dashboard.html
│   ├── report.html
│   └── awareness.html
│
├── static
│   ├── css
│   ├── js
│   └── images
│
└── screenshots
```

---

# 📷 Screenshots

You can add screenshots in the **screenshots folder**.

Example structure:

```
screenshots
│
├── login.png
├── user_dashboard.png
├── report_incident.png
├── admin_dashboard.png
├── chatbot.png
```

---

## Login Page

![Login Page](screenshots/login.png)

---

## User Dashboard

![User Dashboard](screenshots/user_dashboard.png)

---

## Report Incident Page

![Report Incident](screenshots/report_incident.png)

---

## Admin Dashboard

![Admin Dashboard](screenshots/admin_dashboard.png)

---

## Cybersecurity Chatbot

![Chatbot](screenshots/chatbot.png)

---

# 🚀 Installation Guide

Clone the repository:

```bash
git clone https://github.com/yourusername/A-Cyber-Incident-Reporting-and-Awareness-Platform.git
```

Go to project directory:

```bash
cd A-Cyber-Incident-Reporting-and-Awareness-Platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000
```

---

# 🔑 Default Admin Login

Email:

```
admin@gmail.com
```

Password:

```
admin123
```

---

# 🔮 Future Improvements

Possible future enhancements:

- Email alerts for critical incidents
- File evidence upload
- AI-based phishing detection
- Real-time threat monitoring
- Incident timeline tracking

---

# 👨‍💻 Author

Blessy Christrus

Cybersecurity Student Project

---

# 📄 License

This project is developed for **educational and academic purposes**.
