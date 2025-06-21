from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from welcome import get_ai_message
import os

app = Flask(__name__)
CORS(app)

# ------------------------------------------------------------------------------
#  Main page
# ------------------------------------------------------------------------------
@app.route("/")
def index():
    """
    Serves the landing page (index.html) from the root directory.
    """
    print("Serving index.html")
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

# ------------------------------------------------------------------------------
#  AJAX endpoint: /get-message
# ------------------------------------------------------------------------------
@app.route("/get-message", methods=['POST'])
def get_message():
    """
    Returns a JSON payload containing the message based on the user's experience level.
    """
    print("Received request to /get-message")
    try:
        data = request.get_json()
        print("Request data:", data)
        level = data.get('level', 'other')
        name = data.get('name', '')
        
        # Get the base message
        response = get_ai_message(level)
        
        # Personalize the title if we have a name
        if name:
            if name.lower() == "harry":
                response['title'] = f"🚀 Visionary AI Builder {name}!"
            else:
                response['title'] = response['title'].replace('!', f', {name}!')
            
        print("Sending response:", response)
        return jsonify(response)
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------------------------------
#  Entry point
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # debug=True enables hot reload while you iterate
    app.run(debug=True, host="0.0.0.0", port=5000)
