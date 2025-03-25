from extract import extract_data
from transform import transform_data
from load import load_data

DB_CONFIG = {
    'dbname': 'your_database',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': 5432
}


def main():
    # Step 1: Extract data from source CSV
    data = extract_data('data/source_data.csv')

    # Step 2: Transform data
    transformed_data = transform_data(data)

    # Step 3: Load data into target database
    load_data(transformed_data, DB_CONFIG)


if __name__ == "__main__":
    main()
