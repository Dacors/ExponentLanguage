import re

alphabet = open("Language.txt")

exponent = 0

content = alphabet.read()

result = []
ls_1 = []
ls_2 = []
ls_3 = []
ls_4 = []
ls_5 = []

caracters = re.findall(r"[\w']+", content)

def calculate_language(language):

    caracters = re.findall(r"[\w']+", language)
    
    exponent = int(float(caracters[-1]))
    del caracters[0]
    del caracters[-1]
  
    if exponent < 1:
        return result
    else:
        
        for a in range(0,len(caracters)):
            ls_1.append(caracters[a]*exponent)

        for n in combinate(caracters, exponent):
            for b in perm_caracters(n):
                caracter = ""
                for c in range(0,len(b)):
                    caracter = caracter + b[c]

                if caracter in ls_3:
                    a = len(ls_3)
                else:
                    ls_3.append(caracter)
                
        ls_4.extend(ls_3)
            
    ls_1.extend(ls_4)
    return ls_1

def perm_caracters(caracters_for_build):
	if len(caracters_for_build) == 0:
		return ""
	elif len(caracters_for_build) == 1:
		return [caracters_for_build]
	else:
		result = []
		for i in range(len(caracters_for_build)):
			x = caracters_for_build[i]
			xs = caracters_for_build[:i] + caracters_for_build[i+1:]
			for p in perm_caracters(xs):
				result.append([x] + p)
		return result

def combinate(caracters, exponent):
    if exponent > len(caracters):
        exponent = len(caracters)
    return [s for s in pot(caracters) if len(s) == exponent]

def pot(c):
    if len(c) == 0:
        return [[]]
    r = pot(c[:-1])
    return r + [s + [c[-1]] for s in r]

# print(calculate_language(content))
for y in combinate(['a','b','c','d','e'],6):
    for g in range(0,len(y)):       
        y.append(y[g])
        print(y) #permutar
        y.remove(y[g])
        

