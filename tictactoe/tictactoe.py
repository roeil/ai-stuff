"""
Tic Tac Toe Player
"""

import math,  copy, pickle
from util import Node, StackFrontier, QueueFrontier
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count=0
    o_count=0
    for r in range(3):
        for c in range(3):
            if board[r][c]==X:
                x_count+=1
            elif board[r][c]==O:
                o_count+=1
    if x_count==o_count:
        return(X)
    else:
        return(O)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    tups=set()
    for r in range(3):
        for c in range(3):
            if board[r][c] is None:
                tups.update([(r,c)])
    
    if len(tups)>0:# and winner(board) is None:
        print("TUPS:",tups)
        return(tups)
    else:
        print("NOhkkkkkkkkkkkkkkkkkkkkkkkkkkkkkgjNE")
        return(None)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardc=copy.deepcopy(board)
    #print("boardc:",boardc,"\t",action)
    player_= player(boardc)
    boardc[action[0]][action[1]]=player_
    return(boardc)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    if board[0]==[X,X,X] or board[1]==[X,X,X] or board[2]==[X,X,X] or ((board[0][0]==board[1][0] and board[0][0]==board[2][0]) and board[0][0]==X) or \
    ((board[0][1]==board[1][1] and board[0][1]==board[2][1]) and board[0][1]==X) or ((board[0][2]==board[1][2] and board[0][2]==board[2][2]) and board[0][2]==X) or \
    ((board[0][0]==board[1][1] and board[1][1]==board[2][2]) and board[2][2]==X) or ((board[0][2]==board[1][1] and board[1][1]==board[2][0]) and board[2][0]==X):
      win=X
    elif board[0]==[O,O,O] or board[1]==[O,O,O] or board[2]==[O,O,O] or ((board[0][0]==board[1][0] and board[0][0]==board[2][0]) and board[0][0]==O) or \
    ((board[0][1]==board[1][1] and board[0][1]==board[2][1]) and board[0][1]==O) or ((board[0][2]==board[1][2] and board[0][2]==board[2][2]) and board[0][2]==O) or \
    ((board[0][0]==board[1][1] and board[1][1]==board[2][2]) and board[2][2]==O) or ((board[0][2]==board[1][1] and board[1][1]==board[2][0]) and board[2][0]==O):
      win=O
    else:
        win=None
         
         
    return(win)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty=0
    for r in range(3):
        
        for c in range(3):
            if board[r][c] is None:
                empty+=1
    if empty>0 and winner(board) is None:
        return(False)
    else:
        return(True)
            
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win=winner(board)
    if win==X:
        return(-1)
    elif win==O:
        return(1)
    else:
        return(0)



        
        
def checkBoard(boardc, sumsc, mins, maxs, player_):
    sums=sumsc#copy.deepcopy(sumsc)
    board=copy.deepcopy(boardc)
    boards=list()
    boards.append(board)
    print("checkboardr iter\n", board)
    
    while len(boards)>0:
        boards2=list()
        for board in boards:
            actions_=actions(board)
            for action in actions_:
                print("action:",action)
                boardx=result(board,action)
                if terminal(boardx):
                    print("BEFORE: util:",utility(boardx),"\tsums:",sums, "mins:",mins)
                    sums=utility(boardx)
                    print("AFTER: util:",utility(boardx),"\tsums:",sums, "mins:",mins)
                    if player_==X and sums<=-1:
                        return None, 0
                    if player_==O and sums>maxs:
                        return None, 0
               
                else:
                    boards2.append(boardx)
        print("boards2:",boards2)
        boards=boards2
    print("board----------{},\tsums:-------{}".format(boardc,sums))
    return(boardc,sums)
	
       
        

