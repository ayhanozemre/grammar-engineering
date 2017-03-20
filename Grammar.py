from nltk import *

class Grammar:

	def __init__(self, cfg_str):
		self.cfg = grammar.FeatureGrammar.fromstring(cfg_str)
		self.parser = FeatureChartParser(self.cfg)

	def parse(self, text):
		""" Returns a generator. """
		sents = text.splitlines()
		for sent in sents:
			parses = self.parser.parse(sent.split())
			for tree in parses:
				yield tree

	def parse_and_print(self, text, toPrint=False):
		""" Does not return anything, prints all the info. """
		sents = text.splitlines()
		counter = 0
		toPrintNow = False
		for sent in sents:
			parses = self.parser.parse(sent.split())
			number = len(list(parses))
			if number == 0:
				print "No parsing trees for sentence: "
				print "-- ", sent
			if number > 0:
				counter +=1
			if number > 1:
				print number, "trees for sentence:"
				print "-- ", sent
				toPrintNow = True
			if toPrint or toPrintNow:
				for tree in self.parser.parse(sent.split()):
					print tree
					print "--------------"
				if toPrintNow:
					toPrintNow = False
		print counter, "/", len(sents)



