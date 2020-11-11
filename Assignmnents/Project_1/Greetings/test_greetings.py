#! /usr/bin/env python3

"""
Unit Testing greetings.py
"""

__author__ = "Ethan Ruiz"


import unittest
from greetings import answer

class TestGreetings(unittest.TestCase):
	def test1_answer(self):
		input1 = 'heeey'
		self.assertEqual(answer(input1), 'heeeeeey')
	def test2_answer(self):
		input2 = 'heey'
		self.assertEqual(answer(input2), 'heeeey')
	def test3_answer(self):
		input3 = 'heeeeeeeeeey'
		self.assertEqual(answer(input3), "heeeeeeeeeeeeeeeeeeeey")


if __name__ == "__main__":
    unittest.main(verbosity=2)
