import streamlit as st

# Set the page configuration for the Streamlit app
st.set_page_config(page_title="Telematics Insurance Premium Calculator", page_icon="🚗")

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

    # 1. Add cost based on total distance driven
    premium += distance * RISK_FACTORS['distance_cost_per_km']
    
    # 2. Add penalties for risky driving behaviors
    premium += speeding_incidents * RISK_FACTORS['speeding_incident_cost']
    premium += hard_braking_events * RISK_FACTORS['hard_braking_cost']
    premium += rapid_accel_events * RISK_FACTORS['rapid_acceleration_cost']
    
    # 3. Apply a multiplier for night driving
    if night_driving_pct > 0:
        # The multiplier only applies to the risk-based portion of the premium
        behavioral_cost = (premium - BASE_PREMIUM)
        premium += behavioral_cost * (night_driving_pct / 100.0) * (RISK_FACTORS['night_driving_multiplier'] - 1)

    return round(premium, 2)

def main():
    """
    Main function to run the Streamlit application.
    """
    # --- UI Layout ---
    st.title("🚗 Telematics Insurance Premium Calculator")
    st.markdown("Enter the driving data below to calculate the estimated insurance premium.")

    with st.sidebar:
        st.header("Driver Input")
        distance_km = st.number_input("Total Distance Driven (km)", min_value=0.0, value=10000.0, step=100.0)
        speeding_incidents = st.number_input("Number of Speeding Incidents", min_value=0, value=5, step=1)
        hard_braking_events = st.number_input("Number of Hard Braking Events", min_value=0, value=10, step=1)
        rapid_acceleration_events = st.number_input("Number of Rapid Acceleration Events", min_value=0, value=8, step=1)
        night_driving_percentage = st.slider("Percentage of Night Driving (10 PM - 5 AM)", min_value=0, max_value=100, value=10, step=1)

    if st.button("Calculate Premium"):
        # --- Calculation ---
        final_premium = calculate_premium(
            distance=distance_km,
            speeding_incidents=speeding_incidents,
            hard_braking_events=hard_braking_events,
            rapid_accel_events=rapid_acceleration_events,
            night_driving_pct=night_driving_percentage
        )

        # --- Display Results ---
        st.subheader("Premium Calculation Results")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Base Premium", value=f"₹{BASE_PREMIUM:,.2f}")
        with col2:
            st.metric(label="Estimated Final Premium", value=f"₹{final_premium:,.2f}")

        if final_premium > BASE_PREMIUM:
            st.warning(f"The premium is ₹{final_premium - BASE_PREMIUM:,.2f} higher than the base due to driving behavior and distance.")
        else:
            st.success("Excellent driving! Your premium is at or below the base rate.")

        with st.expander("See Risk Factor Details"):
            st.write(f"- **Distance Cost:** ₹{distance_km * RISK_FACTORS['distance_cost_per_km']:,.2f}")
            st.write(f"- **Speeding Cost:** ₹{speeding_incidents * RISK_FACTORS['speeding_incident_cost']:,.2f}")
            st.write(f"- **Hard Braking Cost:** ₹{hard_braking_events * RISK_FACTORS['hard_braking_cost']:,.2f}")
            st.write(f"- **Rapid Acceleration Cost:** ₹{rapid_acceleration_events * RISK_FACTORS['rapid_acceleration_cost']:,.2f}")


if __name__ == '__main__':
    main()
