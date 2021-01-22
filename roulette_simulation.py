from random import randrange
import matplotlib.pyplot as plt
import numpy as np


winnings = []
wins = 0
losses = 0
total_wins =0 
total_loss = 0

#simulating 10k seperate sittings of 60 plays(spins) each

for i in range(10000):

	pot = 1500
	current_bet = 15
	
	#one sitting, 60 plays
	for i in range(60):
		
		if pot <= 0:
			break
		
		roll = randrange(1,38)
		if roll >= 1 and roll <= 18:
			#YOU WON
			won = current_bet * 2
			#ADD TO POT
			pot = pot + won
			
			#NEXT BET
			if current_bet > 15:
				#decrease bet 
				current_bet = current_bet - 15 
		
			total_wins = total_wins + 1
				
				
			#roll is red
			
		
		elif roll >=19 and roll  <= 38:
			#YOU LOST
			loss = current_bet
			#DEDUCT FROM POT
			pot = pot - loss
			
			#NEXT BET
			current_bet = current_bet + 15 
			
			#roll is black
			total_loss = total_loss +1 
		
	winnings.append(pot)
	if pot >= 1500:
		wins = wins + 1
		
	else:
		losses = losses + 1
	
	
#print(winnings)
# plt.hist(winnings,bins=50)
# plt.show()

print(total_loss/total_wins)
print(total_loss)
print(total_wins)




