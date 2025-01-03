from flask import Flask, jsonify, request, render_template
import random
from environment import Environment
app = Flask(__name__)


# Initialize Components
env = Environment()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/environment', methods=['GET', 'POST'])
def environment():
    if request.method == 'POST':
        data = request.json
        env.set_state(
            lamp1=data.get('lamp1'),
            lamp2=data.get('lamp2'),
            lux=data.get('lux'),
            consumption1=data.get('consumption1'),
            consumption2=data.get('consumption2'),
        )
    return jsonify(env.get_state())

# Add similar endpoints for selfawareness, reference, memory, prediction, curiosity

if __name__ == '__main__':
    app.run(debug=True)
