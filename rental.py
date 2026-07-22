class Rental:
    """Represents a movie rental."""

    def __init__(self, customer, movie, days):
        # Check if rental days are valid
        if days <= 0:
            raise ValueError("Rental days must be greater than 0.")

        # Store rental information
        self._customer = customer
        self._movie = movie
        self._days = days

    # Return the customer
    @property
    def customer(self):
        return self._customer

    # Return the movie
    @property
    def movie(self):
        return self._movie

    # Calculate total rental cost
    def calculate_cost(self):
        return self._movie.price * self._days

    # Print rental receipt
    def receipt(self):
        return (f"\nCustomer: {self._customer.name}"
            f"\nMovie: {self._movie.title}"
            f"\nDays: {self._days}"
            f"\nTotal Cost: €{self.calculate_cost():.2f}")

    def __str__(self):
        return f"{self._customer.name} rented {self._movie.title} for {self._days} day(s)"

    def __repr__(self):
        return f"Rental('{self._customer.name}', '{self._movie.title}', {self._days})"
