from nltk import *
cfg = CFG.fromstring("""
	S -> NP | NP VP | Question
	Question -> QuestionWord Auxiliary NP VP
	QuestionWord -> WRB
	Auxiliary -> 'does' | 'do' | 'did'
	NP -> NN | DT Noun | NN CC NN 
	NN -> ProperNoun | Noun
	ProperNoun -> 'Gromit' | 'Wallace'
	Noun -> 'cheese' | 'water' | 'kitchen' | 'dinner'
	VP -> V | V DT Noun | V NN
	V -> VBZ | VB | VBD | VBG
	VBZ -> 'barks' | 'laughs' | 'eats' | 'feeds' | 'thinks' | 'drinks' | 'does'
	VB -> 'bark' | 'laugh' | 'eat' | 'feed' | 'think' | 'drink' | 'do'
 	VBD -> 'barked' | 'laughed' | 'ate' | 'fed' | 'thought' | 'drank' | 'did'
 	VBG -> 'barking' | 'laughing' | 'eating' | 'feeding' | 'thinking' | 'drinking' | 'doing'
	DT -> 'a' | 'the' | 'an' | 'my'
	IN -> 'in' | 'on' | 'at' | 'after' | 'when'
	JJ -> 'tasty' | 'soft' 
	CC -> 'and' | 'but'
	RB -> 'seldom' | 'often' | 'when'
	WRB -> 'when'
	""")
cfparser = ChartParser(cfg)
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

sents = text.splitlines()
counter = 0
for sent in sents:
	parses = cfparser.parse(sent.split())
	for tree in parses:
		print tree
		print "--------------"
		counter += 1
print counter, "/", len(sents)