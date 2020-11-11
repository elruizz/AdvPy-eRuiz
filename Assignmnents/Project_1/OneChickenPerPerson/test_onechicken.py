#! /usr/bin/env python3

"""
Unit Testing onechicken.py
"""

__author__ = "Ethan Ruiz"


import unittest
from onechicken import answer

class TestGreetings(unittest.TestCase):
	def test1_answer(self):
		self.assertEqual(answer(40, 500), 'Dr. Chaz will have 460 pieces of chicken left over!')
	def test2_answer(self):
		self.assertEqual(answer(10, 11), 'Dr. Chaz will have 1 piece of chicken left over!')
	def test3_answer(self):
		self.assertEqual(answer(15, 1), 'Dr. Chaz needs 14 more pieces of chicken!')


if __name__ == "__main__":
    unittest.main(verbosity=2)
