import streamlit as st
import pandas as pd

# Set the page configuration for the Streamlit app
st.set_page_config(page_title="Telematics Insurance Premium Calculator", page_icon="🚗", layout="wide")

# --- Constants ---
BASE_PREMIUM = 2500.0
RISK_FACTORS = {
    'speeding_incident_cost': 50.0,
    'hard_braking_cost': 30.0,
    'rapid_acceleration_cost': 25.0,
    'night_driving_multiplier': 1.5,
    'distance_cost_per_km': 0.05
}

def calculate_premium(distance, speeding_incidents, hard_braking_events, rapid_accel_events, night_driving_pct):
    """
    Calculates the insurance premium based on telematics data.
    """
    premium = BASE_PREMIUM
    premium += distance * RISK_FACTORS['distance_cost_per_km']
    premium += speeding_incidents * RISK_FACTORS['speeding_incident_cost']
    premium += hard_braking_events * RISK_FACTORS['hard_braking_cost']
    premium += rapid_accel_events * RISK_FACTORS['rapid_acceleration_cost']
    
    if night_driving_pct > 0:
        behavioral_cost = (premium - BASE_PREMIUM)
        premium += behavioral_cost * (night_driving_pct / 100.0) * (RISK_FACTORS['night_driving_multiplier'] - 1)

    return round(premium, 2)

def calculate_safety_score(distance, speeding, braking, acceleration, night_driving_pct):
    """
    Calculates a driver safety score from 0 to 100.
    """
    score = 100
    score -= speeding * 2.0  # 2 points off per speeding incident
    score -= braking * 1.0  # 1 point off per hard brake
    score -= acceleration * 1.0 # 1 point off per rapid acceleration
    score -= (distance / 1000) * 0.5 # 0.5 points off per 1000 km
    score -= (night_driving_pct / 10) # 1 point off per 10% of night driving
    
    return max(0, round(score)) # Ensure score doesn't go below 0

def main():
    """
    Main function to run the Streamlit application.
    """
    # --- UI Layout ---
    st.title("🚗 Telematics Insurance Premium Calculator")
    st.markdown("An interactive tool to understand how driving behavior impacts insurance premiums.")
    
    st.image("https://placehold.co/1200x300/06B6D4/FFFFFF?text=Drive+Smart,+Save+More", use_column_width=True)

    with st.sidebar:
        st.header("Driver Input Data")
        driver_id = st.text_input("Driver ID", "DRI-12345")
        distance_km = st.number_input("Total Distance Driven (km)", min_value=0.0, value=10000.0, step=100.0)
        speeding_incidents = st.number_input("Number of Speeding Incidents", min_value=0, value=5, step=1)
        hard_braking_events = st.number_input("Number of Hard Braking Events", min_value=0, value=10, step=1)
        rapid_acceleration_events = st.number_input("Number of Rapid Acceleration Events", min_value=0, value=8, step=1)
        night_driving_percentage = st.slider("Percentage of Night Driving (10 PM - 5 AM)", min_value=0, max_value=100, value=10, step=1)

    if st.sidebar.button("Calculate Premium", use_container_width=True):
        # --- Calculation ---
        final_premium = calculate_premium(
            distance=distance_km,
            speeding_incidents=speeding_incidents,
            hard_braking_events=hard_braking_events,
            rapid_accel_events=rapid_acceleration_events,
            night_driving_pct=night_driving_percentage
        )
        
        safety_score = calculate_safety_score(
            distance=distance_km,
            speeding=speeding_incidents,
            braking=hard_braking_events,
            acceleration=rapid_acceleration_events,
            night_driving_pct=night_driving_percentage
        )

        # --- Display Results ---
        st.header(f"Results for Driver: {driver_id}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Driver Safety Score")
            st.metric(label="Score (out of 100)", value=f"{safety_score}")
            st.progress(safety_score)
            if safety_score > 85:
                st.success("Excellent Driving!")
            elif safety_score > 60:
                st.info("Good Driving, with some room for improvement.")
            else:
                st.warning("Higher risk driving behavior detected.")

            st.subheader("Premium Details")
            st.metric(label="Base Premium", value=f"₹{BASE_PREMIUM:,.2f}")
            st.metric(label="Estimated Final Premium", value=f"₹{final_premium:,.2f}", delta=f"₹{final_premium - BASE_PREMIUM:,.2f} vs Base")

        with col2:
            st.subheader("Premium Cost Breakdown")
            
            risk_costs = {
                'Distance': distance_km * RISK_FACTORS['distance_cost_per_km'],
                'Speeding': speeding_incidents * RISK_FACTORS['speeding_incident_cost'],
                'Hard Braking': hard_braking_events * RISK_FACTORS['hard_braking_cost'],
                'Rapid Acceleration': rapid_acceleration_events * RISK_FACTORS['rapid_acceleration_cost']
            }
            
            # The base premium is the starting point
            cost_data = {
                'Cost Component': ['Base Premium'] + list(risk_costs.keys()),
                'Amount (₹)': [BASE_PREMIUM] + list(risk_costs.values())
            }
            
            cost_df = pd.DataFrame(cost_data)
            
            st.bar_chart(cost_df.set_index('Cost Component'))
            st.markdown("The chart shows the base premium plus additional costs from various risk factors.")

    else:
        st.info("Enter driver data in the sidebar and click 'Calculate Premium' to see the results.")

if __name__ == '__main__':
    main()
