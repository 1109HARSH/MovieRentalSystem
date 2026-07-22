# MovieRentalSystem

# Movie Rental System

This is a Python Object-Oriented Programming (OOP) project developed to simulate a movie rental store. The system allows users to manage movies, customers, and rentals through a simple menu-driven interface while demonstrating core OOP concepts.

## What's the Project About?

The Movie Rental System enables users to register customers, add movies, rent and return movies, and view active rentals. It supports both regular and premium customers, where premium members receive a rental discount.

## Features

* Add and display movies
* Register regular and premium customers
* Rent and return movies
* View current rentals
* Automatic rental cost calculation
* Premium customer discount
* Unit testing using Python's `unittest`

## Files

* `movie.py` – Manages movie information and availability
* `person.py` – Contains `Person`, `Customer`, and `PremiumCustomer` classes
* `rental.py` – Handles rental details and cost calculation
* `movie_store.py` – Manages movies, customers, and rentals
* `main.py` – Menu-driven application
* `test_movie_store.py` – Unit tests for the system

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Python Standard Library
* `unittest` Framework

## How to Run

### Run the Application

```bash
python main.py
```

### Run the Unit Tests

```bash
python test_movie_store.py
```

## Main Menu Options

### 1. Show Movies

Displays all available movies with their details and availability.

### 2. Show Customers

Displays all registered customers and their membership type.

### 3. Rent Movie

Allows a customer to rent an available movie for a specified number of days.

### 4. Return Movie

Returns a rented movie and updates its availability.

### 5. Show Rentals

Displays all active movie rentals.

### 6. Exit

Closes the application.

## OOP Concepts Used

* Encapsulation using private attributes and properties
* Inheritance through `Person`, `Customer`, and `PremiumCustomer`
* Polymorphism using different customer discount calculations
* Composition by managing movies, customers, and rentals within the `MovieStore`

## Learning Outcomes

This project demonstrates:

* Object-Oriented Programming in Python
* Class and object design
* Encapsulation, inheritance, and polymorphism
* Menu-driven application development
* Unit testing with Python's `unittest`
* Basic exception handling

## Conclusion

This project provides a practical implementation of a movie rental management system using Python. It demonstrates fundamental OOP principles while offering a simple and user-friendly console application for managing movie rentals.
