import random

import unittest


class Unittest(unittest.TestCase):

    def setUp(self):

        '''Sets up the initial board'''
        self.board = board('The board')

    def Teardown(self):

        '''Takes the initial board down'''
        self.board = dispose()
        self.board = None

    def board(self):

        '''Checks that that the board size is not 0'''
        self.bdsize = 8
        self.board = [['  ' for item in range(self.bdsize)]for items in range(self.bdsize)]
        self.assertIsNotNone(self.board, ' Has 8 sublists')

    def boardzize(self):
        '''Checks the input of the board size'''
        self.name = raw_input("Enter your name: ")
        self.boardsize = raw_input("Please enter the boardsize: ")
        self.assertIs(int(self.boardsize), int, 'Valid board size')

    def shipsize(self):

        '''Checks the input of the shipsize'''
        self.ship_size = raw_input("Please enter the ship size: ")
        self.assertIs(int(self.ship_size), int, 'Valid ship size')

    def cordx(self):

        '''Checks the input for cordinate x'''
        self.cordx = raw_input("Please enter the x cordinate: ")
        self.assertIs(int(self.cordx), int, 'Valid x cordinate')

    def cordy(self):

        '''Checcs the input for the cordinate y'''
        self.cordy = raw_input("Please enter the y cordinate: ")
        self.assertIs(int(self.cordy), int, 'Valid y cordinate')

    def randomchoice(self):

        '''Checks to see if it takes a random integer from a list'''
        self.randomlst = [1, 8, 9, 4, 7, 2, 3, 54, 6, 9]
        self.randomint = random.choose(self.randomlst)
        self.assertisinstance(self.randomint, int, 'A random integer from the list')

    def hitchecker(self):

        '''Check to see if the cordinate have been marked with 'X'''
        self.board[self.cordy][self.cordx] = ' X'
        self.assertEqual(self.board[self.cordy][self.cordx], ' X', 'Marked with X')

if __name__ == '__main__':
    unittest.main()
