# 🏙 CivicTrack

CivicTrack is a Flask-based app that allows users to report and track civic issues (like road damage, garbage, water leaks) within a 3–5 km radius of their location.

---

## 🚀 Features

- 🧭 Location-based visibility of issues (3-5 km)
- 📝 Report issues with title, description, category, location, and images
- 🔒 Support for anonymous or verified reports
- 🧑‍⚖️ Admin moderation: flag spam, update issue status
- 🔄 Track status (Reported → In Progress → Resolved)

---

## 🧱 Tech Stack

- Python + Flask
- SQLite + SQLAlchemy
- HTML/CSS for frontend
- REST APIs

---

## ⚙️ Setup Instructions

```bash
git clone <repo>
cd civictrack
pip install -r requirements.txt
mkdir uploads
python app.py
