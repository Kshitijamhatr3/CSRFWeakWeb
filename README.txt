# CSRFWeakWeb

⚠️ **Intentionally Vulnerable Application – For Educational Use Only**

CSRFWeakWeb is a deliberately insecure web application designed to help beginners and security enthusiasts understand **Cross-Site Request Forgery (CSRF)** vulnerabilities through hands-on practice.

This project is built purely for **learning, demonstration, and lab purposes**.

---

## 📢 Disclaimer

This application is **intentionally vulnerable**.

* ❌ Do NOT deploy this on the internet
* ❌ Do NOT use this in production
* ❌ Do NOT test against systems you do not own or have permission to test

The author is **not responsible** for any misuse.

---

## 🎯 Purpose of This Project

The goal of CSRFWeakWeb is to help learners:

* Understand what CSRF is
* See how missing CSRF protections lead to real attacks
* Learn how attackers exploit CSRF
* Practice identifying and exploiting CSRF vulnerabilities safely
* Understand the real-world impact of CSRF

This project assumes **basic web knowledge** and is beginner-friendly.

---

## 📝 What is CSRF?

Cross-Site Request Forgery (CSRF) is a vulnerability where:

> A web application performs sensitive actions based solely on a user’s authenticated session, **without verifying the intent of the user**.

An attacker can trick a logged-in victim into performing unwanted actions without their knowledge.

---

## Vulnerabilities Demonstrated

CSRFWeakWeb intentionally includes:

* ❌ No CSRF tokens
* ❌ No SameSite cookie protection
* ❌ No origin or referer validation
* ❌ Sensitive state-changing actions via POST/GET

These weaknesses allow:

* Unauthorized actions
* Account manipulation
* Privilege abuse

---

## 🧪 Example Attack Scenarios

* Changing account details via a malicious external website
* Performing authenticated actions without user consent
* Exploiting trust in session cookies

---

## 🛠️ Technology Stack

* Backend: *(Specify framework if applicable)*
* Frontend: Basic HTML forms
* Authentication: Session-based (intentionally weak)

---

## 📂 Project Structure

```
CSRFWeakWeb/
├── app/
├── templates/
├── static/
├── README.md
└── requirements.txt
```

*(Structure may vary depending on implementation)*

---

## 🧪 How to Use (Local Setup)

1. Clone the repository
2. Install dependencies
3. Run the application locally
4. Log in as a test user
5. Perform CSRF attacks from a separate HTML page

> ⚠️ Run only in a local or lab environment

---

## 🔐 How This Should Be Fixed (Learning Outcome)

After exploiting CSRFWeakWeb, learners should understand how to properly defend against CSRF:

* ✅ CSRF tokens
* ✅ SameSite cookies
* ✅ Proper HTTP methods
* ✅ Origin/Referer validation
* ✅ User re-authentication for sensitive actions

---

## 📚 Who This Project Is For

* Beginners learning web security
* Pentesting students
* Bug bounty beginners
* Security trainers
* Cybersecurity content creators

---

## 🧩 Related Topics to Explore

* Cross-Site Scripting (XSS)
* Authentication flaws
* Session management
* Web security headers
* OWASP Top 10

---

## ⭐ Contribution

This is a learning-focused project.

Feel free to:

* Improve documentation
* Add lab scenarios
* Add secure versions for comparison

---

## 🌻 Author

Created as part of a hands-on cybersecurity learning journey.

---

## ⚖️ License

By - Sukshield.com

This project is released for **educational use only**.

Do not use this code in real-world systems.
