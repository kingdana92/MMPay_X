import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# This receives the notification from the Payment Gateway
@app.route('/webhook', methods=['POST'])
def mmpay_webhook():
    try:
        data = request.get_json()
        
        # Log the data so you can see it in Railway logs
        print(f"💰 PAYMENT RECIEVED: {data}")

        # Basic Check
        if not data:
            return jsonify({"status": "error", "message": "No data"}), 400

        # TODO: Add your logic here (e.g., save to database)
        
        # Return success to the gateway
        return jsonify({"status": "received"}), 200

    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({"status": "error"}), 500

# Railway needs this to start the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)