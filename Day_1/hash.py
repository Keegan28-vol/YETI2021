import hashlib
#create a list with all possible characters
charlist= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

#the variable OurHash holds the Md5 hex digest of the string we are trying to find
OurHash="4002f685108db38f1af9965f3bc869eb"

#iterate through all possibilities for the first, second, third, and fourth character (a,b,c,and d)
for a in range(62):	
	for b in range(62):
		for c in range(62):
			for d in range(62):
				#create a string for each possibility and then find the md5 hash as a hex digest
				str2hash = charlist[a] + charlist[b] +charlist[c] + charlist[d]
				result = hashlib.md5(str2hash.encode()).hexdigest()
				
				#if the resulting hash matches the one we are looking for, break out of all 4 for loops
				if result == OurHash:
					break
			if result == OurHash:
				break
		if result == OurHash:
			break
	if result == OurHash:
		break
		
#small error catch, if the user input a string that isn't within the parameters of the code, they get an error message
#if string is not 4 alphanumeric characters the variable string2hash will be 9999 and if the hash is not the hash of 9999, we know an error has occured
if str2hash =="9999" and OurHash != "fa246d0262c3925617b0c72bb20eeb1d":
	print("error: hash has a corresponding result that is outside the scope of this \n program. Either the string that produced this hash is longer than \n 4 characters, or it contains non-alphanumeric characters")	
else:

#print the string that gave us the correct hash	if no errors were detected
	print("The four character string with the hash "+ OurHash +" is: " + str2hash)