from flask import Flask, render_template, request, jsonify

# Importing necessary components from gpt-4-search.py
from gpt_4_search import run

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/ask', methods=['POST'])
def send_message():
    user_message = request.form.get('message')
    
    # Use gpt-4-search.py's run function to get the AI's response
    ai_response = run(user_message)
    
    return jsonify(response=ai_response)


if __name__ == '__main__':
    app.run(debug=True)
