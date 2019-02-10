from flask import Flask, render_template, send_from_directory
import os
import random
import json

data_file = 'npc.json'
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 
            'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dnd/<kind>')
def dnd(kind):
    with open(os.path.join(app.root_path, data_file), 'r') as f:
        json_data = json.load(f)
        race = random.choice(json_data["Race"])
        gender = random.choice(json_data["Gender"])
        job = random.choice(json_data["Job"])
        alignment = random.choice(json_data["Alignment"])
        first_name = random.choice(json_data["FirstName"])
        last_name = random.choice(json_data["LastName"])
        tavern = random.choice(json_data["Tavern"])
        return render_template('dnd.html', race=race, gender=gender, job=job, first_name=first_name, last_name=last_name, alignment=alignment, tavern=tavern)

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/cakes')
def cakes():
    return 'Yummy <b>cakes</b>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

