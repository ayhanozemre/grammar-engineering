from nltk import *

class Grammar:

	def __init__(self, cfg_str):
		self.cfg = grammar.FeatureGrammar.fromstring(cfg_str)

	def parse(self, text):
		uparser = FeatureChartParser(self.cfg)
		sents = text.splitlines()
		for sent in sents:
			yield uparser.parse(sent.split())

	def parse_and_print(self, text):
		res = self.parse(text)
		for r in res:
			for t in r:
				print t

	def test(text, toPrint=False):
		sents = text.splitlines()
		counter = 0
		toPrintNow = False
		for sent in sents:
			parses = cfparser.parse(sent.split())
			number = len(list(parses))
			if number == 0:
				print "No parsing trees for sentence: "
				print "-- ", sent
			if number > 0:
				counter +=1
			if number>1:
				print number, "trees for sentence:"
				print "-- ", sent
				toPrintNow = True
			if toPrint or toPrintNow:
				for tree in cfparser.parse(sent.split()):
					print tree
					print "--------------"
				if toPrintNow:
					toPrintNow = False
		print counter, "/", len(sents)

