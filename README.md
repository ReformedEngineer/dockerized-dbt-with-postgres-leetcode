# Dockerised DBT Postgres Integration with LeetCode SQL Challenges

This project integrates DBT with a Postgres database, primarily focusing on SQL challenges from LeetCode. It sets up a Dockerized environment for DBT and Postgres, automatically generates DBT source configurations based on the Postgres schema, and enables users to practice and test their SQL skills.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
- Docker & Docker Compose installed on your machine.
- Python environment (recommended to use a virtual environment).

## Setup and Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ReformedEngineer/dockerized-dbt-with-postgres-leetcode.git
   cd your-repo-directory
   ```

2. **Set Environment Variables**:
   - Rename `sample.env` to `.env`.
   - Update the `.env` file with your specific database configurations.

3. **Build the Docker Environment**:
   ```bash
   docker-compose run dbt init (choose a project name , it is 'local' here. )
   modify the profiles.yml file based on your .env file
   docker-compose build
   ```

4. **Start the Services**:
   ```bash
   docker-compose up -d
   ```

5. **Generate DBT Sources Configuration**:
   Navigate to the `dbt_project` directory and run:
   ```bash
   python generate_sources.py
   ```

## Usage

1. **Run DBT Commands**:
   For instance, to run DBT models:
   ```bash
   docker-compose run dbt run --project-dir /dbt/Local
   ```

2. **SQL Challenges**:
   Models inside the `dbt_project/Local/models/medium` directory are based on SQL challenges from LeetCode. Practice your SQL skills by working on these challenges and verifying your solutions using DBT.

## Acknowledgments
This project is using leetcode questions dump file from [cM2908's leetcode-sql repository](https://github.com/cM2908/leetcode-sql) to set up a local postgres database called leetcode
