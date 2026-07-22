from movie import Movie
from person import Customer, PremiumCustomer
from movie_store import MovieStore

# Create movie store
store = MovieStore()

# Add movies
store.add_movie(Movie("M101", "Interstellar", "Sci-Fi", 5))
store.add_movie(Movie("M102", "Titanic", "Romance", 4))

# Register customers
store.register_customer(Customer("C101", "John"))
store.register_customer(PremiumCustomer("C102", "Alice"))

# Main menu
while True:
    print("\n===== Movie Rental System =====")
    print("1. Show Movies")
    print("2. Show Customers")
    print("3. Rent Movie")
    print("4. Return Movie")
    print("5. Show Rentals")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        store.show_movies()

    elif choice == "2":
        store.show_customers()

    elif choice == "3":
        customer_id = input("Enter Customer ID: ")
        movie_id = input("Enter Movie ID: ")
        days = int(input("Enter Rental Days: "))
        store.rent_movie(customer_id, movie_id, days)

    elif choice == "4":
        customer_id = input("Enter Customer ID: ")
        movie_id = input("Enter Movie ID: ")
        store.return_movie(customer_id, movie_id)

    elif choice == "5":
        store.show_rentals()

    elif choice == "6":
        print("Thank you for using Movie Rental System!")
        break

    else:
        print("Invalid choice. Please try again.")
