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
**Glassmorphism UI** 
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

<img width="1920" height="1080" alt="Screenshot (478)" src="https://github.com/user-attachments/assets/b9770de0-f3e8-4d10-b9a1-8bd5d94d6602" />
<img width="1920" height="1080" alt="Screenshot (479)" src="https://github.com/user-attachments/assets/900708f9-ffe0-4d42-8fad-9e08f87837f0" />

---

## Home page

<img width="1920" height="1080" alt="Screenshot (480)" src="https://github.com/user-attachments/assets/b62f6f79-f81b-4258-8100-49d7c5ee7e2d" />



---

## Report Incident Page

<img width="1920" height="1080" alt="Screenshot (482)" src="https://github.com/user-attachments/assets/0ff273b7-d207-4451-9894-61e14e412e13" />
<img width="1920" height="1080" alt="Screenshot (483)" src="https://github.com/user-attachments/assets/287e2bdf-c2c5-4f4b-baeb-85941ea345d2" />

---

## Incident Dashboard

<img width="1920" height="1080" alt="Screenshot (484)" src="https://github.com/user-attachments/assets/d7f7a2b2-bf2f-46d8-be3c-13674ace90a2" />

---
## Cyber Awareness Page
<img width="1920" height="1080" alt="Screenshot (485)" src="https://github.com/user-attachments/assets/9e1300a7-c79a-4bcf-a99e-3c8b5a189b79" />
<img width="1920" height="1080" alt="Screenshot (486)" src="https://github.com/user-attachments/assets/36ae30ed-28c4-46dd-a708-8b081a2fd32a" />

---

## Cybersecurity Chatbot

<img width="1920" height="1080" alt="Screenshot (481)" src="https://github.com/user-attachments/assets/b990099d-333d-4c03-90c1-cd4b72cff494" />


---

## Admin Dashboard

<img width="1920" height="1080" alt="Screenshot (487)" src="https://github.com/user-attachments/assets/cd8527be-cd78-438a-9959-1198ce2837da" />
<img width="1920" height="1080" alt="Screenshot (488)" src="https://github.com/user-attachments/assets/4f634336-39ea-4ed5-b151-453dc8765906" />


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



