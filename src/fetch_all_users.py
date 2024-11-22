import requests
import csv
import os

def fetch_all_users():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    
    if response.status_code == 200:
        users = response.json()
        print(f"Fetched {len(users)} users from the API.")
    else:
        print(f"Failed to fetch users: {response.status_code}")
        return []

    return users

def save_to_csv(users, filename):
    headers = ['ID', 'Name', 'Username', 'Email', 'Phone', 'City', 'Zipcode']
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        for user in users:
            writer.writerow([
                user['id'],
                user['name'],
                user['username'],
                user['email'],
                user['phone'],
                user['address']['city'],
                user['address']['zipcode']
            ])
    
    print(f"Data saved to {filename}")

def main():
    users = fetch_all_users()
    if users:
        # Get the absolute path to the data folder and CSV file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, '..', 'data', 'all_users.csv')
        save_to_csv(users, csv_path)

if __name__ == "__main__":
    main()