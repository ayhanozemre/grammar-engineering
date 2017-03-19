from nltk import *
cfg = CFG.fromstring("""
	S -> NP VP
	NP -> ProperNoun | Noun
	ProperNoun -> 'Gromit' | 'Wallace'
	Noun -> 'cheese' | 'water' | 'kitchen' | 'dinner'
	VP -> V
	V -> VBZ
	VBZ -> 'barks' | 'laughs' | 'eats' | 'feeds' | 'thinks' | 'drinks' 
	DT -> 'a' | 'the' 
	IN -> 'in' | 'on' | 'at' | 'after' | 'when'
	JJ -> 'tasty' | 'soft' 
	CC -> 'and' | 'but'
	RB -> 'seldom' | 'often' | 'when'
	WP -> 'when'
	""")
cfparser = ChartParser(cfg)
text = """\
Gromit barks
Wallace laughs
"""
sents = text.splitlines()
for sent in sents:
	parses = cfparser.parse(sent.split())
	for tree in parses:
		print tree