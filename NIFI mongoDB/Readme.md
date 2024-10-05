# Dockerized Lab ReadMe

## Overview
This lab sets up a data generation and transformation pipeline using Dockerized tools. It includes generating sales data, running SQL queries, and performing data transformations.

## Setup Instructions
1. **Start the Docker Environment**: 
   ```bash
   docker-compose up
   ```
   This will initialize the necessary services.

2. **Generate Sales Data**: 
   Run the Python script to generate sales data:
   ```bash
   python sales_data_generation.py
   ```

3. **Execute SQL Queries**: 
   Use the SQL queries from the provided file to interact with the generated data within the environment.

## Prerequisites
- Ensure Docker and Python are installed on your system.
- Properly configure the environment by unzipping and setting up any required components.