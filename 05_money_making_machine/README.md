# 💰 Money Making Machine

A fun and interactive Streamlit application that generates random money amounts, side hustle ideas, and money-related quotes to inspire your financial journey.

![Money Making Machine](https://img.shields.io/badge/Money%20Making%20Machine-v1.0.0-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- **Instant Cash Generator**: Generate random amounts of money with a single click
- **Side Hustle Ideas**: Get creative ideas for earning extra income
- **Money-Making Motivation**: Receive inspirational quotes about money and success
- **Interactive UI**: Simple and engaging user interface

## 📋 Requirements

- Python 3.8 or higher
- Streamlit
- Requests library
- A running backend server (for side hustle and quote features)

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/muhammadhamza718/Ramadan_Coding_Nights_Challenge/05_money-making-machine.git
   cd 05_money_making_machine
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the backend server (if applicable):

   ```bash
   # Instructions for starting your backend server
   ```

4. Run the application:
   ```bash
   streamlit run main.py
   ```

## 💻 Usage

1. **Generate Money**:

   - Click the "Generate Money" button
   - Watch as a random amount between $1 and $1000 is generated

2. **Get Side Hustle Ideas**:

   - Click the "Generate Hustle" button
   - Receive a creative idea for earning extra income

3. **Get Money-Making Motivation**:
   - Click the "Generate Quote" button
   - Receive an inspirational quote about money and success

## 🛠️ Development

The application is structured with the following components:

- `main.py`: Main application file containing all functionality
- `requirements.txt`: Dependencies
- `README.md`: Documentation

### Backend Integration

The application attempts to connect to a backend server running on `http://127.0.0.1:8000` to fetch:

- Side hustle ideas from `/side_hustles` endpoint
- Money quotes from `/money_quotes` endpoint

If the backend is unavailable, the application will fall back to default values.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Muhammad Hamza**

- GitHub: [@muhammadhamza718](https://github.com/muhammadhamza718)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing framework
- [Python](https://www.python.org/) for the programming language
- All contributors who have helped improve this project
