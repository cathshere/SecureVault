# SecureVault

SecureVault is a cybersecurity-focused web application that combines secure file storage with integrated threat detection. The system enables users to securely store sensitive files using encryption while identifying phishing emails and malicious URLs through built-in security modules.

The project aims to improve data confidentiality, integrity, and user awareness by bringing secure file management and threat analysis into a single platform.

---

## Features

### Secure File Vault
- User registration and authentication
- Secure file upload and download
- AES (Fernet)-based file encryption and decryption
- User-specific encrypted storage
- Activity logging

### PhishGuard
- Email phishing analysis
- Risk score generation
- Detection of phishing indicators and suspicious keywords
- Threat classification (Low, Medium, High)

### URL Scanner
- URL reputation analysis
- VirusTotal integration
- Domain and IP information
- Detection of malicious and suspicious URLs

---

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite
- SQLAlchemy

### Security
- Cryptography (Fernet / AES Encryption)
- VirusTotal API

---

## Project Structure

```text
SecureVault/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── files.html
│   ├── logs.html
│   ├── phishguard.html
│   ├── urlscanner.html
│   ├── reports.html
│   ├── settings.html
│   └── auditlog.html
│
├── uploads/
├── reports/
│   └── report_history.json
│
├── app.py
├── email_analyzer.py
├── requirements.txt
├── secret.key
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/SecureVault.git
cd SecureVault
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## Modules

### SecureVault
Encrypts uploaded files before storing them and decrypts them only during authorized downloads, ensuring secure file management and data confidentiality.

### PhishGuard
Analyzes email content to detect phishing characteristics, generates a risk score, and highlights suspicious indicators to help users identify potential phishing attacks.

### URL Scanner
Checks URLs using the VirusTotal API and displays security information such as reputation, domain details, IP address, and malicious detection results.

---

## Future Enhancements

- Multi-factor authentication (MFA)
- Malware scanning for uploaded files
- AI-based phishing detection
- Real-time threat monitoring
- Cloud storage integration
- Role-based access control





## Team

* **Member 1:** User Authentication, Database, Dashboard
* **Member 2:** Secure File Vault, File Encryption & Management
* **Member 3:** PhishGuard, URL Scanner, UI Design, Testing & Documentation

---

## License

This project was developed for academic and educational purposes.

# SecureVault – Secure File Storage and Phishing Detection System

##  Project Overview

SecureVault is a web-based cybersecurity application developed using **Python Flask**. It provides users with a secure platform to upload, encrypt, store, manage, and download files while also offering phishing detection capabilities. The system ensures confidentiality of sensitive files through encryption and enhances cybersecurity awareness by identifying suspicious phishing URLs.

This project was developed as a team project by three members, with each member contributing to different modules.

---

#  Objectives

- Securely upload and store confidential files.
- Encrypt files before storage.
- Allow only authenticated users to access their files.
- Detect phishing URLs to improve cybersecurity.
- Maintain user activity logs.
- Provide a simple and user-friendly dashboard.

---

#  Features

##  User Authentication

- User Registration
- Secure Login
- Logout
- Session Management
- SQLite Database Integration

---

##  Secure File Vault

- Upload Files
- Automatic File Encryption
- Secure File Storage
- User-wise File Separation
- Download and Decrypt Files
- Delete Files
- Dashboard Statistics

---

##  Activity Logs

The system maintains logs for:

- File Upload
- File Download
- File Deletion
- User Actions

Each log contains:

- Username
- Filename
- Action Performed
- Timestamp

---

##  Phishing Detection Module

The application includes a phishing detection system that allows users to verify whether a URL is legitimate or suspicious.

### Features

- URL Analysis
- Phishing Website Detection
- Safe/Unsafe Prediction
- User-Friendly Interface

---

##  Modern User Interface

The project uses Bootstrap for creating a responsive and attractive interface.

Pages include:

- Login
- Register
- Dashboard
- Upload Files
- Stored Files
- Activity Logs
- Phishing Detection

---

# 🛠 Technologies Used

### Backend

- Python
- Flask
- Flask-SQLAlchemy

### Database

- SQLite

### Encryption

- Cryptography (Fernet AES Encryption)

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Jinja2 Templates

### Version Control

- Git
- GitHub

---

#  Project Structure

```
SecureVault/
│
├── app.py
├── requirements.txt
├── secret.key
├── generate_key.py
│
├── uploads/
│
├── instance/
│     └── users.db
│
├── static/
│     ├── style.css
│     └── images/
│
├── templates/
│     ├── login.html
│     ├── register.html
│     ├── index.html
│     ├── files.html
│     ├── logs.html
│     └── phishing.html
│
└── README.md
```

---

#  Security Features

- AES File Encryption using Fernet
- User Authentication
- Session Management
- User-wise File Isolation
- Secure File Downloads
- Protected Routes
- Activity Monitoring

---

#  Project Workflow

1. User registers an account.
2. User logs into the system.
3. Dashboard displays file statistics.
4. User uploads a file.
5. File is encrypted before storage.
6. User can:
   - View files
   - Download files
   - Delete files
7. Every action is logged.
8. User can analyze URLs using the phishing detection module.
9. User logs out securely.

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Avantika23-git/SecureVault.git
```

---

## Navigate to Project

```bash
cd SecureVault
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Generate Encryption Key

```bash
python generate_key.py
```

---

## Run Application

```bash
python app.py
```

---

## Open Browser

```
http://127.0.0.1:5000
```

---

#  Modules

## Module 1

### Authentication

- Register
- Login
- Logout

### Database

- SQLite Integration
- User Management

### Dashboard

- User Dashboard
- Statistics

---

## Module 2

### Secure Vault

- Upload Files
- Encrypt Files
- Download Files
- Delete Files
- Activity Logs

---

## Module 3

### Phishing Detection

- URL Verification
- Phishing Prediction
- Result Display
- Security Recommendations

---

#  Team Contributions

## Member 1

- User Authentication
- SQLite Database
- Dashboard Development
- User-wise File Management
- Activity Logs
- UI Styling
- GitHub Integration

---

## Member 2

- File Upload Module
- File Encryption
- File Download
- Secure Storage
- Delete Functionality

---

## Member 3

- Phishing Detection Module
- URL Analysis
- Prediction Logic
- Frontend Integration
- Testing

---

#  Future Enhancements

- Two-Factor Authentication
- Cloud Storage Integration
- Email Verification
- OTP Login
- AI-based Threat Detection
- Malware Scanning
- Admin Dashboard
- Password Reset
- File Sharing with Permissions
- Audit Reports

---

#  Expected Output

- Secure user authentication
- Encrypted file storage
- User-specific file access
- Phishing URL detection
- Responsive dashboard
- Activity monitoring
- Enhanced cybersecurity awareness

---

#  Conclusion

SecureVault is a secure and user-friendly web application that combines encrypted file storage with phishing detection. The project demonstrates the practical implementation of cybersecurity concepts such as encryption, authentication, access control, activity logging, and phishing awareness using Python Flask. It provides a strong foundation for secure digital file management and can be extended with advanced security features in future versions.

