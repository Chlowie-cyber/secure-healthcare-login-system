# 🔐 Secure Healthcare Staff Login System

## 📌 Overview
This project is a cybersecurity-focused login system designed to simulate how healthcare organizations can protect sensitive systems from unauthorized access.

Healthcare institutions are prime targets for cyberattacks due to the high value of medical data. This system demonstrates secure authentication practices such as password hashing, role-based access control, login attempt tracking, and account lockout to help mitigate common attack methods like brute-force attacks.

---

## 🚨 Security Problem
Weak authentication systems can allow attackers to:

- Access confidential patient records  
- Launch ransomware attacks  
- Sell medical data on the black market  
- Disrupt critical healthcare services  

This project was built to demonstrate practical security controls that reduce these risks.

---

## 🔒 Security Features

✅ **Password Hashing**  
Passwords are encrypted using SHA-256 and are never stored in plain text.

✅ **Role-Based Access Control**  
Supports multiple healthcare roles:
- Admin  
- Doctor  
- Nurse  

This follows the Principle of Least Privilege.

✅ **Account Lockout Protection**  
Accounts are locked after three failed login attempts to prevent brute-force attacks.

✅ **Persistent Attempt Tracking**  
Failed login attempts are stored, preventing attackers from bypassing lockouts by restarting the system.

✅ **Audit Logging**  
All login attempts are recorded with timestamps to support monitoring and investigations.

---

## 🛠 Technologies Used
- Python  
- Hashlib  
- CSV (simulated database)  
- File-based logging  

---

## ▶️ How to Run

1. Clone the repository  
2. Navigate to the project folder  
3. Run: python login_system.py


Use the sample credentials stored in `users.csv`.

---

## 🧠 Cybersecurity Concepts Demonstrated
- Secure authentication  
- Brute-force attack prevention  
- Access control  
- Security logging  
- Defense-in-depth  

---

## 🚀 Future Improvements
- Multi-factor authentication (MFA)  
- Database integration (MySQL/PostgreSQL)  
- Password complexity rules  
- Data encryption  
- Web-based authentication system  

---

## 👨‍💻 Author
**Lehlogonolo Mpye**  
Aspiring Cybersecurity Professional passionate about protecting sensitive systems and critical infrastructure.
