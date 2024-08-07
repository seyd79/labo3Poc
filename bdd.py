from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'alarme.db')
db = SQLAlchemy(app)

class Alarme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    systemStatus = db.Column(db.Integer, default=0)

class Button(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    state = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/activer', methods=['POST'])
def activer():
    alarme = Alarme.query.first()
    if alarme.systemStatus == 0:
        alarme.systemStatus = 1
        db.session.commit()
    return jsonify({"status": alarme.systemStatus})

@app.route('/activerdesactiver', methods=['POST'])
def activerdesactiver():
    alarme = Alarme.query.first()
    if alarme.systemStatus == 0:
        alarme.systemStatus = 1
    elif alarme.systemStatus == 1:
        alarme.systemStatus = 0
    db.session.commit()
    return jsonify({"status": alarme.systemStatus})

@app.route('/reinitialiser', methods=['POST'])
def reinitialiser():
    alarme = Alarme.query.first()
    if alarme.systemStatus == 1:
        alarme.systemStatus = 1
        # Réinitialisation des autres composants
    db.session.commit()
    return jsonify({"status": alarme.systemStatus})

@app.route('/btnclick', methods=['POST'])
def btnclick():
    alarme = Alarme.query.first()
    button_id = request.json.get('button_id')
    button = Button.query.get(button_id)
    if alarme.systemStatus == 1 and button:
        button.state = not button.state
        db.session.commit()
    return jsonify({"button": button.name if button else "Button not found", "state": button.state})

@app.route('/desactiver', methods=['POST'])
def desactiver():
    alarme = Alarme.query.first()
    if alarme.systemStatus == 1:
        alarme.systemStatus = 0
        db.session.commit()
    return jsonify({"status": alarme.systemStatus})

if __name__ == '__main__':
    app.run(debug=True)
