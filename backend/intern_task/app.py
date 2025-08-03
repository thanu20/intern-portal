from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/user", methods=["GET"])
def get_user():
    return jsonify({
        "name": "Linganaboina Thanuja",
        "referral_code": "thanuja2025",
        "total_donations": 7000
    })

if __name__ == "__main__":
    print("✅ Flask server is starting...")
    app.run(debug=True)
