# Hash table size
HASH_TABLE_SIZE = 49999

def hashnum(number):
	return hash(number)%HASH_TABLE_SIZE
	
# Hash table class
class HashTable:

	# Initialize table object
	def __init__(self,size):
		self.table = [None]*size
		self.tablesize = size
		
	# Insert a number in the table
	# Use linear probing
	# Refer to table as self.table
	# and its size as self.tablesize
	# None is an empty slot in table
	# Return the index where stored and -1 if table full	
	def insert(self,number):
		index = number % self.tablesize
		if self.table[index] == None:
			self.table[index] = number
			return 0
		if index > self.tablesize:
			return -1 #-1 palautetaan jos hashtable on täysi
		
	# Search a number from the table
	# Assume linear probing used
	# Refer to table as self.table
	# and its size as self.tablesize
	# None is an empty slot in table
	# Return the index where stored and -1 if not found	
	def search(self,number):
		for i in range(len(self.table)): 
			if self.table[i] == number:
				return i
		return -1 #-1 palautetaan jos numeroa ei löydy


def main():
	# New hash table
	hashtab = HashTable(HASH_TABLE_SIZE) 

	file = open(r'C:\Users\Suturri\Desktop\tärkeät\TRA\tra5\task5_4_nums.txt')
	for line in file:
		hashtab.insert(int(line))
	
	
	searchnums = [613695,906429,180551,151841,951585,569127]
	
	for num in searchnums:
		if hashtab.search(num) >= 0:
			print(num, ' FOUND in table')
		else:
			print(num, ' NOT FOUND in table')
	
main()