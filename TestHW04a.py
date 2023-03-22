"""
@author: Suraj

HW 05a - Isolate External Dependencies
"""

import unittest
from unittest.mock import patch
import HW04a
from HW04a import getRepo
from HW04a import getCommit
from HW04a import my_brand
from unittest import mock

my_brand("HW05a-Isolate External Dependencies")


class TestApi(unittest.TestCase):
       
    @mock.patch('HW04a.getRepo')
    def test_mock_1(self,test1):
        test1.return_value="Success"
        result = HW04a.getRepo("https://api.github.com/users/richkempinski/repos")
        self.assertEqual(result,"Success")

    @mock.patch('HW04a.getCommit')
    def test_mock_2(self,test2):
        test2.return_value=2
        result = HW04a.getCommit('richkempinski','try_nbdev')
        self.assertEqual(result,2)


if __name__ == '__main__':
   unittest.main()
   
