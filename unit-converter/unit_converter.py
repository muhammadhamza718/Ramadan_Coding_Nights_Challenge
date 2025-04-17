import streamlit as st
import math

# =============================================================================
# CUSTOM CSS STYLING
# =============================================================================
# This section defines the custom CSS styles for the application
# It creates a modern, clean UI inspired by Google's design language
st.markdown("""
<style>
/* Base styles */
.stApp {
    font-family: 'Google Sans', sans-serif !important;
}
/* Title and header styling */
h1 {
    font-weight: 500 !important;
    font-size: 2.5rem !important;
    margin-bottom: 2rem !important;
    color: #dc2626 !important;  /* Bright red */
}
.subtitle {
    font-size: 1.1rem;
    margin-bottom: 2rem;
    opacity: 0.8;
}
/* Button styling */
.stButton > button {
    border-radius: 8px !important;
    padding: 0.75rem 1.5rem !important;
    font-family: 'Google Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
    margin-top: 1rem !important;
    background-color: #dc2626 !important;  /* Bright red */
    color: white !important;
    border: none !important;
}
.stButton > button:hover {
    background-color: #b91c1c !important;  /* Darker red */
    box-shadow: 0 2px 6px rgba(220, 38, 38, 0.3) !important;
}
/* Result box styling */
.result-box {
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 2rem;
    text-align: center;
    font-size: 1.25rem;
    font-weight: 500;
    box-shadow: 0 4px 6px rgba(220, 38, 38, 0.1);
    border: 2px solid #dc2626;
}
/* Footer styling */
.footer {
    text-align: center;
    margin-top: 3rem;
    padding: 1rem;
    font-size: 0.9rem;
    opacity: 0.7;
}
/* Sidebar styling */
.stSidebar {
    width: 400px !important;
}
[data-testid="stSidebar"] {
    padding: 2rem 1rem;
}
[data-testid="stSidebar"] .stMarkdown {
    margin-bottom: 1.5rem;
}
[data-testid="stSidebarUserContent"] {
    padding-left: 1rem;
    padding-right: 1rem;
    padding-bottom: 4rem;
}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# SIDEBAR CONFIGURATION
# =============================================================================
# Set up the sidebar with title and instructions
st.sidebar.title("Conversion Type")
st.sidebar.markdown("Choose conversion type and units below")

# Create a dropdown for conversion type selection with emoji indicators
# The format_func parameter adds emojis to make the options more visually appealing
conversion_type = st.sidebar.selectbox(
    "Select Conversion Type",
    ["Length", "Weight", "Temperature"],
    index=0,
    format_func=lambda x: f"📏 {x}" if x == "Length" else f"⚖️ {x}" if x == "Weight" else f"🌡️ {x}"
)

# =============================================================================
# MAIN APPLICATION HEADER
# =============================================================================
# Display the main title and subtitle
st.title("Unit Converter")
st.markdown('<p class="subtitle">Convert between different units with real-time updates</p>',
            unsafe_allow_html=True)

# =============================================================================
# UNIT DEFINITIONS
# =============================================================================
# Define conversion factors for length units (all relative to meters)
# These values represent how many meters are in one unit of the given measurement
LENGTH_UNITS = {
    "Kilometer": 1000, "Meter": 1, "Centimeter": 0.01, "Millimeter": 0.001,
    "Micrometer": 0.000001, "Nanometer": 0.000000001, "Mile": 1609.344,
    "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254, "Nautical Mile": 1852
}

# Define conversion factors for weight units (all relative to grams)
# These values represent how many grams are in one unit of the given measurement
WEIGHT_UNITS = {
    "Kilogram": 1000, "Gram": 1, "Milligram": 0.001,
    "Metric Ton": 1000000, "Pound": 453.592, "Ounce": 28.3495
}

# Define temperature units (no conversion factors needed as they use formulas)
TEMPERATURE_UNITS = ["Celsius", "Fahrenheit", "Kelvin"]

# =============================================================================
# CONVERSION FUNCTIONS
# =============================================================================
def convert_length(value, from_unit, to_unit):
    """
    Convert a length value from one unit to another.
    
    This function works by:
    1. Converting the input value to meters (the base unit)
    2. Converting from meters to the target unit
    
    Args:
        value: The numeric value to convert
        from_unit: The source unit (must be a key in LENGTH_UNITS)
        to_unit: The target unit (must be a key in LENGTH_UNITS)
        
    Returns:
        The converted value in the target unit
    """
    # Convert to meters first (base unit)
    meters = value * LENGTH_UNITS[from_unit]
    # Convert from meters to target unit
    return meters / LENGTH_UNITS[to_unit]


def convert_weight(value, from_unit, to_unit):
    """
    Convert a weight value from one unit to another.
    
    This function works by:
    1. Converting the input value to grams (the base unit)
    2. Converting from grams to the target unit
    
    Args:
        value: The numeric value to convert
        from_unit: The source unit (must be a key in WEIGHT_UNITS)
        to_unit: The target unit (must be a key in WEIGHT_UNITS)
        
    Returns:
        The converted value in the target unit
    """
    # Convert to grams first (base unit)
    grams = value * WEIGHT_UNITS[from_unit]
    # Convert from grams to target unit
    return grams / WEIGHT_UNITS[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """
    Convert a temperature value from one scale to another.
    
    This function works by:
    1. Converting the input value to Kelvin (the base unit)
    2. Converting from Kelvin to the target scale
    
    Args:
        value: The numeric value to convert
        from_unit: The source temperature scale ("Celsius", "Fahrenheit", or "Kelvin")
        to_unit: The target temperature scale ("Celsius", "Fahrenheit", or "Kelvin")
        
    Returns:
        The converted temperature in the target scale
    """
    # Convert to Kelvin first (base unit)
    if from_unit == "Celsius":
        kelvin = value + 273.15
    elif from_unit == "Fahrenheit":
        kelvin = (value - 32) * 5/9 + 273.15
    else:
        kelvin = value

    # Convert from Kelvin to target unit
    if to_unit == "Celsius":
        return kelvin - 273.15
    elif to_unit == "Fahrenheit":
        return (kelvin - 273.15) * 9/5 + 32
    else:
        return kelvin

def format_number(number):
    """
    Format a number with appropriate precision based on its magnitude.
    
    This function ensures that numbers are displayed with the right number of decimal places:
    - Very small numbers (< 0.000001) use scientific notation
    - Small numbers (< 0.001) use 6 decimal places
    - Numbers less than 1 use 4 decimal places
    - Numbers less than 1000 use 2 decimal places
    - Larger numbers use 2 decimal places with thousands separators
    
    Args:
        number: The numeric value to format
        
    Returns:
        A formatted string representation of the number
    """
    if abs(number) < 0.000001:
        return f"{number:.8e}"
    elif abs(number) < 0.001:
        return f"{number:.6f}"
    elif abs(number) < 1:
        return f"{number:.4f}"
    elif abs(number) < 1000:
        return f"{number:.2f}"
    else:
        return f"{number:,.2f}"


# =============================================================================
# USER INTERFACE ELEMENTS
# =============================================================================
# Create a number input field for the value to convert
input_value = st.number_input(
    "Enter value", value=1.0, format="%f", key="input_value"
)

# Create two columns for the unit selection dropdowns
col1, col2 = st.columns(2)
with col1:
    # Dynamically select the appropriate units based on the conversion type
    units = {
        "Length": LENGTH_UNITS.keys(),
        "Weight": WEIGHT_UNITS.keys(),
        "Temperature": TEMPERATURE_UNITS
    }[conversion_type]
    # Create a dropdown for the source unit
    from_unit = st.selectbox("From", options=list(units), key="from_unit")

with col2:
    # Create a dropdown for the target unit
    to_unit = st.selectbox("To", options=list(units), key="to_unit")

# =============================================================================
# CONVERSION LOGIC AND RESULT DISPLAY
# =============================================================================
# Only perform conversion if a valid input value is provided
if input_value is not None:
    result = None
    # Select the appropriate conversion function based on the conversion type
    if conversion_type == "Length":
        result = convert_length(input_value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(input_value, from_unit, to_unit)
    else:  # Temperature
        result = convert_temperature(input_value, from_unit, to_unit)

    # Display the result if a conversion was performed
    if result is not None:
        formatted_result = format_number(result)
        st.markdown(
            f"""
            <div class="result-box">
                {format_number(input_value)} {from_unit} = {formatted_result} {to_unit}
            </div>
            """,
            unsafe_allow_html=True
        )

# =============================================================================
# ADDITIONAL CONTROLS
# =============================================================================
# Add a button to swap the source and target units
if st.button("🔄 Swap Units"):
    # Store the current units in temporary variables
    temp_from = st.session_state.from_unit
    temp_to = st.session_state.to_unit
    # Swap the units in the session state
    st.session_state.from_unit = temp_to
    st.session_state.to_unit = temp_from
    # Rerun the app to update the UI
    st.experimental_rerun()

# =============================================================================
# FOOTER
# =============================================================================
# Display the footer with credits
st.markdown("""
<div class="footer">
    Built with Streamlit • Inspired by Google's Unit Converter
</div>
""", unsafe_allow_html=True)
