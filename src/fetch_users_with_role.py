import csv

def fetch_users_with_role(role, input_file='data/all_users.csv', output_file='data/users_with_role.csv'):
    """
    Fetch users from a CSV file who match the specified role.
    """
    filtered_users = []

    # Open the input file
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        csvreader = csv.DictReader(infile)
        
        # Filter users based on the role
        for row in csvreader:
            if row['role'] == role:
                filtered_users.append(row)

    # Write the filtered users to the output file
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['first_name', 'last_name', 'email', 'role']  # Add the fieldnames you want
        csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write header and data
        csvwriter.writeheader()
        for user in filtered_users:
            csvwriter.writerow(user)
    
    print(f"Users with role '{role}' have been saved to {output_file}.")

# Example of how to run the function
if __name__ == "__main__":
    role_to_filter = "Admin"  # Replace with the role you want to filter by
    fetch_users_with_role(role_to_filter)
