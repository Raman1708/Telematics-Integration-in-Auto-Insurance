# 🚗 Telematics-Based Auto Insurance Premium Calculator

This is an interactive web application built with Streamlit that calculates an estimated auto insurance premium based on telematics data. It provides a user-friendly interface to demonstrate how driving behavior (like speeding, hard braking, and night driving) directly impacts insurance costs.

---

## 🚀 Live Demo

You can access the live application here:

**[➡️ Click here to view the live app](https://telematics-integration-in-auto-insurance-yhbzp4rbes27skrfig4qv.streamlit.app/)**


## ✨ Features

- **Interactive UI**: Easily input driving data using sliders and number fields.
- **Instant Premium Calculation**: Get real-time feedback on how different risk factors affect the premium.
- **Driver Safety Score**: Calculates a safety score from 0 to 100 to provide an overall assessment of driving behavior.
- **Cost Breakdown**: A visual bar chart shows exactly how the final premium is calculated, breaking down costs from the base premium and various risk factors.
- **Responsive Design**: The application is accessible on both desktop and mobile devices.

---

## ⚙️ How It Works

The application uses a rule-based model to calculate the insurance premium.

1.  **Base Premium**: A flat base rate is the starting point for the calculation.
2.  **Risk Factors**: The premium is adjusted based on several factors:
    - **Distance Driven**: A small cost is added per kilometer.
    - **Speeding Incidents**: Each incident adds a fixed penalty.
    - **Hard Braking Events**: Each event adds a fixed penalty.
    - **Rapid Acceleration Events**: Each event adds a fixed penalty.
    - **Night Driving**: A percentage-based multiplier is applied to the risk-based portion of the premium for driving during late hours (10 PM - 5 AM).
3.  **Safety Score**: A score is calculated by starting at 100 and subtracting points for risky behaviors and high mileage.

---

## 🛠️ Technologies Used

- **Python**: The core programming language.
- **Streamlit**: For building and hosting the interactive web application.
- **Pandas**: Used for data manipulation and creating the cost breakdown chart.

---
