"""
Time Zone Converter Application

A Streamlit application that allows users to:
1. View current time in multiple time zones
2. Convert time between different time zones

Author: [Muhamad Hamza Samad]
GitHub: [https://github.com/muhammadhamza718]
License: MIT
Version: 1.0.0
"""

import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
TIME_ZONES: List[str] = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Set page configuration
st.set_page_config(
    page_title="Time Zone Converter",
    page_icon="⏰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_current_time(timezone: str) -> str:
    """
    Get the current time in the specified timezone.
    
    Args:
        timezone: The timezone to get the time for
        
    Returns:
        Formatted time string
    """
    try:
        return datetime.now(ZoneInfo(timezone)).strftime("%Y-%m-%d %I:%M:%S %p")
    except Exception as e:
        logger.error(f"Error getting time for {timezone}: {str(e)}")
        return "Error retrieving time"

def convert_time(time: datetime.time, from_tz: str, to_tz: str) -> Optional[str]:
    """
    Convert time from one timezone to another.
    
    Args:
        time: The time to convert
        from_tz: Source timezone
        to_tz: Target timezone
        
    Returns:
        Formatted converted time string or None if error occurs
    """
    try:
        dt = datetime.combine(datetime.today(), time, tzinfo=ZoneInfo(from_tz))
        return dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    except Exception as e:
        logger.error(f"Error converting time from {from_tz} to {to_tz}: {str(e)}")
        return None

def main():
    """Main application function"""
    st.title("⏰ Time Zone Converter")
    
    # Add sidebar with information
    with st.sidebar:
        st.header("About")
        st.info("""
        This app helps you view and convert times across different time zones.
        
        **Features:**
        - View current time in multiple time zones
        - Convert time between different time zones
        
        **Contributions welcome!** Visit our [GitHub repository](https://github.com/yourusername/time-zone-app) to contribute.
        """)
        
        st.header("Documentation")
        st.markdown("""
        ### How to use:
        1. Select time zones to view current times
        2. Use the converter to change time between zones
        """)
    
    # Main content
    st.subheader("Current Time in Selected Timezones")
    selected_timezone = st.multiselect(
        "Select Timezones", 
        TIME_ZONES, 
        default=["UTC", "Asia/Karachi"],
        help="Choose one or more time zones to display current time"
    )
    
    # Display current time in selected timezones
    cols = st.columns(min(3, len(selected_timezone)))
    for i, tz in enumerate(selected_timezone):
        col_idx = i % len(cols)
        with cols[col_idx]:
            current_time = get_current_time(tz)
            st.metric(tz, current_time)
    
    # Time conversion section
    st.subheader("Convert Time Between Timezones")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        current_time = st.time_input("Current Time", value=datetime.now().time())
    
    with col2:
        from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
    
    with col3:
        to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)
    
    if st.button("Convert Time", type="primary"):
        converted_time = convert_time(current_time, from_tz, to_tz)
        if converted_time:
            st.success(f"Converted Time in {to_tz}: {converted_time}")
        else:
            st.error("Failed to convert time. Please try again.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>Made with ❤️ by <a href="https://github.com/muhammadhamza718">Muhammad Hamza</a></p>
        <p>Open source project - <a href="https://github.com/muhammadhamza718/Ramadan_Coding_Nights_Challenge/06_time_zone_app">GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()