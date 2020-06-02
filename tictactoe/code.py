for board in boardsx:
	board,sums=checkBoard(board, sums)
		if player_==X and board is not None and sums>mins:
			mins=sums
			NODE=board
		if player_==O and board is not None and sums<maxs:
			maxs=sums
			NODE=board


def checkBoard(boardc, sumsc):
	sums=copy.deepCopy(boardc)
	board=copy.deepCopy(boardc)
	boards.append(board)
	while len(boards)>0:
		boards2=list()
		for board in boards:
			actions_=actions(board)
			for action in actions_:
					board=result(board,action)
					if terminal(board):
						
						sums+=utility(board)
						if player_==X and sums<mins:
							return None, 0
						if player_==O and sums>maxs:
							return None, 0
					else:
						boards2.append(board)
	
		boards=boards2
	return(board,sums)
	
	