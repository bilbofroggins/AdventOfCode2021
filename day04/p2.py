from math import sqrt
import re

f = open('input.txt')
lines = f.readlines()

# 24 75 59 41 17 5
# 58 74 64 92 39 5
# 68  8 78 85 72 5.      lowest = 5
# 18  3 22  4 34 5
# 11 76  6 28 50 5
# 5.  5. 5. 5. 5

class Board():
	def __init__(self):
		self.board = {}
		self.seen = set()
		self.col_totals = []
		self.row_totals = []
		self.lowest = None
		self.board_size = 0
		self.winner = False

	def add(self, r):
		self.board[r] = self.board_size
		self.board_size += 1

	def set_hashes(self):
		row_col_size = int(sqrt(self.board_size))
		self.col_totals = [row_col_size]*row_col_size
		self.row_totals = [row_col_size]*row_col_size
		self.lowest = row_col_size

	def update(self, called_number):
		if called_number in self.board and not self.winner:
			position = self.board[called_number]
			self.seen.add(position)

			row = position // int(sqrt(self.board_size))
			col = position % int(sqrt(self.board_size))

			self.row_totals[row] -= 1
			if self.row_totals[row] < self.lowest:
				self.lowest = self.row_totals[row]
			self.col_totals[col] -= 1
			if self.col_totals[col] < self.lowest:
				self.lowest = self.col_totals[col]

			if self.lowest == 0:
				self.win_sequence(int(called_number))

	def win_sequence(self, called_number):
		self.winner = True
		total = 0
		for i, num in enumerate(self.board.keys()):
			if i not in self.seen:
				total += int(num)

		print("win:", total * called_number)


called_numbers = lines[0].rstrip().split(',')
boards = []


i = 2
line = lines[i]

while i < len(lines):
	board = Board()
	while i < len(lines) and lines[i] != '\n':
		row = re.split('\s+', lines[i].strip())
		for r in row:
			board.add(r)
		i += 1

	i += 1
	board.set_hashes()
	boards.append(board)

for called_number in called_numbers:
	for board in boards:
		board.update(called_number)

