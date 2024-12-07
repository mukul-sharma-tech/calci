import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Dropdown for selecting operation
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Button to calculate result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"Result: {result}")
