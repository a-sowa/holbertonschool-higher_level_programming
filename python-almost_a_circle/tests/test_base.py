#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """
    A class to test the Base Class
    """

    def test_id_as_positive(self):
        """
        Test for a positive Base Class id
        """
        base_instance = Base(115)
        self.assertEqual(base_instance.id, 115)
        base_instance = Base(67)
        self.assertEqual(base_instance.id, 67)

    def test_id_as_negative(self):
        """
        Test for a negative Base Class id
        """
        base_instance = Base(-91)
        self.assertEqual(base_instance.id, -91)
        base_instance = Base(-4)
        self.assertEqual(base_instance.id, -4)

    def test_id_as_none(self):
        """
        Test for a None Base Class id
        """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        base_instance = Base('Monty Python')
        self.assertEqual(base_instance.id, 'Monty Python')
        base_instance = Base('Python is cool')
        self.assertEqual(base_instance.id, 'Python is cool')

    def test_empty_to_json_string(self):
        """
        Test for a empty data on the to_json_string method
        """
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

    def test_instance(self):
        """
        Test a Base Class instance
        """
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_to_json_string(self):
        """
        Test a normal to_json_string functionality
        """
        rect_data = {'id': 31, 'x': 14, 'y': 11, 'width': 3, 'height': 3}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{["id": 31, "x": 14, "y": 11, "width": 3, "height": 3]}'
        )

    def test_wrong_save_to_file(self):
        """
        Test the save_to_file method
        """
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'",
             str(msg.exception)
        )
