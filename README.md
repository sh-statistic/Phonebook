# Phonebook
---

# PostgreSQL and MongoDB Database Creation with Python

This project demonstrates how to create a simple database using Python with both PostgreSQL and MongoDB as backend databases.

## Introduction

This project consists of two parts: one for PostgreSQL and one for MongoDB. Each part showcases how to set up a database, create tables/collections, insert sample data, and perform basic queries.

## Features

- PostgreSQL database creation and manipulation using Peewee ORM.
- MongoDB database creation and manipulation using PyMongo.
- Inserting sample data into both databases.
- Performing basic queries on the databases.

## Dependencies

- Python 3.x
- `peewee`
- `pymongo`

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/your_username/your_project.git
    ```

2. Install dependencies:

    ```
    pip install peewee pymongo
    ```

## Usage

1. Ensure PostgreSQL and MongoDB are installed and running on your system.
2. Configure the database connection settings in `local_settings.py`.
3. Run the PostgreSQL script (`postgres_example.py`) and the MongoDB script (`mongodb_example.py`) to see examples of database creation and manipulation.

## Examples

### PostgreSQL Example

This script sets up a PostgreSQL database using Peewee ORM, creates tables for `Information` and `Phone`, inserts random sample data, and prints any errors encountered.

### MongoDB Example

This script sets up a MongoDB database using PyMongo, creates collections for `Information` and `Phone`, inserts random sample data, performs a query based on a random last name, and prints the results.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

---

Ensure you replace placeholders like `your_username` and `your_project` with appropriate values for your project. Additionally, make sure to include the `local_settings.py` file in your repository with the necessary database connection settings.
