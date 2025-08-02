<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>CivicTrack README</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #f9f9fb;
      margin: 0;
      padding: 30px;
      color: #333;
    }
    h1 {
      color: #2c3e50;
      font-size: 2.5rem;
      margin-bottom: 10px;
    }
    h2 {
      color: #2980b9;
      margin-top: 40px;
    }
    p {
      line-height: 1.6;
    }
    code, pre {
      background: #f4f4f4;
      border-radius: 5px;
      padding: 2px 6px;
      font-family: Consolas, monospace;
    }
    pre {
      padding: 15px;
      overflow-x: auto;
    }
    ul {
      margin-top: 0;
      padding-left: 20px;
    }
    .badge {
      background: #3498db;
      color: white;
      padding: 2px 8px;
      font-size: 0.8rem;
      border-radius: 4px;
      margin-left: 5px;
    }
    .folder {
      font-family: monospace;
      font-size: 0.95rem;
      background: #ecf0f1;
      padding: 10px;
      border-radius: 5px;
    }
  </style>
</head>
<body>

  <h1>🏙️ CivicTrack</h1>
  <p><strong>CivicTrack</strong> is a Python-based web app that empowers users to report and track civic issues like potholes, garbage dumps, or water leaks — all within a 3–5 km radius.</p>

  <h2>🚀 Features</h2>
  <ul>
    <li>📍 GPS-based local issue visibility</li>
    <li>📝 Submit issues with title, description, location, category, and up to 35 images</li>
    <li>🔒 Support for both anonymous and verified reports</li>
    <li>🔄 Transparent status tracking (Reported → In Progress → Resolved)</li>
    <li>🗃️ Admin panel with flagging and banning support</li>
  </ul>

  <h2>⚙️ Tech Stack</h2>
  <ul>
    <li><strong>Backend:</strong> Python + Flask</li>
    <li><strong>Database:</strong> SQLite + SQLAlchemy</li>
    <li><strong>Frontend:</strong> HTML + CSS</li>
    <li><strong>API:</strong> REST</li>
  </ul>

  <h2>📁 Folder Structure</h2>
  <div class="folder">
    civictrack/<br>
    ├── app.py<br>
    ├── requirements.txt<br>
    ├── README.md<br>
    ├── uploads/<br>
    ├── templates/<br>
    │   └── index.html<br>
    └── static/<br>
    &nbsp;&nbsp;&nbsp;&nbsp;└── styles.css<br>
  </div>

  <h2>📦 Installation</h2>
  <pre><code>git clone https://github.com/yourname/civictrack.git
cd civictrack
pip install -r requirements.txt
mkdir uploads
python app.py
</code></pre>

  <h2>🌐 Open in Browser</h2>
  <p>Go to <code>http://localhost:5000</code></p>

  <h2>🔐 Security Practices</h2>
  <ul>
    <li>Sanitized file uploads using <code>secure_filename()</code></li>
    <li>SQL injection protection via SQLAlchemy</li>
    <li>Limited image uploads to 35 per report</li>
    <li>Future-ready for authentication, CSRF protection, and HTTPS headers</li>
  </ul>

  <h2>🧑‍💻 Contributing</h2>
  <p>Fork this project and submit PRs to enhance features like map filtering, real admin dashboard, or Leaflet/OpenStreetMap integration.</p>

  <h2>📜 License</h2>
  <p>MIT License — use freely and help make your community better.</p>

</body>
</html>
