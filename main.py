from nltk import *
cfg = CFG.fromstring("""
	S -> NP VP
	NP -> ProperNoun | Noun
	ProperNoun -> 'Gromit' | 'Wallace'
	Noun -> 'cheese' | 'water' | 'kitchen'
	VP -> V
	V -> VB | VBD | VBG | VBZ
	VB -> 'bark' | 'laugh'
	VBD -> 'barked' | 'laughed'
	VBG -> 'barking' | 'laughing'
	VBZ -> 'barks' | 'laughs'
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