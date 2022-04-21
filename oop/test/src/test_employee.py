import unittest

from oop.src.employee import Employee

class TestEmployee(unittest.TestCase):
    def test_get_fullname(self):
        e=Employee("vera","V",0,None)
        self.assertEqual(e.get_fullname(),"Vera V")