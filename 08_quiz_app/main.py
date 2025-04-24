import streamlit as st # for the web interface
import random # for randomizing the questions
import time # for the timer

# Title of the Application
st.title("📝 Quiz Application")

# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "What is Python?",
        "options": [
            "A snake species",
            "A programming language",
            "A web browser",
            "A database system"
        ],
        "answer": "A programming language",
    },
    {
        "question": "Who created Python?",
        "options": [
            "Guido van Rossum",
            "James Gosling",
            "Brendan Eich",
            "Rasmus Lerdorf"
        ],
        "answer": "Guido van Rossum",
    },
    {
        "question": "Which of the following is NOT a Python data type?",
        "options": [
            "List",
            "Dictionary",
            "Array",
            "Tuple"
        ],
        "answer": "Array",
    },
    {
        "question": "What is the correct way to create a function in Python?",
        "options": [
            "function myFunc():",
            "def myFunc():",
            "create myFunc():",
            "func myFunc():"
        ],
        "answer": "def myFunc():",
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": [
            "^",
            "**",
            "^^",
            "exp"
        ],
        "answer": "**",
    },
    {
        "question": "What does the 'self' keyword represent in a Python class?",
        "options": [
            "The class itself",
            "The parent class",
            "The instance of the class",
            "A static method"
        ],
        "answer": "The instance of the class",
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": [
            "Curly braces {}",
            "Parentheses ()",
            "Indentation",
            "Keywords begin/end"
        ],
        "answer": "Indentation",
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": [
            "6",
            "8",
            "5",
            "Error"
        ],
        "answer": "8",
    },
    {
        "question": "Which method is used to add an item to the end of a list in Python?",
        "options": [
            "append()",
            "add()",
            "insert()",
            "push()"
        ],
        "answer": "append()",
    },
    {
        "question": "What is the correct way to create a variable in Python?",
        "options": [
            "var x = 5",
            "x = 5",
            "variable x = 5",
            "int x = 5"
        ],
        "answer": "x = 5",
    },
    {
        "question": "Which of the following is a valid comment in Python?",
        "options": [
            "// This is a comment",
            "/* This is a comment */",
            "# This is a comment",
            "<!-- This is a comment -->"
        ],
        "answer": "# This is a comment",
    },
    {
        "question": "What is the purpose of the 'import' statement in Python?",
        "options": [
            "To export functions",
            "To include modules",
            "To define classes",
            "To create variables"
        ],
        "answer": "To include modules",
    },
    {
        "question": "Which of the following is NOT a Python loop?",
        "options": [
            "for",
            "while",
            "do-while",
            "for-in"
        ],
        "answer": "do-while",
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [
            ".py",
            ".python",
            ".pt",
            ".pyt"
        ],
        "answer": ".py",
    },
    {
        "question": "Which of the following is a Python web framework?",
        "options": [
            "Django",
            "Spring",
            "Express",
            "Laravel"
        ],
        "answer": "Django",
    },
]

# Initialize session state variables if they don't exist
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.asked_questions = [st.session_state.current_question]
    st.session_state.score = 0
    st.session_state.total_questions = 0

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Submit button the check the answer
if st.button("Submit Answer"):
    # Increment total questions counter
    st.session_state.total_questions += 1
    
    # check if the answer is correct
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.session_state.score += 1
    else:
        st.error("❌ Incorrect! The correct answer is " + question["answer"])
  
    # Wait for 3 seconds before showing the next question
    time.sleep(3)

    # Select a new random question that hasn't been asked yet
    available_questions = [q for q in questions if q not in st.session_state.asked_questions]
    
    # If all questions have been asked, reset the asked questions list
    if not available_questions:
        st.session_state.asked_questions = []
        available_questions = questions
    
    # Select a new random question
    st.session_state.current_question = random.choice(available_questions)
    st.session_state.asked_questions.append(st.session_state.current_question)

    # Rerun the app to display the next question    
    st.rerun()

# Display score
st.sidebar.header("Quiz Stats")
st.sidebar.write(f"Score: {st.session_state.score}/{st.session_state.total_questions}")
st.sidebar.write(f"Questions answered: {len(st.session_state.asked_questions)}")