import random

game = ['rock', 'paper', 'scissors']

def generate_move():
    player1 = random.choice(game)       
    player2 = random.choice(game)
    move_set = [player1, player2]
    print('player 1\'s move:', player1)
    print('player 2\'s move:',player2)
    return move_set

def validity():
    decisions = generate_move()
    for j in range(len(decisions)):
        if decisions[j] == 'rock' or decisions[j] == 'paper' or decisions[j] == 'scissors':
            print('player', j+1, 'made a valid move')
        else:
            print('player', j+1, 'made an invalid move')
            break
    return decisions
    
def result():
    choices = validity()
    player1 = choices[0]        
    player2 = choices[1]
    if player1 == 'rock' and player2 == 'scissors':
        print('player 1 wins, rock smashes scissors')
        winner = 'player 1'
        return winner
    elif player1 == 'rock' and player2 == 'paper':
        print('player 2 wins, paper covers rock')
        winner = 'player 2'
        return winner
    elif player1 == 'paper' and player2 == 'rock':
        print('player 1 wins, paper covers rock')
        winner = 'player 1'
        return winner
    elif player1 == 'paper' and player2 == 'scissors':
        print('player 2 wins, scissors cut paper')
        winner = 'player 2'
        return winner
    elif player1 == 'scissors' and player2 == 'rock':
        print('player 2 wins, rock smashes scissors')
        winner = 'player 2'
        return winner
    elif player1 == 'scissors' and player2 == 'paper':
        print('player 1 wins, scissors cut papers')
        winner = 'player 1'
        return winner
    else:
        print(f"Both players selected {player1}. It's a tie!")
   
def score(game):
    point = result()
    if game == 0:
        global player1score
        global player2score
        player1score = 0
        player2score = 0    
        if point == 'player 1':
            player1score = player1score + 1
        elif point == 'player 2':
            player2score = player1score + 1
    elif game != 0 and point == 'player 1':
        player1score = player1score + 1
    elif game != 0 and point == 'player 2':
        player2score = player2score + 1
    print('player 1\'s score:',player1score)
    print('player 2\'s score:',player2score)

def rounds(n):
    for x in range(n):
        print('round #', x+1)
        score(x)
        print()
    
if __name__=='__main__':
    number = input('pick the number of rounds:')
    rounds(int(number))


        
