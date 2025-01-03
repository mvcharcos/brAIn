from flask import Flask, jsonify, request, render_template
from components.environment import Environment
from components.selfawareness import SelfAwareness
from components.reference import Reference
from components.memory import Memory
from components.prediction import Prediction
from components.curiosity import Curiosity

app = Flask(__name__)

# Initialize Components
env = Environment()
self_awareness = SelfAwareness()
reference = Reference()
memory = Memory()
prediction = Prediction(memory, self_awareness, env, reference)
curiosity = Curiosity()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/components', methods=['GET'])
def get_components():
    return jsonify({
        "environment": env.get_state(),
        "selfawareness": self_awareness.get_state(),
        "reference": reference.get_state(),
        "memory": memory.get_state(),
    })

@app.route('/add_memory', methods=['POST'])
def add_memory():
    data = request.json
    entry = data.get("entry", "")
    memory.add_entry(entry)
    return jsonify({"success": True, "entries": memory.entries})

@app.route('/environment', methods=['POST'])
def update_environment():
    data = request.json
    env.set_state(
        lamp1=data.get('lamp1', env.lamp1),
        lamp2=data.get('lamp2', env.lamp2),
        lux=data.get('lux', env.lux),
        consumption1=data.get('consumption1', env.consumption1),
        consumption2=data.get('consumption2', env.consumption2),
    )
    return jsonify(env.get_state())

@app.route('/predict', methods=['GET'])
def predict():
    result = prediction.generate_prompt()
    return jsonify(result)

@app.route('/curiosity', methods=['POST'])
def generate_curiosity_prompt():
    data = request.json
    actions = data.get("actions", "")
    result = curiosity.generate_prompt(actions)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
