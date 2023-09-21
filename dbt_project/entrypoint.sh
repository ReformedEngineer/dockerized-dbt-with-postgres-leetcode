#!/bin/sh

# Run the Python script to generate sources.yml
python /dbt/generate_sources.py

# Execute the command provided in the docker command line
exec dbt "$@"
