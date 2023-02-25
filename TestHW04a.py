"""
Created on Fri Feb 22 19:56:09 2023

@author: Suraj

Homework: 04a - Develop with the Perspective of the Tester in mind
"""

import unittest
from unittest.mock import patch
from HW04a import getRepo
from HW04a import getCommit
from HW04a import my_brand
my_brand("HW04a-Develop-with-the-Perspective-of-the-Tester-in-mind")


class TestApi(unittest.TestCase):
    @patch('HW04a.requests.get')
    

#Testing Valid user name :
    
    def testValidUser(self,mock):
        self.assertEqual(getRepo('https://api.github.com/users/richkempinski/repos'), 'Success')
       
#Testing number of commits within repository :
    
    def testCommits(self):
        user = 'richkempinski'
        name = 'try_nbdev'
        self.assertEqual(getCommit(user,name),2)
       

if __name__ == '__main__':
   unittest.main()
