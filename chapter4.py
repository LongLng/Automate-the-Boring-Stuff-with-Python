import random

#Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats']
def comma_code(list):
    print( f'{", ".join(list[:-1])}, and {list[-1]}')
    
#Coin Flip Streaks
def coin_flip():
	numberOfStreaks = 0
	coinFlip = []
	check = 0
	for experimentNumber in range(10000):
		for i in range(1000):
			coinFlip.append(random.randint(0,1))
		for j in range(len(coinFlip)):
			if j==0:
				pass
			elif coinFlip[j] == coinFlip[j-1]:
				check +=1
			else:
				check = 0
			if check == 6:
				numberOfStreaks += 1
	print('Chance of streak: %s%%' % (numberOfStreaks / 100))
 
#Character Picture Grid
def character_picture():
    grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
    
    for i in range(len(grid[0])):
        print('')
        for j in range(len(grid)):
            print(grid[j][i], end='')
        

if __name__=='__main__':
    character_picture()