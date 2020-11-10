#! /usr/bin/env python3

"""
Unit Testing quiteaproblem.py
"""

__author__ = "Ethan Ruiz"


import unittest
from quiteaproblem import answer

class TestGreetings(unittest.TestCase):
	def test1_answer(self):
		input1 = 'probably we will figure out when to solve the equation'
		self.assertEqual(answer(input1), 'no')
	def test2_answer(self):
		input2 = 'the issue will consist of when we find the error in the system'
		self.assertEqual(answer(input2), 'no')
	def test3_answer(self):
		input3 = 'probably I will think of a way to solve the question I have'
		self.assertEqual(answer(input3), "no")
	def test4_answer(self):
		input4 = 'hearing about problims make me think about other solutions'
		self.assertEqual(answer(input4), "no")


if __name__ == "__main__":
    unittest.main(verbosity=2)
