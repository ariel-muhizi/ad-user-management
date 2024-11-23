# api-user-data-manager

This project fetches user data from a free API, saves it into a neat CSV file, and creates a simple visualization to explore it further. It’s a super lightweight way to showcase practical API usage, data handling, and visualization skills.

## Project Overview

The script `fetch_all_users.py` performs the following tasks:
1. Fetches user data from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/users).
2. Extracts key user attributes (e.g., ID, Name, Username, Email, Phone, City, Zipcode).
3. Saves the extracted data into a CSV file located in the `data/` folder.
4. Visualizes the data in `visualize_data.py` to uncover patterns such as the distribution of users across cities.

### How It Works

- The script fetches data from the mock JSONPlaceholder API, a service commonly used for testing and development.
- The data retrieved contains information about 10 users, which is parsed and saved into a CSV file for further processing.
- The `visualize_data.py` script processes the saved CSV file and generates a bar chart showing the number of users in each city. This helps quickly identify where the users are concentrated.

### Output

The `all_users.csv` file includes the following columns:
- **ID**
- **Name**
- **Username**
- **Email**
- **Phone**
- **City**
- **Zipcode**

### Notes ###
The project fetches data from the JSONPlaceholder API, which is a mock API for testing and development purposes.
The dataset is limited to 10 users for demonstration purposes.
   

