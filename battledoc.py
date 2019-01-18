import time
import random

print()
print('-' * 55)
print()

print('A wild Wartortle appears!')
time.sleep(0.5)
print('... the background music changes...')
time.sleep(0.5)
print('You only have one pokemon, Leekbird!')
time.sleep(0.5)
print('I choose you Leekbird !!!')
time.sleep(0.5)
print()





# set the starting health values 
leekbird_hp = 150
wartortle_hp = 170

# display the correct health 
print('starting HP:')
time.sleep(0.3)
print('leekbird_hp:' + str(leekbird_hp))
time.sleep(0.3)
print('wartortle_hp:' + str(wartortle_hp))
time.sleep(0.3)
print()

# this is the battle loop, it continues as long as one pokemon 	
while leekbird_hp > 0 and wartortle_hp >0:
	print('Choose your battle move:')
	time.sleep(0.3)
	print('- [1] Tackle')
	time.sleep(0.3)
	print('- [2] Super Screech')
	time.sleep(0.3)
	print('- [3] Eat Leek')
	time.sleep(0.3)
	print('- [4] Falon attack')
	time.sleep(0.3)
	print('- [5] Capture')
	time.sleep(0.3)
	print()

	player_move = input('Pick a move using the corresponding number:')
	player_move = int(player_move)

	if player_move == 1:
		wartortle_hp = wartortle_hp - 25
		print('Leekbird uses Tackle and deals 25 HP of damage')
	elif player_move == 2:
		damage = random.randint(5,40)
		wartortle_hp = wartortle_hp - damage
		print('Leekbird uses Super Screech and deals' + str(damage) + 'HP of damage')
	elif player_move == 3:
		leekbird_hp = leekbird_hp + 100
		print('Leekbird uses Eat Leek and recovers 100 HP.')
	elif player_move == 5:
		capture_roll = random.randint(0,170)
		if capture_roll > wartortle_hp:
			print('You have captured Wartortle!')
			break
		else:
			print('You have tried to capture Wartortle but failed')
		

		time.sleep(0.3)
		print()

		# enemy battle choices
	enemy_move = random.randint(1,2)
	if enemy_move ==1:
		leekbird_hp = leekbird_hp - 30
		print('Wartortle uses water blast and deals 30 HP of damage')
	elif enemy_move ==2:
		leekbird_hp = leekbird_hp - 20
		wartortle_hp = wartortle_hp + 20
		print('Wartortle uses Drink Blood and deals 20 HP of damage while also recovering 20 HP')

		time.sleep(0.3)
		print()

	# display the current health s
		print('Updated HP:')
		time.sleep(0.3)
		print('leekbird_hp:' + str(leekbird_hp))
		time.sleep(0.3)
		print('wartortle_hp:' + str(wartortle_hp))
		time.sleep(0.3)
		print()

#who won!

	





















