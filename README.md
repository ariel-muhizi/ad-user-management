# ad-user-management - Fetch All Users

This project demonstrates the ability to fetch user data from an API and save it into a structured CSV file. It is designed to simulate operations on Active Directory (AD) user data while utilizing publicly available APIs to showcase practical skills in data extraction and manipulation.

## Project Overview

The script `fetch_all_users.py` performs the following tasks:
1. Fetches user data from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/users).
2. Extracts key user attributes (e.g., ID, Name, Username, Email, Phone, City, Zipcode).
3. Saves the extracted data into a CSV file located in the `data/` folder.

### How It Works

- The script fetches data from the mock JSONPlaceholder API, a service commonly used for testing and development.
- The data retrieved contains information about 10 users, which is parsed and saved into a CSV file for further processing.

### Output

The `all_users.csv` file includes the following columns:
- **ID**
- **Name**
- **Username**
- **Email**
- **Phone**
- **City**
- **Zipcode**

**Notes**
The project fetches data from the JSONPlaceholder API, which is a mock API for testing and development purposes.
The dataset is limited to 10 users for demonstration purposes.
   

