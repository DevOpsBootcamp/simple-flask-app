#!/usr/bin/env python
import unittest
import script

class TinsyAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = script.app.test_client()

    def test_main_page(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(b"<img src=/static/x.gif></img>" in rv.data)

    def test_user_page(self):
        rv = self.app.get('/user/dave')
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(b"<img src=/static/hal.jpg></img>" in rv.data)
        self.assertTrue(b"I'm sorry, dave but I can't do that for you."\
                        in rv.data)

    def test_dogs_page(self):
        rv = self.app.get('/dogs/')
        # Add Your Test Code Here
        self.assertTrue(True)  # Remove this test

unittest.main()
