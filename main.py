from Grammar import *

cfg_str ="""\
	S -> NP VP | NP RB VP | Question | S CC S | NP V S | IN S 
	Question -> WhP Auxiliary NP VP
	WhP -> WRB
	NP -> NP CC NP | DT Nominal | Nominal | ProperNoun | AP NP | NP PP
	VP -> V | V NP NP | V NP | VP CC VP | V PP  
	AP -> RB JJ | JJ
	Nominal -> Nominal Noun | Noun 
	PP -> IN NP
	V -> VBZ | VB | VBD | VBG
	VBZ -> 'barks' | 'laughs' | 'eats' | 'feeds' | 'thinks' | 'drinks' | 'does'
	VB -> 'bark' | 'laugh' | 'eat' | 'feed' | 'think' | 'drink' | 'do'
 	VBD -> 'barked' | 'laughed' | 'ate' | 'fed' | 'thought' | 'drank' | 'did'
 	VBG -> 'barking' | 'laughing' | 'eating' | 'feeding' | 'thinking' | 'drinking' | 'doing'
 	Auxiliary -> 'does' | 'do' | 'did'
 	ProperNoun -> 'Gromit' | 'Wallace'
	Noun -> 'cheese' | 'water' | 'kitchen' | 'dinner'
	DT -> 'a' | 'the' | 'an' | 'my'
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

def main():
	g = Grammar(cfg_str)
	g.parse_and_print(text)

if __name__ == '__main__':
	main()