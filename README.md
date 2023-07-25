# Northwind
## Overview
This project involves working with SQLite databases and executing SQL queries using Python's sqlite3 module. The tasks are divided into three parts, each focusing on different aspects of interacting with databases and writing SQL queries.

## Part 1 - Making and Populating a Database
In this part, we create a new SQLite database and populate it with data from a given table. The table contains columns "s," "x," and "y," and our goal is to store this data in a table named "demo" within the database. The specific tasks in this part are as follows:

Open a connection to a new (blank) database file called "demo_data.sqlite3."
Execute an appropriate CREATE TABLE statement to define the "demo" table structure.
Use INSERT INTO statements to add the provided data to the "demo" table.
Perform specific queries to test the "demo" database and save the results under predefined variable names: row_count, xy_at_least_5, and unique_y.

## Part 2 - The Northwind Database - Basic Queries
In this part, we work with the "northwind_small.sqlite3" database, which contains multiple tables with various relationships. We need to answer specific questions by writing SQL queries and retrieve data from the database. The tasks in this part include:

Connect to the "northwind_small.sqlite3" database.
Answer two specific questions related to the data in the database:
expensive_items: Find the ten most expensive items (per unit price) in the database and return all columns for those items.
avg_hire_age: Calculate the average age of an employee at the time of their hiring.

## Part 3 - Sailing the Northwind Seas (JOIN statements)
In this part, we continue working with the "northwind_small" database and focus on using JOIN statements to retrieve data from multiple related tables. The tasks in this part are:

Answer two specific questions using JOIN statements in SQL queries:
ten_most_expensive: Find the ten most expensive items (per unit price) in the database and retrieve their supplier information, including the ProductName, UnitPrice, and CompanyName columns.
largest_category: Determine the largest category in the database based on the number of unique products it contains.

## Project Files
demo_data.py: Contains the code to create the "demo_data.sqlite3" database, populate it with data, and execute queries for Part 1.
northwind.py: Contains the code to connect to the "northwind_small.sqlite3" database and execute queries for Parts 2 and 3.

## Results
The results of the executed queries are stored in the specified variables as query strings. These query strings represent the SQL statements used to retrieve the required data from the databases.
