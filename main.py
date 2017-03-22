from Grammar import *

cfg_str ="""\

	# Grammar
	S -> Statement
	S -> Question 
	S -> SBAR 
	SBAR -> WhP Statement Statement  

	Statement[NUM=?n] -> NP[NUM=?n, PER=?p] VP[NUM=?n, PER=?p, SUBCAT=nil] 

	Question -> WhP SQ 
	WhP -> WhNP | WhADVP
	WhNP -> WP | WDT Nominal 
	WhADVP -> WRB 
	SQ -> Auxiliary[NUM=?n, PER=?p] NP[NUM=?n, PER=?p] VP[NUM=pl, SUBCAT=nil]
	

	NP[NUM=pl] -> NP CC NP
	NP[NUM=?n, PER=?p] -> DT[NUM=?n] Nominal[NUM=?n] | Nominal[NUM=?n] | ProperNoun[NUM=?n, PER=?p] | Pronoun[NUM=?n, PER=?p] | AP NP[NUM=?n] | NP[NUM=?n] PP

	VP[NUM=?n, PER=?p, SUBCAT=?rest] -> VP[NUM=?n, PER=?p, SUBCAT=nil] CC VP[NUM=?n, PER=?p, SUBCAT=nil] 
	VP[NUM=?n, PER=?p, SUBCAT=?rest] -> VP[NUM=?n, PER=?p, SUBCAT=[HEAD=?arg, TAIL=?rest]] ARG[CAT=?arg]
	VP[NUM=?n, PER=?p, SUBCAT=?args] -> V[NUM=?n, PER=?p, SUBCAT=?args]
	VP[NUM=?n, PER=?p, SUBCAT=?args] -> RB VP[NUM=?n, PER=?p, SUBCAT=?args]

	AP -> RB JJ | JJ
	Nominal[NUM=?n] -> Nominal[NUM=?n] Noun[NUM=?n] | Noun[NUM=?n] 
	PP -> IN NP

	ARG[CAT=np] -> NP
	ARG[CAT=vp] -> VP
	ARG[CAT=pp] -> PP
	ARG[CAT=ap] -> AP
	ARG[CAT=st] -> Statement

	# Words

	V[NUM=sg, PER=3, SUBCAT=nil] -> 'barks' | 'laughs'
	V[NUM=sg, PER=3, SUBCAT=[HEAD=np, TAIL=[HEAD=pp, TAIL=nil]]] -> 'puts' 
	V[NUM=sg, PER=3, SUBCAT=[HEAD=np, TAIL=nil]] -> 'eats' | 'drinks'
	V[NUM=sg, PER=3, SUBCAT=[HEAD=np, TAIL=nil]] -> 'feeds'
	V[NUM=sg, PER=3, SUBCAT=[HEAD=np, TAIL=[HEAD=np, TAIL=nil]]] -> 'feeds'
	V[NUM=sg, PER=3, SUBCAT=[HEAD=st, TAIL=nil]] -> 'thinks'

 	V[TENSE=past] -> 'barked' | 'laughed' | 'ate' | 'fed' | 'thought' | 'drank' | 'did'
 	V[TENSE=prespart] -> 'barking' | 'laughing' | 'eating' | 'feeding' | 'thinking' | 'drinking' | 'doing'
 	V[NUM=pl] -> 'bark' | 'laugh' | 'eat' | 'feed' | 'think' | 'drink' | 'do'
 	Auxiliary[NUM=sg, PER=3] -> 'does'
 	Auxiliary[NUM=pl] -> 'do' | 'did'
 	ProperNoun[NUM=sg, PER=3] -> 'Gromit' | 'Wallace'
 	Pronoun[PER=1] -> 'I' | 'we'
 	Pronoun[PER=2] -> 'you'
 	Pronoun[NUM=sg, PER=3] -> 'he' | 'she' | 'it'
 	Pronoun[PER=3, NUM=pl] -> 'they' 
	Noun[NUM=sg] -> 'cheese' | 'water' | 'kitchen' | 'dinner'
	DT[NUM=sg] -> 'a' | 'an' 
	DT -> 'the' | 'my'
	IN -> 'in' | 'on' | 'at' | 'after' | 'when'
	JJ -> 'tasty' | 'soft' 
	CC -> 'and' | 'but' | 'or'
	RB -> 'seldom' | 'often'
	WRB -> 'when'
	WP -> 'what' 
	WDT -> 'what'
	"""

text = """\
Gromit barks
Gromit barked
Wallace and Gromit eat cheese
Wallace and Gromit ate cheese
Wallace feeds Gromit
Wallace seldom feeds Gromit cheese
Wallace thinks Gromit eats cheese and drinks water
Wallace often eats tasty soft cheese in the kitchen after dinner
when Gromit barks Wallace feeds Gromit
when does Wallace eat cheese
"""

to_test = """\
she and they eat
"""

invalid = """\
Gromit bark
when do Gromit eat cheese
Gromit barks the kitchen
"""

def main():
	print """\
	##############################################
	#                 Begin                      #
	##############################################
	"""
	g = Grammar(cfg_str)
	g.parse_and_print(text, False, False)
	g.parse_and_print(to_test, True)
	g.parse_and_print(invalid)

if __name__ == '__main__':
	main()