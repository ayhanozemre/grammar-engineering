from Grammar import *

cfg_str ="""\

	# Grammar

	S -> NP[NUM=?n, PER=?p] VP[NUM=?n, PER=?p, SUBCAT=?s] 
	S -> NP[NUM=?n, PER=?p] RB VP[NUM=?n, PER=?p, SUBCAT=?s] 
	S -> Question[NUM=?n] 
	#S -> NP[NUM=?n, PER=?p] V[NUM=?n, PER=?p, SUBCAT=?s] S 
	S -> IN[SUBCAT=[HEAD=vp, TAIL=[HEAD=pp, TAIL=nil]]]
	#S -> IN NP[NUM=?n, PER=?p] VP[NUM=?n, PER=?p, SUBCAT=?s] NP[NUM=?n, PER=?p] VP[NUM=?n, PER=?p, SUBCAT=?s] 
	Question[NUM=?n] -> WhP Auxiliary[NUM=?n] NP[NUM=?n] VP[NUM=pl, SUBCAT=?s]
	WhP -> WRB
	NP[NUM=pl] -> NP[NUM=?n] CC NP[NUM=?n]
	NP[NUM=?n, PER=?p] -> DT[NUM=?n] Nominal[NUM=?n] | Nominal[NUM=?n] | ProperNoun[NUM=?n, PER=?p] | Pronoun[NUM=?n, PER=?p] | AP NP[NUM=?n] | NP[NUM=?n] PP

	# VP[NUM=?n, TENSE=?t, PER=?p] -> V[NUM=?n, TENSE=?t, PER=?p]
	#VP[NUM=?n, TENSE=?t, PER=?p] -> V[NUM=?n, TENSE=?t, PER=?p] NP NP 
	#VP[NUM=?n, TENSE=?t, PER=?p] -> V[NUM=?n, TENSE=?t, PER=?p] NP 
	VP[NUM=?n, TENSE=?t, PER=?p, SUBCAT=?rest] -> VP[NUM=?n, TENSE=?t, PER=?p, SUBCAT=?rest] CC VP[NUM=?n, TENSE=?t, PER=?p, SUBCAT=?rest] 
	#VP[NUM=?n, TENSE=?t, PER=?p] -> V[NUM=?n, TENSE=?t, PER=?p] PP  

	VP[NUM=?n, PER=?p, SUBCAT=?rest] -> VP[NUM=?n, PER=?p, SUBCAT=[HEAD=?arg, TAIL=?rest]] ARG[CAT=?arg]
	VP[NUM=?n, PER=?p, SUBCAT=?args] -> V[NUM=?n, PER=?p, SUBCAT=?args]
	AP -> RB JJ | JJ
	Nominal[NUM=?n] -> Nominal[NUM=?n] Noun[NUM=?n] | Noun[NUM=?n] 
	PP -> IN NP

	ARG[NUM=?n, PER=?p, CAT=np] -> NP
	ARG[NUM=?n, PER=?p, CAT=vp] -> VP
	ARG[NUM=?n, PER=?p, CAT=pp] -> PP
	ARG[NUM=?n, PER=?p, CAT=ap] -> AP

	# Words

	V[NUM=sg, PER=3, SUBCAT=nil] -> 'barks' | 'lauhgs'
	V[NUM=sg, PER=3, SUBCAT=[HEAD=np, TAIL=[HEAD=pp, TAIL=nil]]] -> 'puts' | 'eats' | 'drinks'
	V[NUM=sg, PER=3, SUBCAT=[HEAD=np, TAIL=[HEAD=np, TAIL=nil]]] -> 'feeds' | 'thinks'
	V[NUM=sg, PER=3, SUBCAT=[HEAD=np, TAIL=[HEAD=vp, TAIL=nil]]] -> 'thinks'
	
	# V[NUM=sg, PER=3] -> 'barks' | 'laughs' | 'eats' | 'feeds' | 'thinks' | 'drinks' | 'does'
 	V[TENSE=past] -> 'barked' | 'laughed' | 'ate' | 'fed' | 'thought' | 'drank' | 'did'
 	V[TENSE=prespart] -> 'barking' | 'laughing' | 'eating' | 'feeding' | 'thinking' | 'drinking' | 'doing'
 	V[NUM=pl, CAT=trans] -> 'bark' | 'laugh' | 'eat' | 'feed' | 'think' | 'drink' | 'do'
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

to_test = 
"""when Gromit barks Wallace feeds Gromit"""

invalid = """\
Gromit bark
when do Gromit eat cheese
Gromit barks the kitchen
"""

def main():
	print """\
	##############################################
	#         Begin                              #
	##############################################
	"""
	g = Grammar(cfg_str)
	g.parse_and_print(to_test, True)
	#g.parse_and_print(invalid)

if __name__ == '__main__':
	main()