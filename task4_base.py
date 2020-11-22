QUEUE_SIZE = 10
QUEUE = []


def menu():
    print('Choice:');
    print('1. Add customer');
    print('2. Remove customer');
    print('3. Exit');

def main():    
	C_NUMBER = 0
	choice = 0
	while choice != 3:
		menu()
		choice = (int)(input('> '))
		if choice == 1:
			# Add a customer if possible
			if len(QUEUE) < 10:
				C_NUMBER += 1
				QUEUE.append(C_NUMBER)
				print(QUEUE)
			elif len(QUEUE) >= 10:
				print(QUEUE)
				print("The queue is full!")
		elif choice == 2:
			# Remove a customer from queue if possible
            # and print customer's number
			if len(QUEUE) > 0:
				QUEUE.pop(0)
				print(QUEUE)
			else:
				print("The queue is empty.")
main()
