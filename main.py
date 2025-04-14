import random

def bet_money(start_money):
    bet_money = 0
    while True:
        bet_money = int(input("Enter your bet: "))
        if bet_money > start_money:
            print("You don't have enough money!")
        else:
            break
    return bet_money

def game_engine():
    print(" Game Tài or Xỉu ")
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum_of_dice = dice_1 + dice_2
    guess = int(input('\tPress 1 if you choose tài, 2 if xỉu, 3 if you want to triple the bet (sum of dice equal 5): '))
    lost = False
    super_win = False
    if guess == 1 and sum_of_dice > 5:
        print("You win!")
    elif guess == 2 and sum_of_dice < 5:
        print("You win!")
    elif guess == 3 and sum_of_dice == 5:
        print("You win!")
        super_win = True
    else:
        lost = True
    return lost, super_win
if __name__ == '__main__':
    start_money = 100000
    num_win = 0
    while True:
        bet_money = bet_money(start_money)
        lost, super_win = game_engine()
        if lost:
            start_money -= bet_money
            print("You lost!")
            print(f"Your current balance: {start_money}")
        else:
            num_win += 1
            if super_win:
                start_money += bet_money*3
            else:
                start_money += bet_money
            print(f"Your current balance: {start_money}")
            print(f"You won {num_win} times")
        if start_money <= 0:
            print("You lost all your money!")
            break
        print('Do you want to play again? (y/n)')
        answer = input()
        if answer != 'y':
            print(f"Your current balance: {start_money}")
            print(f"You won {num_win} times")
            break



