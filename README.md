# 🏥 Health Management Backend

A robust Python backend system for managing health-related data and calculations. This application provides essential health metrics calculations and user authentication features.

## 📋 Features

- **BMI Calculator** - Calculate Body Mass Index with accurate health categorization
- **User Authentication** - Secure user registration and login system
- **Health Data Management** - Track and manage user health information
- **RESTful API** - Clean API endpoints for easy integration

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Backend Framework:** Flask/FastAPI (based on main.py implementation)
- **Authentication:** Custom authentication module
- **Data Storage:** File-based or Database (configurable)

## 📁 Project Structure

```
HealthManagement_Backend/
├── main.py           # Main application entry point
├── auth.py           # Authentication and authorization logic
├── manager.py        # Health data management functions
├── BMI.py            # BMI calculation utilities
├── .gitignore        # Git ignore rules
└── __pycache__/      # Python cache files
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/shubhankar011/HealthManagement_Backend.git
cd HealthManagement_Backend
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

### Running the Application

```bash
python main.py
```

The server will start on the default port (typically `http://localhost:5000` or `http://localhost:8000`).

## 📡 API Endpoints

### Authentication
- `POST /register` - Register a new user
- `POST /login` - User login
- `POST /logout` - User logout

### Health Management
- `POST /bmi/calculate` - Calculate BMI
- `GET /health/profile` - Get user health profile
- `PUT /health/profile` - Update health information

## 💡 Usage Examples

### Calculate BMI
```python
import requests

response = requests.post('http://localhost:5000/bmi/calculate', json={
    'weight': 70,  # in kg
    'height': 1.75  # in meters
})

print(response.json())
```

### User Registration
```python
response = requests.post('http://localhost:5000/register', json={
    'username': 'john_doe',
    'email': 'john@example.com',
    'password': 'secure_password'
})
```

## 🔐 Security

- Passwords are hashed before storage
- Authentication tokens for session management
- Input validation on all endpoints
- CORS configuration for safe cross-origin requests

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author
**Pratyush Kush**
- GitHub: [pratyush789245](https://github.com/pratyush789245)
## 👨‍💻
**Shubhankar**
- GitHub: [@shubhankar011](https://github.com/shubhankar011)

## 🙏 Acknowledgments

- Original repository by [@pratyush789245](https://github.com/pratyush789245)
- Inspired by modern health tracking applications
- Built with best practices for backend development

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainer.

---

⭐ **Star this repository if you find it helpful!**
