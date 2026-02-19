import os
from flask import Flask, request, jsonify, render_template

# Tell Flask to look in the 'templates' folder for your HTML
app = Flask(__name__, template_folder='templates')

# --- 1. THE FRONTEND (What users see) ---
@app.route('/', methods=['GET'])
def home():
    # This serves your index.html when you visit your Railway link
    return render_template('index.html')

# --- 2. THE BACKEND (What MMPay talks to) ---
@app.route('/webhook', methods=['POST'])
def mmpay_webhook():
    try:
        data = request.get_json()
        print(f"💰 PAYMENT RECEIVED: {data}")

        if not data:
            return jsonify({"status": "error", "message": "No data"}), 400

        # TODO: Database logic goes here later
        
        return jsonify({"status": "received"}), 200

    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)