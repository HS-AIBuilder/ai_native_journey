from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from welcome import get_ai_message
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configure CORS for production
CORS(app, resources={
    r"/get-message": {"origins": os.getenv('ALLOWED_ORIGINS', '*').split(',')},
    r"/": {"origins": os.getenv('ALLOWED_ORIGINS', '*').split(',')}
})

# Security headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

# ------------------------------------------------------------------------------
#  Main page
# ------------------------------------------------------------------------------
@app.route("/")
def index():
    """
    Serves the landing page (index.html) from the root directory.
    """
    logger.info("Serving index.html")
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

# ------------------------------------------------------------------------------
#  AJAX endpoint: /get-message
# ------------------------------------------------------------------------------
@app.route("/get-message", methods=['POST'])
def get_message():
    """
    Returns a JSON payload containing the message based on the user's experience level.
    """
    logger.info("Received request to /get-message")
    try:
        data = request.get_json()
        logger.debug("Request data: %s", data)
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
            
        logger.info("Sending response for level: %s", level)
        logger.debug("Response data: %s", response)
        return jsonify(response)
    except Exception as e:
        logger.error("Error processing request: %s", str(e), exc_info=True)
        return jsonify({"error": "An internal error occurred"}), 500

# ------------------------------------------------------------------------------
#  Entry point
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Use environment variables for configuration
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    app.run(debug=debug, host=host, port=port)
