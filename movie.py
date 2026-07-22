class Movie:
    """Represents a movie in the store."""

    def __init__(self, movie_id: str, title: str, genre: str, price: float):
        self._movie_id = movie_id
        self._title = title
        self._genre = genre
        self._price = price
        self._available = True

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def title(self):
        return self._title

    @property
    def genre(self):
        return self._genre

    @property
    def price(self):
        return self._price

    @property
    def available(self):
        return self._available

    def rent_movie(self):
        if not self._available:
            raise ValueError("Movie is already rented.")
        self._available = False

    def return_movie(self):
        self._available = True

    def __str__(self):
        status = "Available" if self._available else "Rented"
        return f"{self.movie_id} | {self.title} | {self.genre} | €{self.price}/day | {status}"

    def __repr__(self):
        return f"Movie('{self.movie_id}','{self.title}','{self.genre}',{self.price})"
