import unittest
from .models import movie
Movie = movie.Movie

class MovieTest(unittestst.TestCase):
    def setUp(self):
        self.new_movie = Movie(1234, "Python must be crazy","Ancient pythoneers",
        "https://image.tmdb.org/t/p/w500/khsjha27hbs",8.5,129993)

    def test_inctance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

if __name__ == '__main__':
    unittest.main()