def min_(board):
    boardc=board.copy()
    actstore=None
    mins=math.inf
    if terminal(board):
        return(utility(board),0)
        
    actions_=actions(boardc)
    if actions_ is not None:
        for action in actions_:
            
            boardc=result(board,action)
          
            m, blnk=max_(boardc)
            
            if m <mins:
                mins=m
                actstore=action
                
    
    return mins, actstore


def max_(board):
    actstore=None
    maxs=-math.inf
    boardc=board.copy()
    if terminal(board):
        return(utility(board), 0)
        
    actions_=actions(boardc)
    if actions_ is not None:
        for action in actions_:
            
            boardc=result(board,action)
            
            #print("mmmmmmmm",m)
            m, blnk=min_(boardc)
            
            if m >maxs:
                maxs=m
                actstore=action
        
    
    return maxs, actstore

    

        
        
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
#    boardCopy=copy.deepcopy(board)
#    maxs = math.inf; mins = -math.inf
    player_=player(board)
    m=[]
    actions_=actions(board)
    
    #for action in actions_:
    if player_==X:
        # m.append(max_(board, action))
        m, actstore = min_(board)
    else:
        m, actstore = max_(board)
            #m.append(min_(board, action))
            #print("ACTSTORE:",actstore)
    
#    print(m)
#    actions_=list(actions_)
#    if player_==X:
#        actstore=actions_[m.index(max(m))]
#    
#    if player_==O:
#        actstore=actions_[m.index(min(m))]
    
    return actstore
