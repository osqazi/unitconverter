import streamlit as st

def length_converter(frm_unit, to_unit, value):
    length_units = {
        "Meters": 1.0,
        "Kilometers": 0.001,
        "Centimeters": 100.0,
        "Millimeters": 1000.0,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    }
    return value * length_units[frm_unit] / length_units[to_unit]

def  weight_converter(to_unit, frm_unit, value):
    weight_units = {
        "Kilograms": 1.0,
        "Grams": 1000.0,
        "Milligrams": 1_000_000.0,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return value * weight_units[frm_unit] / weight_units[to_unit]

def temperature_converter(to_unit, frm_unit, value):
    if frm_unit == to_unit:
        return value
    if frm_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        if to_unit == "Kelvin":
            return value + 273.15
    if frm_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        if to_unit == "Kelvin":
            return (value + 459.67) * 5/9
    if frm_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        if to_unit == "Fahrenheit":
            return (value * 9/5) - 459.67
    
def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
    st.markdown("""
        <style>
        .stApp { background-color: #f4f4f4; }
        .title { text-align: center; font-size: 36px; color: #4a90e2; }
        .subtitle { text-align: center; font-size: 28px; color: #333; }
        .stSelectbox, .stNumberInput { border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)
    
    
    st.markdown("<h1 class='title'>Unit Converter App</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='subtitle'>Convert Length, Weight, and Temperature easily!</h3>", unsafe_allow_html=True)
    st.markdown("<h3 class='subtitle'>Project 3 - Created by Owais Qazi</h3>", unsafe_allow_html=True)
    
    
    category = st.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])
    value = round(st.number_input("Enter Value", min_value=0.0, format="%.6f"),6)
    if category == "Length":
        frm_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
        result = length_converter(frm_unit, to_unit, value)
        results = (f"{value:.6f} {frm_unit} is equal to {result:.6f} {to_unit}")
    elif category == "Weight":
        frm_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
        result = weight_converter(frm_unit, to_unit, value)
        results = (f"{value:.6f} {frm_unit} is equal to {result:.6f} {to_unit}")
    else:
        frm_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        result = temperature_converter(frm_unit, to_unit, value)
        results = (f"{value:.6f} {frm_unit} is equal to {result:.6f} {to_unit}")
    
    st.title({results})

if __name__ == "__main__":
    main()
