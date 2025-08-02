from flask import Flask, request, jsonify
import os

app = Flask(__name__)

BASE_PREMIUM = 2500.0

RISK_FACTORS = {
    'speeding_incident_cost': 50.0,
    'hard_braking_cost': 30.0,
    'rapid_acceleration_cost': 25.0,
    'night_driving_multiplier': 1.5,
    'distance_cost_per_km': 0.05
}

@app.route('/')
def index():
    return "<h1>Telematics Insurance Premium API</h1><p>Send a POST request to /calculate_premium with your driving data.</p>"

@app.route('/calculate_premium', methods=['POST'])
def calculate_premium():
    try:
        data = request.get_json()

        required_fields = [
            "driver_id", "distance_km", "speeding_incidents",
            "hard_braking_events", "rapid_acceleration_events", "night_driving_percentage"
        ]
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing or invalid data in request body"}), 400

        distance = float(data['distance_km'])
        speeding_incidents = int(data['speeding_incidents'])
        hard_braking_events = int(data['hard_braking_events'])
        rapid_accel_events = int(data['rapid_acceleration_events'])
        night_driving_pct = float(data['night_driving_percentage'])

        premium = BASE_PREMIUM

        premium += distance * RISK_FACTORS['distance_cost_per_km']
        
        premium += speeding_incidents * RISK_FACTORS['speeding_incident_cost']
        premium += hard_braking_events * RISK_FACTORS['hard_braking_cost']
        premium += rapid_accel_events * RISK_FACTORS['rapid_acceleration_cost']
        
        if night_driving_pct > 0:
            behavioral_cost = (premium - BASE_PREMIUM)
            premium += behavioral_cost * night_driving_pct * (RISK_FACTORS['night_driving_multiplier'] - 1)

        response_data = {
            "driver_id": data['driver_id'],
            "base_premium": BASE_PREMIUM,
            "calculated_premium": round(premium, 2),
            "risk_summary": {
                "distance_km": distance,
                "speeding_incidents": speeding_incidents,
                "hard_braking_events": hard_braking_events,
                "rapid_acceleration_events": rapid_accel_events,
                "night_driving_percentage": night_driving_pct
            }
        }
        
        return jsonify(response_data), 200

    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid data type in request. Details: {str(e)}"}), 400
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
