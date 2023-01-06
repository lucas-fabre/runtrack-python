def tapis(n):
	for i in range(n+1): 
		tapis="" 
		for j in range(n-i): tapis+="#" 
		tapis+=" " 
		for j in range(i): tapis+="#" 
		print("|" + tapis + "|") 
tapis(15)