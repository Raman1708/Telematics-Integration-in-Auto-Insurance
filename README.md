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

## 🧠 Learnings from the Project

Building this application provided several key insights and hands-on experience:

-   **Rapid Prototyping with Streamlit**: Gained practical experience in using Streamlit to quickly build and deploy interactive data applications. Learned to effectively use widgets like `st.slider` and `st.number_input` to capture user input and update the UI in real-time.

-   **Data-Driven UI Design**: Understood the importance of designing a user interface that provides immediate, visual feedback. The instant recalculation of the premium and safety score upon changing an input value makes the cause-and-effect relationship clear to the user.

-   **Implementing Business Logic in Code**: Translated a conceptual business model (rule-based premium calculation) into functional Python code. This involved defining variables, applying conditional logic for factors like night driving, and structuring the calculations logically.

-   **Data Visualization for Clarity**: Utilized Pandas to structure the cost components and Streamlit's `st.bar_chart` to create a simple yet effective visualization. This reinforces the principle that visualizing data is crucial for making it understandable, especially when breaking down complex figures like an insurance premium.

-   **Full-Stack Application Thinking**: While simple, the project covers the end-to-end process of application development: from backend logic (Python calculations) and frontend interface (Streamlit UI) to deployment (hosting on a public platform).
