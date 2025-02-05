import requests

def get_number_fact(number):
    """Fetch a fun fact about the given number using Numbers API."""
    url = f"http://numbersapi.com/{number}/math?jason"
    try:
        response = requests.get(url, timeout=5)  # Set a timeout for the request
        response.raise_for_status()  # Raise an error if response is not 200
        return response.text  # Return the fun fact as a string
    except requests.RequestException:
        return "Could not fetch a fun fact at this time."

