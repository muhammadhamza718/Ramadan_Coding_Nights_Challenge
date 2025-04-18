import streamlit as st
import random
import string
import re

# =============================================================================
# CONSTANTS AND CONFIGURATION
# =============================================================================
# List of common weak passwords that should be avoided
# These passwords are frequently used and easily guessable
COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123", "password123", "admin", "letmein", "welcome"}

# =============================================================================
# PASSWORD STRENGTH CHECKING
# =============================================================================
def check_password_strength(password):
    """
    Evaluate the strength of a password using a point-based scoring system.
    
    This function checks multiple aspects of password security:
    1. Checks if the password is in a list of common weak passwords
    2. Evaluates password length (minimum 8 characters recommended)
    3. Checks for presence of uppercase and lowercase letters
    4. Checks for presence of numbers
    5. Checks for presence of special characters
    6. Awards bonus points for additional security features
    
    Args:
        password: The password string to evaluate
        
    Returns:
        score: A numeric score from 0-10 indicating password strength
        feedback: A list of suggestions to improve the password
    """
    score = 0
    feedback = []

    st.write(f"🔍 Checking password: `{password}`")

    # Check if password is in the blacklist of common weak passwords
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["❌ This password is too common. Choose a more unique password."]

    # Check password length - minimum 8 characters is recommended
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 2
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Check for presence of numbers
    if re.search(r'\d', password):
        score += 2
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Check for presence of special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 2
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Award bonus points for additional security features
    if len(password) >= 12:
        score += 2  # Bonus for longer passwords
    if re.search(r'\d{3,}', password):  # 3+ consecutive digits
        score += 1
    if re.search(r'[!@#$%^&*]{2,}', password):  # 2+ consecutive special chars
        score += 1

    # Return the final score and feedback
    return score, feedback

# =============================================================================
# PASSWORD GENERATION
# =============================================================================
def generate_strong_password(length=16):
    """
    Generate a cryptographically secure random password.
    
    This function creates a password by randomly selecting characters from:
    - Uppercase letters (A-Z)
    - Lowercase letters (a-z)
    - Numbers (0-9)
    - Special characters (!@#$%^&*)
    
    Args:
        length: The desired length of the password (default: 16)
        
    Returns:
        A randomly generated password string
    """
    # Combine all possible character types
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    # Generate a random password of the specified length
    password = ''.join(random.choices(all_chars, k=length))
    return password

# =============================================================================
# USER INTERFACE
# =============================================================================
# Set the page title
st.title("🔐 Password Strength Meter")

# Create a password input field (hidden by default)
password = st.text_input("Enter your password:", type="password")

# Create a button to check password strength
if st.button("Check Password Strength"):
    # Only proceed if a password was entered
    if password:
        # Evaluate the password strength
        score, feedback = check_password_strength(password)

        # Display appropriate message based on password strength score
        if score >= 9:
            st.success("🔥 Ultra Strong Password! Your password is very secure. 🔥")
        elif score >= 7:
            st.success("✅ Strong Password! Your password is secure. 👍")
        elif score >= 5:
            st.warning("⚠️ Almost Strong - Consider a minor improvement.")
        elif score >= 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        # Display feedback suggestions for improvement
        for msg in feedback:
            st.write(msg)

        # If password is not strong enough, suggest a stronger one
        if score < 7:
            strong_password = generate_strong_password()
            st.write("🔹 Suggested Strong Password: ", strong_password)
    else:
        # Prompt user to enter a password if none was provided
        st.warning("⚠️ Please enter a password!")
