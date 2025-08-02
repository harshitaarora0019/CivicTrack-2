from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///civictrack.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    is_verified = db.Column(db.Boolean, default=False)

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    category = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='Reported')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    is_anonymous = db.Column(db.Boolean, default=False)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'))

class StatusLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'))
    old_status = db.Column(db.String(50))
    new_status = db.Column(db.String(50))
    changed_at = db.Column(db.DateTime, default=datetime.utcnow)

class Flag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    data = request.form
    images = request.files.getlist('images')
    user_id = data.get('user_id')
    is_anon = data.get('is_anonymous') == 'true'

    issue = Issue(
        title=data['title'],
        description=data['description'],
        category=data['category'],
        latitude=float(data['latitude']),
        longitude=float(data['longitude']),
        user_id=user_id if not is_anon else None,
        is_anonymous=is_anon
    )
    db.session.add(issue)
    db.session.commit()

    for img in images[:35]:
        filename = secure_filename(img.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img.save(path)
        db.session.add(Image(filename=filename, issue_id=issue.id))

    db.session.commit()
    return jsonify({'message': 'Issue reported successfully', 'issue_id': issue.id})

@app.route('/issues', methods=['GET'])
def get_issues():
    radius = float(request.args.get('radius', 3))
    lat = float(request.args['lat'])
    lon = float(request.args['lon'])
    # Placeholder: Use haversine or spatial query in real app
    issues = Issue.query.filter(Issue.latitude.between(lat-0.05, lat+0.05), Issue.longitude.between(lon-0.05, lon+0.05)).all()
    result = []
    for i in issues:
        result.append({
            'id': i.id,
            'title': i.title,
            'category': i.category,
            'status': i.status,
            'latitude': i.latitude,
            'longitude': i.longitude
        })
    return jsonify(result)

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.json
    issue = Issue.query.get(data['issue_id'])
    log = StatusLog(issue_id=issue.id, old_status=issue.status, new_status=data['new_status'])
    issue.status = data['new_status']
    db.session.add(log)
    db.session.commit()
    return jsonify({'message': 'Status updated'})

if __name__ == '__main__':
    if not os.path.exists('civictrack.db'):
        db.create_all()
    app.run(debug=True)
