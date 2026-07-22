from rental import Rental

class MovieStore:

    def __init__(self):
        # Store movies, customers and rentals
        self.movies = {}
        self.customers = {}
        self.rentals = []

    # Add a new movie
    def add_movie(self, movie):
        self.movies[movie.movie_id] = movie

    # Register a new customer
    def register_customer(self, customer):
        self.customers[customer.person_id] = customer

    # Rent a movie
    def rent_movie(self, customer_id, movie_id, days):
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)

        if customer is None or movie is None:
            print("Invalid customer or movie.")
            return

        if not movie.available:
            print("Movie is already rented.")
            return

        movie.rent_movie()
        customer.rent_movie(movie)

        rental = Rental(customer, movie, days)
        self.rentals.append(rental)

        print(rental.receipt())

    # Return a movie
    def return_movie(self, customer_id, movie_id):
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)

        if customer and movie:
            movie.return_movie()
            customer.return_movie(movie)

            for rental in self.rentals:
                if rental.customer == customer and rental.movie == movie:
                    self.rentals.remove(rental)
                    break

            print("Movie returned successfully.")

    # Show all movies
    def show_movies(self):
        for movie in self.movies.values():
            print(movie)

    # Show all customers
    def show_customers(self):
        for customer in self.customers.values():
            print(customer)

    # Show all rentals
    def show_rentals(self):
        for rental in self.rentals:
            print(rental)