##    if player_==X:
##        sums=mins
##    else:
##        sums=maxs
#    sums=0
#    boards=list()
#    boards.append(board.copy())
#    qfTerm=QueueFrontier()
#    
#    qf=QueueFrontier()
#    term=False
#    
#    l=1
#    actions_ = actions(board)
#    
#    
#    qfx=QueueFrontier()
#    
#    boardsx=list()
#    
#    for action in actions_:
#        res=result(board,action)
#        qfx.add(Node(res, board, action))
#        print("board:{},action:{},parent:{}".format(res,action,board))
#        boardsx.append(res)
#    
#    
#    for boardx in boardsx:
#        print("check!")
#        board_,sums=checkBoard(boardx, sums, mins, maxs, player_)
#        
#        if (player_==X and board_ is not None) and (sums>mins):
#            mins=sums
#            NODE=board_
#            print("NODEX**************", NODE)
#                 
#                 
#        if (player_==O and board_ is not None) and (sums<maxs):
#            maxs=sums
#            NODE=board_
#            print("NODEO*********",NODE)
#   
#    for node in qfx.frontier:
#        if NODE==node.state:
#            action=node.action
#           
#
#
#    
#    
#    
##    
##    
##    
##    
##    
##    while len(boards)>0 and(mins<1 or maxs>-1):
##        print("WHILELOOP",mins)
##        boards2=list()
##        
##        for board_ in boards:
##            qf3l=list()    
##            actions_= actions(board_)
##
##            #player_=player(board_)
##            if actions_ is not None and l==1:
##                   for action in actions_:
##                           
##                           print(board_,"board_")        
##                           print(board_,":\t",actions_)
##                           board=result(board_,action) #board=result(board_.copy(),action)
##                           print(board,":AFTER\t",actions_)
##                           boards2.append(board)
##                           if terminal(board):
##                               term=True# is not None:
##                               print('TERMINAL','\t:',utility(board))
##                               u=utility(board)
##                               
##                               qfTerm.add(Node(board,board_,u))
##                               if player_==X:
##                                   print("X")
##                                   if u>mins:
##                                       print("TRUE;",u,"\t",mins)
##                                       NODEx=Node(board,board_,u)
##                                       qf3l.append(u)
##                                   else:
##                                       #boards2=boards2[:len(boards2)-1]
##                                       print("FLASE;",u,"\t",mins)
##                                       term=False
##                                       break;
##                               elif player_==O:
##                                   print("O")
##                                   if u<maxs:
##                                       print("TRUEO;",u,"\t",mins)
##                                       NODEx=Node(board,board_,u)
##                                       qf3l.append(u)
##                                   else:
##                                       #boards2=boards2[:len(boards2)-1]
##                                       print("FLASEO;",u,"\t",mins)
##                                       term=False
##                                       break;
##                           else:
##                               
##                               qf.add(Node(board,board_,action))
##        #print(boards2)
##                   
##                   
##                   print("OUT",term)
##                   
##                   if term:
##                       if player_==X:
##                           print("IN1")
##                           print(qf3l)
##                           if min(qf3l)>mins:
##                               mins=min(qf3l)
##                               #NODE=Node(board,board_,action)
##                               NODE=NODEx
##                               print("NOde:",board,"\t",board_,"\t",action,":",player_)
##                       if player_==O:   
##                           print("IN1O")
##                           if max(qf3l)<maxs:
##                               maxs=max(qf3l)
##                               #NODE=Node(board,board_,action)
##                               NODE=NODEx
##                               print("NOde:",board,"\t",board_,"\t",action,":",player_)
##                       term=False
##                   if mins==1 or maxs==-1:
##                       break
##        boards=boards2
##
##
##
##
##    termSet=QueueFrontier()
##
##    print(termSet.frontier,"termset-----------------")
##
##    #termSet.frontier.reverse()       
##    maxs = math.inf; mins = -math.inf
###    termSet=set()
###    for node in qfTerm.frontier:
###        termSet.add(node.parent)
##    
##    qf3l=list()
##    lst2=list()
##    l=1
###    print("**********************",qfTerm.frontier)
###    for par in qf.frontier:
###        print("qf:\t",par.state,"\t",par.parent,"\t",par.action)
##    #for par in termSet.frontier:
##    #for node in qfTerm.frontier
##    
###    with open('qfTerm.pkl', 'wb') as output:
###    
###        pickle.dump(qfTerm, output, pickle.HIGHEST_PROTOCOL)
###    with open('qfTerm.pkl', 'rb') as input:
###        qfTerm = pickle.load(input)
###    
##
##
##
##
##
##
##
##
##
##
##
##
###
###    for i in range(len(qfTerm.frontier)-1):
###        print("i:\t",i,"\t",qfTerm.frontier[i].parent,"\t",qfTerm.frontier[i+1].parent)
###        if l==1 and qfTerm.frontier[i].parent==qfTerm.frontier[i+1].parent:
###            if qfTerm.frontier[i].action>mins and player_==X:
###                print("append X")
###                qf3l.append(qfTerm.frontier[i].action)
###            elif qfTerm.frontier[i].action<maxs and player_==O:
###                qf3l.append(qfTerm.frontier[i].action)
###                print("append O")
###            else:
###                l*=-1
###                continue;
###        else:
###            #qf3l.append(qfTerm.frontier[i+1].action)
###            if qfTerm.frontier[i].parent!=qfTerm.frontier[i+1].parent:
###                
###                if i>1:
###                    if l==1 and player_==X and min(qf3l)>mins:
###                        NODE=qfTerm.frontier[i]
###                    elif l==1 and player_==O and max(qf3l)<maxs:
###                        NODE=qfTerm.frontier[i]
###                    print(l)
###                    qf3l=list()
###                    l*=-1
###                
###                    
###        
###        
###        
##        
##        
##        
##        
##        
##        
##        
###                                                    
###                                                    
###                                                    
###                                                    
###                                                    
###                                                    
###                                                    
###                                                    
###                                                    if not termSet.contains_state(node.parent):
###                                                        
###                                                        print('added')
###                                                        termSet.add(node)
###                                            
###                                            
###                                                        #print(termSet.frontier[0].parent)
###                                                        #print(par.parent)
###                                                        #print("**********************",par.state)
###                                                        qf3=QueueFrontier()
###                                                        
###                                                        #for node in qfTerm.frontier:
###                                                         #   print(node.state,"###############",node.parent,"\t",node.action)
###                                                        for node2 in qfTerm.frontier:
###                                                        #for node in qf.frontier:
###                                                            #print(node.state,"###############",node.parent,"\t",node.action)
###                                                            if node.state==node2.parent:
###                                                                #print('FOUND!!!!!')
###                                                                if player_==X:
###                                                                    if node.action<mins:
###                                                                        qf3l=list()
###                                                                        break;
###                                                                    else:
###                                                                        qf3.add(node) 
###                                                                        qf3l.append(node.action)
###                                                                elif player_==O:
###                                                                    if node.action>maxs:
###                                                                        qf3l=list()
###                                                                        break;
###                                                                    else:
###                                                                        qf3.add(node) 
###                                                                        qf3l.append(node.action)
###                                                        
###                                                    #qf3l2=qf3l
###                                                    if len(qf3l)>0: 
###                                                        #print(qf3l)
###                                                        iminsqf=qf3l.index(min(qf3l))
###                                                        
###                                                        minsqf=min(qf3l)
###                                                        imaxsqf=qf3l.index(max(qf3l))
###                                                        maxsqf=max(qf3l)
###                                                        
###                                                        
###                                                        if minsqf>mins and player_==X:
###                                                            print("212 LINE 212")
###                                                            mins=minsqf
###                                                            NODE=qf3.frontier[iminsqf]
###                                                        elif maxsqf<maxs and player_==O:
###                                                            maxs=maxsqf
###                                                            NODE=qf3.frontier[imaxsqf]
###                                            
###                                                
##    #for node in qf3.frontier:
##        #print("line222:\t",node.parent,"\t",node.state)
##    print("NODENDOENDOEDNOE\t", NODE.parent,"NODENODNODENOE",NODE.state,":",NODE.action, "BoardCopy:",boardCopy)        
##    parent=NODE.parent
##    #print(NODE.parent,"\t",NODE.state)
##    #print(NODE.parent,"**********************NODENODNEODNEODE",NODE.state,"\t") 
##    while parent !=boardCopy:
##        for node in qf.frontier:
##            if node.state==parent:
##                
##    #            print(node.parent, "\t",parent,"\t",node.state, "\t",boardCopy) 
##                parent=node.parent
##                action=node.action
##                break;
##               
##
##    
##                
##              
#    print("minimax board:{}, minimax action:{}".format(NODE,action)) 
#    return(action)
#
##def checkBoard(boardc, sumsc, mins, maxs, player_):
##    sums=copy.deepcopy(sumsc)
##    board=copy.deepcopy(boardc)
##    boards=list()
##    boards.append(board)
##    term=terminal(board)
##
##    
###
###    if terminal(board):
###        print("util:",utility(board),"\tsums:",sums)
###        sums+=utility(board)
###        print("AFTER: util:",utility(board),"\tsums:",sums)
###        if player_==X and sums<mins:
###            return None, 0
###        if player_==O and sums>maxs:
###            return None, 0
###        return(board,sums)
###    else:
###        
###
###    
###    
##    
##    while len(boards)>0:
##        boards2=list()
##        for board in boards:
##            actions_=actions(board)
##            for action in actions_:
##                board=result(board,action)
##                if terminal(board):
##                    print("util:",utility(board),"\tsums:",sums)
##                    sums+=utility(board)
##                    print("AFTER: util:",utility(board),"\tsums:",sums)
##                    if player_==X and sums<mins:
##                        return None, 0
##                    if player_==O and sums>maxs:
##                        return None, 0
##                else:
##                    boards2.append(board)
##        boards=boards2
##    print("sums:",sums)
##    return(board,sums)
##	
##
##    
#    
##    
##    
##def same(board1,board2):
##    c=0
##    for i in range(3):
##        for j in range(3):
##            
##            if board1[i][j]==board2[i][j]:
##                c+=1
##    print(c)
##    return(c)
##    