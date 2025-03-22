# 🏆 Eventease - Event Management System

Eventease is a **Django-based web application** designed to simplify **event management**. Users can **create, edit, and manage events** while ensuring security and scalability using **AWS Elastic Beanstalk**.

## 🌟 Features
- ✅ **User Authentication** (Admin/User roles)
- ✅ **Event Creation, Editing & Management**
- ✅ **Image Upload for Events**
- ✅ **Secure Role-Based Access Control**
- ✅ **AWS Cloud Deployment (Elastic Beanstalk, S3, RDS)**
- ✅ **CI/CD Integration (GitHub Actions, AWS CodePipeline)**
- ✅ **Automated Testing & Static Code Analysis**

## 🛠️ Technology Stack
| Component        | Technology Used |
|-----------------|----------------|
| **Backend**     | Django (Python) |
| **Database**    | SQLite (Development), AWS RDS/DynamoDB (Production) |
| **Frontend**    | HTML, CSS, Bootstrap, JavaScript |
| **Cloud**       | AWS Elastic Beanstalk, S3, EC2, IAM, CloudWatch |
| **CI/CD**       | GitHub Actions, AWS CodePipeline |
| **Security**    | Pylint, SonarQube, Bandit (Code Analysis) |

---

## 🚀 Installation & Setup

### 🔹 1. Clone the Repository
```sh
git clone https://github.com/supreeth2003/Eventease.git
cd Eventease
```

### 🔹 2. Create a Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate   # For Windows
pip install -r requirements.txt
```

### 🔹 3. Run Migrations & Start Server
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Application will be available at **http://127.0.0.1:8000/**.

---

## ☁️ Cloud Deployment (AWS Elastic Beanstalk)

### 🔹 1. Install AWS Elastic Beanstalk CLI
```sh
pip install awsebcli --upgrade
```

### 🔹 2. Initialize Elastic Beanstalk
```sh
eb init -p python-3.12 Eventease --region us-east-1
```

### 🔹 3. Deploy Application
```sh
eb create eventease-env
```

Application will be available at **`http://eventease-env.eba-5qmmf4pp.us-west-2.elasticbeanstalk.com`**.

---

## ⚙️ CI/CD Pipeline (GitHub Actions + AWS CodePipeline)
### ✅ **Continuous Integration (CI)**
- Automated testing (`pytest`, `pylint`)
- Security scanning (`Bandit`, `SonarQube`)

### ✅ **Continuous Deployment (CD)**
- Automated AWS Elastic Beanstalk deployment via GitHub Actions

---

## 🔍 Testing & Security Analysis

### ✅ Run Pytest for Unit Testing
```sh
pytest
```

### ✅ Perform Static Code Analysis with Pylint
```sh
pylint events/
```

### ✅ Security Scan with Bandit
```sh
bandit -r events/
```

---

## 📈 Future Improvements
- 🔹 Implement API-based Event Booking
- 🔹 Add Real-time Notifications via WebSockets
- 🔹 Enhance AI-based Event Recommendations

---

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Submit a pull request!


---

