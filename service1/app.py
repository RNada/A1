from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
     team = requests.get('http://team_position_api:5000/get_team')
     position = requests.post('http://team_position_api:5000/get_position', data=team.text)
     return render_template('index.html', team=team.text, position=position.text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True) 