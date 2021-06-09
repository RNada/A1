from flask import Flask
import random
app = Flask(__name__)

@app.route('/get_team', methods=['GET'])
def get_team():
    return random.choice(['Manchester Red', 'North London White', 'Manchester Blue'])

@app.route('/get_position', method=['POST'])
def get_position():
    return random.choice(['Center Back', 'Center Midfield', 'Striker'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True) 