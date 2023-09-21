FROM fishtownanalytics/dbt:1.0.0

# Install necessary libraries
RUN pip install psycopg2-binary python-dotenv==1.0.0
