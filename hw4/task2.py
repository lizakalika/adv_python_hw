import argparse

def fibo(n):
	a = 0
	b = 1
	for x in range(n):
		a = b 
		b = a + b
	return a

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', type = int)
 
    return parser

if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    
    print(fibo(args.num))
