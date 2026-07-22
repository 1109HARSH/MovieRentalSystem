from movie import Movie

class Person:
    def __init__(self, person_id, name):
        self._person_id = person_id
        self._name = name

    @property
    def person_id(self):
        return self._person_id

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"{self.person_id} - {self.name}"


class Customer(Person):
    def __init__(self, person_id, name):
        super().__init__(person_id, name)
        self._movies = []

    @property
    def movies(self):
        return self._movies    # Returns the list of rented movies

    def rent_movie(self, movie: Movie):
        self._movies.append(movie)        # Add a movie to the customer's rented movies

    def return_movie(self, movie: Movie):
        if movie in self._movies:
            self._movies.remove(movie)         # Remove a movie from the customer's rented movies
        else:
            print("Movie not found in customer's rented list.")

    def calculate_discount(self):
        return 0

    def membership(self):
        return "Regular"

    def __str__(self):
        return f"{self.person_id} | {self.name} | {self.membership()}"


class PremiumCustomer(Customer):
    def calculate_discount(self):
        return 0.20

    def membership(self):
        return "Premium"
