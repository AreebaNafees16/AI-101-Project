import streamlit as st

# Streamlit App Title
st.title("BMI Calculator 💪")

# User Inputs
# weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
# height = st.number_input("Enter your height (cm):", min_value=1.0, step=0.1)

weight = st.slider("Enter your weight (kg):", 40, 200, 70)
height = st.slider("Enter your height (cm):", 100, 220, 175)

# BMI Calculation
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        height_m = height / 100  # Convert cm to meters
        bmi = weight / (height_m ** 2)  # BMI Formula

        # Determine BMI Category
        if bmi < 18.5:
            category = "Underweight 😟"
            color = "blue"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight ✅"
            color = "green"
        elif 25 <= bmi < 29.9:
            category = "Overweight ⚠️"
            color = "orange"
        else:
            category = "Obese ❌"
            color = "red"

        # Display Results
        st.success(f"Your BMI is **{bmi:.2f}**")
        st.markdown(f"<h3 style='color:{color};'>{category}</h3>", unsafe_allow_html=True)
    else:
        st.error("Please enter valid height and weight!")

