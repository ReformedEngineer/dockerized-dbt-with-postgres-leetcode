import psycopg2
import os
import yaml
from dotenv import load_dotenv

# Load the .env file explicitly
load_dotenv()

# Fetch environment variables using os.getenv
DB_DETAILS = {
    'dbname': os.getenv('DBT_DBNAME'),
    'user': os.getenv('DBT_USER'),
    'password': os.getenv('DBT_PASS'),
    'host': os.getenv('DBT_HOST'),
    'port': os.getenv('DBT_PORT')
}

# Fetch the project name from dbt_project.yml
def fetch_project_name():
    with open('./Local/dbt_project.yml', 'r') as f:
        dbt_config = yaml.safe_load(f)
        return dbt_config.get('name', '')

# Fetch tables from the leetcode database
def fetch_tables():
    try:
        connection = psycopg2.connect(**DB_DETAILS)
        cursor = connection.cursor()

        # Fetch all tables from the specified schema
        cursor.execute(f"SELECT tablename FROM pg_tables WHERE schemaname='{os.getenv('DBT_SCHEMA')}'")
        
        tables = cursor.fetchall()
        return [table[0] for table in tables]
    except Exception as error:
        print(f"Error fetching tables: {error}")
        return []   # Return an empty list in case of an error
    finally:
        if connection:
            cursor.close()
            connection.close()

# Generate sources.yml
def generate_sources_yml(tables):
    project_name = fetch_project_name()
    database = os.getenv('DBT_DBNAME')

    tables_string = "\n".join([f"      - name: {table}" for table in tables])
    
    content = f"""
version: 2

sources:
  - name: {database}
    database: {database}
    schema: public
    tables:
{tables_string}
"""

    destination_directory = os.path.join(project_name, 'models')
    os.makedirs(destination_directory, exist_ok=True)
    destination_file = os.path.join(destination_directory, 'sources.yml')

    with open(destination_file, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    tables = fetch_tables()
    generate_sources_yml(tables)
