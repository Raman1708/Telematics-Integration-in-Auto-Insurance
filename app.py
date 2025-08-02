# Backend API for Telematics Dashboard
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

# Load trained model from file (assume you save it earlier)
# model = joblib.load("risk_model.pkl")
# For demo purposes, we'll use the inline model from your current script
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Simulated model setup (copy from main script)
data = {
    'avg_speed': np.random.normal(50, 10, 1000),
    'harsh_braking': np.random.poisson(2, 1000),
    'rapid_accel': np.random.poisson(1, 1000),
    'night_driving_pct': np.random.uniform(0, 1, 1000),
    'mileage_per_day': np.random.normal(30, 5, 1000),
    'accident_risk_score': np.random.normal(50, 15, 1000)
}
df = pd.DataFrame(data)
X = df.drop('accident_risk_score', axis=1)
y = df['accident_risk_score']
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Flask app setup
app = Flask(__name__)
CORS(app)

@app.route("/api/risk_score", methods=["POST"])
def get_risk_score():
    data = request.get_json()
    try:
        input_df = pd.DataFrame([data])
        score = model.predict(input_df)[0]
        return jsonify({"score": round(score, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/sample_history", methods=["GET"])
def get_history():
    # Static response for frontend line chart
    return jsonify([
        {"date": "Week 1", "score": 48, "premium": 1200},
        {"date": "Week 2", "score": 45, "premium": 1150},
        {"date": "Week 3", "score": 42, "premium": 1100},
        {"date": "Week 4", "score": 38, "premium": 1050}
    ])

if __name__ == "__main__":
    app.run(debug=True)
