import random
import time
import os

def fn(a):
	return 2*a

def main():
	try: 
		while True:
			print(chr(random.randint(60,88)))
			time.sleep(0.033)
			os.system('cls');
			
	except KeyboardInterrupt:
		print('Adiós')
		
if __name__ == '__main__':
	main()
	