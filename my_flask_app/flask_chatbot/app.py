from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    response = get_response(user_input)
    return jsonify({'response': response})

def get_response(message):
    # Simple response logic based on user input
    if 'name' in message.lower():
        return "What's your pet's name?"
    elif 'my pet is' in message.lower():
        pet_name = message.split('my pet is')[-1].strip()
        return f"Nice to meet your pet, {pet_name}!"
    return "I'm not sure what to say. Can you tell me more about your pet?"

if __name__ == '__main__':
    app.run(debug=True)