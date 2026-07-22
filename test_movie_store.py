import unittest
from movie import Movie
from person import Customer
from movie_store import MovieStore

class TestMovieStore(unittest.TestCase):

    def setUp(self):
        self.store = MovieStore()
        self.movie = Movie("M101", "Interstellar", "Sci-Fi", 5)
        self.customer = Customer("C101", "John")
        self.store.add_movie(self.movie)
        self.store.register_customer(self.customer)

    def test_add_movie(self):
        self.assertEqual(len(self.store.movies), 1)

    def test_register_customer(self):
        self.assertEqual(len(self.store.customers), 1)

    def test_rent_movie(self):
        self.store.rent_movie("C101", "M101", 3)
        self.assertFalse(self.movie.available)

    def test_return_movie(self):
        self.store.rent_movie("C101", "M101", 2)
        self.store.return_movie("C101", "M101")
        self.assertTrue(self.movie.available)

if __name__ == "__main__":
    unittest.main()