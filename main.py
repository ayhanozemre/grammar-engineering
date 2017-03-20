from Grammar import *

cfg_str ="""\

	# Grammar

	S -> NP[NUM=?n, PER=?p] VP[NUM=?n, PER=?p] | NP[NUM=?n, PER=?p] RB VP[NUM=?n, PER=?p] | Question[NUM=?n] | NP[NUM=?n, PER=?p] V[NUM=?n, PER=?p] S | IN S 
	Question[NUM=?n] -> WhP Auxiliary[NUM=?n] NP[NUM=?n] VP
	WhP -> WRB
	NP[NUM=pl] -> NP[NUM=?n] CC NP[NUM=?n]
	NP[NUM=?n, PER=?p] -> DT[NUM=?n] Nominal[NUM=?n] | Nominal[NUM=?n] | ProperNoun[NUM=?n, PER=?p] | Pronoun[NUM=?n, PER=?p] | AP NP[NUM=?n] | NP[NUM=?n] PP
	VP[NUM=?n, TENSE=?t, PER=?p] -> V[NUM=?n, TENSE=?t, PER=?p]| V[NUM=?n, TENSE=?t, PER=?p] NP NP | V[NUM=?n, TENSE=?t, PER=?p] NP 
	VP[NUM=?n, TENSE=?t, PER=?p] -> VP[NUM=?n, TENSE=?t, PER=?p] CC VP[NUM=?n, TENSE=?t, PER=?p] | V[NUM=?n, TENSE=?t, PER=?p] PP  
	AP -> RB JJ | JJ
	Nominal[NUM=?n] -> Nominal[NUM=?n] Noun[NUM=?n] | Noun[NUM=?n] 
	PP -> IN NP

	ARG[CAT=np] -> NP
	ARG[CAT=vp] -> VP
	# Words

	V[NUM=sg, PER=3] -> 'barks' | 'laughs' | 'eats' | 'feeds' | 'thinks' | 'drinks' | 'does'
 	V[TENSE=past] -> 'barked' | 'laughed' | 'ate' | 'fed' | 'thought' | 'drank' | 'did'
 	V[TENSE=prespart] -> 'barking' | 'laughing' | 'eating' | 'feeding' | 'thinking' | 'drinking' | 'doing'
 	V[NUM=pl] -> 'bark' | 'laugh' | 'eat' | 'feed' | 'think' | 'drink' | 'do'
 	Auxiliary -> 'does' | 'do' | 'did'
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

invalid = """\
Gromit bark
when do Gromit eats cheese
Gromit barks the kitchen
"""

def main():
	g = Grammar(cfg_str)
	g.parse_and_print(text)
	g.parse_and_print(invalid, True)

if __name__ == '__main__':
	main()