# Import required libraries for the mood tracking application
import streamlit as st  # Streamlit: Modern web framework for creating interactive data apps
import pandas as pd     # Pandas: Powerful data manipulation and analysis library
import datetime        # Datetime: Standard library for handling dates and times
import csv            # CSV: Standard library for reading/writing CSV files
import os             # OS: Standard library for file and directory operations

# Configuration: Define the CSV file path for persistent mood data storage
MOOD_FILE = "mood_log.csv"

def load_mood_data():
    """
    Loads mood tracking data from CSV file.
    Returns an empty DataFrame if no data exists.
    """
    if not os.path.exists(MOOD_FILE):
        # Initialize empty DataFrame with required columns if file doesn't exist
        return pd.DataFrame(columns=["Date", "Mood"])
    # Load existing mood data from CSV file
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date, mood):
    """
    Appends a new mood entry to the CSV file.
    Args:
        date: The date of the mood entry
        mood: The mood value to be recorded
    """
    with open(MOOD_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Initialize Streamlit UI components
st.title("Mood Tracker")  # Main application title
today = datetime.date.today()  # Get current date for new entries

# Create mood input section
st.subheader("How are your feeling today?")
mood = st.selectbox(
    "Select your mood",
    ["Happy", "Sad", "Angry", "Neutral"]  # Available mood options
)

# Handle mood logging
if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")

# Load and display mood data
data = load_mood_data()

if not data.empty:
    # Create visualization section
    st.subheader("Mood Trends Over Time")
    
    # Process data for visualization
    data["Date"] = pd.to_datetime(data["Date"])  # Convert string dates to datetime
    mood_counts = data.groupby("Mood").count()["Date"]  # Calculate mood frequencies
    
    # Display mood distribution chart
    st.bar_chart(mood_counts)

# Footer with attribution
st.write("Build with ❤️ by [Muhammad Hamza](https://github.com/muhammadhamza718)")