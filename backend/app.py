from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/user")
def user_info():
    return jsonify({
        "name": "Linganaboina Thanuja",
        "referral_code": "thanuja2025",
        "total_donations": 7000
    })

if __name__ == "__main__":
    app.run(debug=True)
