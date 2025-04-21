"""
Money Making Machine

A Streamlit application that generates random money amounts, side hustle ideas, 
and money-related quotes to inspire your financial journey.

Author: [Your Name]
GitHub: [Your GitHub Profile]
License: MIT
Version: 1.0.0
"""

import streamlit as st
import random as rd
import time 
import requests
import logging
from typing import Dict, Any, Optional, List
import json
import os
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
API_BASE_URL = "http://127.0.0.1:8000"
DEFAULT_SIDE_HUSTLE = "Freelancing"
DEFAULT_QUOTE = "Money is the root of all evil!"
MAX_MONEY_AMOUNT = 1000
MIN_MONEY_AMOUNT = 1

# Set page configuration
st.set_page_config(
    page_title="Money Making Machine",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def generate_money() -> int:
    """
    Generate a random amount of money.
    
    Returns:
        int: A random amount between MIN_MONEY_AMOUNT and MAX_MONEY_AMOUNT
    """
    return rd.randint(MIN_MONEY_AMOUNT, MAX_MONEY_AMOUNT)

def fetch_data_from_api(endpoint: str, fallback: str) -> str:
    """
    Fetch data from the API with error handling.
    
    Args:
        endpoint: The API endpoint to fetch from
        fallback: The fallback value if the API call fails
        
    Returns:
        str: The fetched data or fallback value
    """
    try:
        response = requests.get(f"{API_BASE_URL}/{endpoint}", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get(endpoint, fallback)
        else:
            logger.warning(f"API returned status code {response.status_code}")
            return fallback
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from API: {str(e)}")
        return fallback
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON response: {str(e)}")
        return fallback
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return fallback

def fetch_side_hustle() -> str:
    """
    Fetch a side hustle idea from the API.
    
    Returns:
        str: A side hustle idea or the default value
    """
    return fetch_data_from_api("side_hustles", DEFAULT_SIDE_HUSTLE)

def fetch_money_quote() -> str:
    """
    Fetch a money-related quote from the API.
    
    Returns:
        str: A money quote or the default value
    """
    return fetch_data_from_api("money_quotes", DEFAULT_QUOTE)

def save_transaction(amount: int) -> None:
    """
    Save a transaction to a log file.
    
    Args:
        amount: The amount of money generated
    """
    try:
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        log_file = os.path.join(log_dir, "transactions.log")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(log_file, "a") as f:
            f.write(f"{timestamp}, {amount}\n")
            
        logger.info(f"Transaction logged: ${amount} at {timestamp}")
    except Exception as e:
        logger.error(f"Error saving transaction: {str(e)}")

def main():
    """Main application function"""
    st.title("💰 Money Making Machine")
    
    # Add sidebar with information
    with st.sidebar:
        st.header("About")
        st.info("""
        This app helps you generate random money amounts, get side hustle ideas, 
        and receive money-related quotes to inspire your financial journey.
        
        **Features:**
        - Instant Cash Generator
        - Side Hustle Ideas
        - Money-Making Motivation
        
        **Contributions welcome!** Visit our [GitHub repository](https://github.com/yourusername/money-making-machine) to contribute.
        """)
        
        st.header("Statistics")
        st.metric("Total Money Generated", "$0")
        st.metric("Side Hustles Generated", "0")
        st.metric("Quotes Generated", "0")
    
    # Main content
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Instant Cash Generator")
        if st.button("Generate Money", type="primary"):
            with st.spinner("Counting your money..."):
                time.sleep(1)
                amount = generate_money()
                save_transaction(amount)
                st.success(f"You made ${amount}!")
    
    with col2:
        st.subheader("Side Hustle Ideas")
        if st.button("Generate Hustle"):
            with st.spinner("Finding the perfect side hustle..."):
                idea = fetch_side_hustle()
                st.success(idea)
    
    with col3:
        st.subheader("Money-Making Motivation")
        if st.button("Generate Quote"):
            with st.spinner("Finding the perfect quote..."):
                quote = fetch_money_quote()
                st.info(quote)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>Made with ❤️ by <a href="https://github.com/yourusername">Your Name</a></p>
        <p>Open source project - <a href="https://github.com/yourusername/money-making-machine">GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 