# 🛡 Cyber Incident Reporting and Awareness Platform

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![HTML](https://img.shields.io/badge/Frontend-HTML5-orange?logo=html5)
![CSS](https://img.shields.io/badge/Style-CSS3-blue?logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript)
![Chart.js](https://img.shields.io/badge/Charts-Chart.js-ff6384?logo=chartdotjs)
![License](https://img.shields.io/badge/License-Educational-green)

A web-based cybersecurity platform that allows users to **report cyber incidents, track threats, and improve cybersecurity awareness**.  
The system provides an **admin dashboard with analytics and monitoring tools** to help manage reported incidents effectively.

This project was built using **Python Flask, SQLite, HTML, CSS, JavaScript, and Chart.js**.

---

#  Project Overview

Cyber attacks such as phishing, malware, and ransomware are increasing rapidly. Many users do not know how to report incidents or understand cyber threats.

This platform provides:

- A **centralized system to report cyber incidents**
- **Admin monitoring dashboard**
- **Incident analytics and visualization**
- **Cybersecurity awareness resources**
- **Cybersecurity chatbot assistance**

---

#  Features

##  User Features

- User Registration and Login
- Report Cyber Incidents
- View Reported Incidents
- Search Incidents
- Cybersecurity Awareness Page
- Cybersecurity Chatbot

---

##  Admin Features

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

#  Dashboard Analytics

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

#  Cybersecurity Chatbot

The platform includes a **basic chatbot assistant** that answers cybersecurity questions.

Example questions:

- What is phishing?
- What is malware?
- What is ransomware?
- How to protect passwords?
- What should I do if my account is hacked?

The chatbot provides **simple awareness guidance for common cyber threats**.

---

#  Database Structure

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

#  Technologies Used

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

#  Screenshots

##  Login and Register page

<img width="1920" height="1080" alt="Screenshot (460)" src="https://github.com/user-attachments/assets/aa29a6e6-f429-4c77-bd27-8d98af7f77c3" />
<img width="1920" height="1080" alt="Screenshot (461)" src="https://github.com/user-attachments/assets/fa3d440c-2277-43f3-857c-572f10678254" />


---

## Home page

<img width="1920" height="1080" alt="Screenshot (462)" src="https://github.com/user-attachments/assets/64359690-3478-42da-89fb-9722ab60219b" />
<img width="1920" height="1080" alt="Screenshot (463)" src="https://github.com/user-attachments/assets/cda45fa5-6ce6-4b05-b7b2-4a03f6f34ca8" />


---

## Report Incident Page

<img width="1920" height="1080" alt="Screenshot (464)" src="https://github.com/user-attachments/assets/2255d8e1-8a24-4627-b70c-ba0a2fe3702c" />
<img width="1920" height="1080" alt="Screenshot (465)" src="https://github.com/user-attachments/assets/a55fc05e-5bab-4af1-b93c-427777bb2b55" />

---

## Incident Dashboard

<img width="1920" height="1080" alt="Screenshot (466)" src="https://github.com/user-attachments/assets/3bdeaa78-cffd-49e7-8611-cf09446aa572" />

---
## Cyber Awareness Page
<img width="1920" height="1080" alt="Screenshot (467)" src="https://github.com/user-attachments/assets/f5cbeaaf-c418-421c-87ef-46a59c83dbf4" />
<img width="1920" height="1080" alt="Screenshot (468)" src="https://github.com/user-attachments/assets/3c18e27a-e1b1-46a7-8820-c2e63f90beb7" />

---

## Cybersecurity Chatbot

<img width="1920" height="1080" alt="Screenshot (469)" src="https://github.com/user-attachments/assets/14db8b11-1c25-4be0-93c9-448abbc0ed11" />


---

## Admin Dashboard

<img width="1920" height="1080" alt="Screenshot (470)" src="https://github.com/user-attachments/assets/109d8650-2c9f-41fd-9d2e-59e3e72de685" />
<img width="1920" height="1080" alt="Screenshot (471)" src="https://github.com/user-attachments/assets/8639f611-4fa0-42e1-90ea-14e716450434" />


---

#  Installation 

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

#  Default Admin Login

Email:

```
admin@gmail.com
```

Password:

```
admin123
```

---



