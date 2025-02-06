# Number Classification API

## Project Description
The Number Classification API is a Django REST Framework-based API that classifies numbers based on their properties. It determines whether a number is prime, perfect, Armstrong, odd, or even. Additionally, it fetches fun facts about numbers from the Numbers API.

## Features
- Classifies numbers (Prime, Perfect, Armstrong, Odd/Even)
- Fetches fun facts about numbers using the Numbers API
- Returns JSON responses
- CORS enabled for cross-origin requests

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Deployment:** Render
- **External API Integration:** Numbers API

  ## Setup Instructions

Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Git

Installation Steps
```bash
# Clone the repository
git clone https://github.com/Nsikanekpo/number-classification-api.git
cd number-classification-api

# Create a virtual environment and activate it
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

### Environment Variables
Create a `.env` file and add the following:
```
SECRET_KEY=your_secret_key
DEBUG=True
```

## API Usage

### Base URL
```
https://number-classification-api-dijq.onrender.com/
```

### Endpoints
#### **Classify a Number**
**GET** `/classify/<number>/`
- **Example Request:**
  ```bash
  curl -X GET https://number-classification-api-dijq.onrender.com/classify/7/
  ```
- **Example Response:**
  ```json
  {
    "number": 7,
    "is_prime": true,
    "is_perfect": false,
    "is_armstrong": false,
    "is_even": false,
    "fun_fact": "7 is the number of continents in the world."
  }
  ```

## Deployment
The API is deployed on **Render**.

### Procfile for Deployment
```
web: gunicorn core.wsgi:application --preload
```

## Known Issues
- The API works with `curl` but has connection issues with the Postman desktop app. Possible solutions include disabling SSL verification in Postman settings.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make changes and commit (`git commit -m 'Add feature'`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request


## Acknowledgments
- Django REST Framework documentation
- Numbers API for number facts
- Render for deployment

