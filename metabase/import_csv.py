import csv
import mysql.connector

# Database connection details
db_config = {
    'host': 'localhost',       # Change to your database host
    'user': 'your_username',   # Change to your MySQL username
    'password': 'your_password',  # Change to your MySQL password
    'database': 'your_database'   # Change to your target database
}

# Path to the CSV file
csv_file_path = 'insurance_sales_leads.csv'

# Initialize connection variable
connection = None

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    # Create the table if it doesn't exist
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS insurance_sales_leads (
        lead_id INT AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(100),
        email VARCHAR(100),
        phone_number VARCHAR(15),
        city VARCHAR(50),
        insurance_type VARCHAR(50),
        lead_source VARCHAR(50),
        status VARCHAR(20),
        follow_up_date DATE,
        created_at TIMESTAMP
    );
    '''
    cursor.execute(create_table_query)
    print("Table created or already exists.")
    
    # Insert data from CSV
    insert_query = '''
    INSERT INTO insurance_sales_leads 
    (full_name, email, phone_number, city, insurance_type, lead_source, status, follow_up_date, created_at) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            cursor.execute(insert_query, row)
    
    # Commit changes
    connection.commit()
    print("Data inserted successfully.")

except mysql.connector.Error as err:
    print(f"Database Error: {err}")

except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found.")

finally:
    # Close the connection if it was opened
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
