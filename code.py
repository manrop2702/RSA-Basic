import sys
arr = []
def diff(a, b):
	for i in range(len(a)):
		arr.append(ord(a[i])-ord(b[i]))
	print(arr)

inp1 = sys.argv[1]
inp2 = sys.argv[2]
diff(inp1, inp2)