def multiplication(a,b):
	re = a
	if b >= 0:
		for i in range(b-1):
			re += a
	if b <= 0:
		for i in range(b-1,0):
			re -= a
	return re
			
assert multiplication(3,5) == 15
assert multiplication(-4,-8) == 32
assert multiplication(-2,6) == -12
assert multiplication(-2,0) == 0
assert multiplication(0,0) == 0
assert multiplication(1,0) == 0
assert multiplication(0,1) == 0
assert multiplication(1,1) == 1
assert multiplication(-1,-1) == 1
assert multiplication(-1,5) == -5



def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1
    return False
    
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) == False
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31,33,33,33,33,69],True) == False
