import random

pc_choise = random.choice(['sang', 'kaqaz', 'qeychi'])

user_choice = input('Enter what you want rock, paper, or scissor: ')

def set_pc():
    return random.choice(['sang', 'kaqaz', 'qeychi'])

def normalize(user):
    ''' input var checked and normalized '''
    lis = ['sang', 'SANG', 'ROCK', 's']
    lis2 = ['kagaz', 'KAGAZ', 'PAPER', 'k']
    lis3 = ['scissor', 'SCISSOR', 'QEYCHI', 'qeychi', 'q']
    if user == 'rock' or lis:
        return 'sang'
    elif user == 'paper' or lis2:
        return 'kagaz'
    elif user == 'scissor' or lis3:
        return 'qeychi'
    else:
        return 'NOT'


user = normalize(user_choice)


def davari(user, pc):
    ''' check how is wining '''
    try:
        if pc == 'sang' and user == 'kaqaz':
            return 'user win'
        elif pc == 'sang' and user == 'qeychi':
            return 'user lose'

        elif pc == 'qeychi' and user == 'sang':
            return 'user win'
        elif pc == 'qeychi' and user == 'kaqaz':
            return 'user lose'
        elif pc == 'kaqaz' and user == 'sang':
            return 'user lose'
        elif pc == 'kaqaz' and user == 'qeychi':
            return 'user win'
        else:
            return 'BARA BAR'
    except ValueError:
        return 'give mee sang or qeychi or kaqaz'


winer_loser = davari(user=user, pc=pc_choise)
print(f'this is pc {pc_choise}')
print(winer_loser)
