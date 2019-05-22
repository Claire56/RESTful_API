from unittest import TestCase
from server import app
from data_model import connect_to_db, db, example_data
from flask import session


class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_try_page(self):
        """Test the trial route ."""

        result = self.client.get("/try")
        self.assertIn(b"data", result.data)

    def commodity_page(self):
        """Test the commodity route ."""
    

        result = self.client.get("/commodity",query_string={"start_date": '2019-03-1',"end_date":'2019-7-1','commodity_type': 'gold'})
        self.assertIn(b"data", result.data)




class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    



if __name__ == "__main__":
    import unittest

    unittest.main()




