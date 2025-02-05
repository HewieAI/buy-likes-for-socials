import requests

# Configuration
API_KEY = "your_smm_laboratory_api_key"
API_URL = "https://smmlaboratory.com/api/v2"

# Function to buy likes
def buy_likes(service_id, link, quantity):
    endpoint = f"{API_URL}"
    payload = {
        "key": API_KEY,
        "action": "add",
        "service": service_id,  # Service ID for likes
        "link": link,           # Link to the post
        "quantity": quantity    # Number of likes to buy
    }

    try:
        response = requests.post(endpoint, data=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        result = response.json()

        if result.get("error"):
            print(f"Error: {result['error']}")
        else:
            print(f"Order placed successfully! Order ID: {result['order']}")
            print(f"Details: {result}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    # Replace these values with your actual data
    service_id = 123  # Replace with the service ID for likes (check SMM Laboratory dashboard)
    post_link = "https://www.instagram.com/p/your-post-link/"  # Replace with your post link
    quantity = 100  # Number of likes to buy

    # Buy likes
    buy_likes(service_id, post_link, quantity)

# Run the script
if __name__ == "__main__":
    main()