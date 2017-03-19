from nltk import *
cfg = CFG.fromstring("""
	S -> NP VP | NP RB VP | Question | S CC S
	Question -> QuestionWord Auxiliary NP VP
	QuestionWord -> WRB
	Auxiliary -> 'does' | 'do' | 'did'
	PPS -> PPS PP | PP 
	PP -> IN DT NN | IN NN
	NP -> NN | DT Noun | JJ NN | DT Noun PPS
	NN -> ProperNoun | Noun | NN CC NN
	JJ -> JJ JJS | JJS
	VP -> V | V NN NN | V NP | VP CC VP | V NP VP | VP PPS
	V -> VBZ | VB | VBD | VBG
	VBZ -> 'barks' | 'laughs' | 'eats' | 'feeds' | 'thinks' | 'drinks' | 'does'
	VB -> 'bark' | 'laugh' | 'eat' | 'feed' | 'think' | 'drink' | 'do'
 	VBD -> 'barked' | 'laughed' | 'ate' | 'fed' | 'thought' | 'drank' | 'did'
 	VBG -> 'barking' | 'laughing' | 'eating' | 'feeding' | 'thinking' | 'drinking' | 'doing'
 	ProperNoun -> 'Gromit' | 'Wallace'
	Noun -> 'cheese' | 'water' | 'kitchen' | 'dinner'
	DT -> 'a' | 'the' | 'an' | 'my'
	IN -> 'in' | 'on' | 'at' | 'after' | 'when'
	JJS -> 'tasty' | 'soft' 
	CC -> 'and' | 'but'
	RB -> 'seldom' | 'often' | 'when'
	WRB -> 'when'
	""")

cfparser = ChartParser(cfg)
text = """
when Gromit barks Wallace feeds Gromit
"""

done = """\
Gromit barks
Gromit barked
Wallace and Gromit eat cheese
Wallace and Gromit ate cheese
Wallace feeds Gromit
Wallace seldom feeds Gromit cheese
Wallace thinks Gromit eats cheese and drinks water
Wallace often eats tasty soft cheese in the kitchen after dinner
when does Wallace eat cheese
"""


def test(text, toPrint=False):
	sents = text.splitlines()
	counter = 0
	for sent in sents:
		parses = cfparser.parse(sent.split())
		for tree in parses:
			if toPrint:
				print tree
				print "--------------"
			counter += 1
	print counter, "/", len(sents)

test(text, True)
test(done)