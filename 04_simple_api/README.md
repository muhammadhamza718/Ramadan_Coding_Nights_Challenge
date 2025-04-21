# Money Motivation API 💰

A RESTful API service built with FastAPI that provides random side hustle ideas and money-related quotes to inspire and motivate users in their financial journey.

## 🌟 Features

- Random side hustle suggestions
- Inspirational money quotes
- RESTful endpoints
- Comprehensive API documentation
- Health check endpoint
- Proper error handling
- Logging system
- Type hints and validation

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/muhammadhamza718/Ramadan_Coding_Nights_Challenge/04_simple_api.git
cd 04_simple_api
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the API

1. Start the server:

```bash
uvicorn Fastapi:app --reload
```

2. Access the API:

- API Documentation: http://localhost:8000/docs
- ReDoc Documentation: http://localhost:8000/redoc
- Health Check: http://localhost:8000/health

## 📚 API Endpoints

### Root Endpoint

```
GET /
```

Returns welcome message and API information.

### Side Hustles

```
GET /side_hustles
```

Returns a random side hustle idea.

### Money Quotes

```
GET /money_quotes
```

Returns a random money-related quote.

### Health Check

```
GET /health
```

Returns the health status of the API.

## 🔒 Security

The API includes several security features:

- Input validation
- Error handling
- Logging system
- API key authentication (to be implemented)
- Rate limiting (to be implemented)
- CORS policies (to be implemented)

## 📝 API Documentation

The API documentation is available at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🛠️ Development

### Project Structure

```
money-motivation-api/
├── Fastapi.py          # Main API implementation
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

### Adding New Features

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📈 Future Improvements

- [ ] Implement API key authentication
- [ ] Add rate limiting
- [ ] Implement CORS policies
- [ ] Add database integration
- [ ] Add caching layer
- [ ] Add more side hustle categories
- [ ] Add more money quotes
- [ ] Add user authentication
- [ ] Add analytics tracking

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- FastAPI framework
- Python community
- All contributors and supporters

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---

Made with ❤️ by [Muhammad Hamza](https://github.com/muhammadhamza718)
