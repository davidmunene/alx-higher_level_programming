#!/usr/bin/python3
# 101-nqueens.py
"""Solves the N-queens puzzle. """
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's.
    """
    board = [['' for col in range(n)] for row in range(n)]
    return board
