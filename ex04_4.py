import random

coin = [3]*3
tail = 0
head = 0

print("Who are you?")
name = input()
print("Hello,"+str(name)+"!")
print("Tossing a coin...")
for times in range(3) :
	coin = random.randint(1, 1000)
	if ( coin % 2 == 0 ) :
		print("Round "+str(times)+":Head")
		head += 1
	else : 
		print("Round "+str(times)+":Tail")
		tail += 1
print("Heads: "+str(head)+", Tails: "+str(tail))
if ( head > tail ) : print(name+" won")
else : print(name+" lost")