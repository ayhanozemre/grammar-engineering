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

	def parse_and_print(self, text, toPrint=False, toPrintRepetitions=False):
		""" Does not return anything, prints all the info. """
		sents = text.splitlines()
		counter = 0
		for sent in sents:
			parses = self.parser.parse(sent.split())
			number = len(list(parses))
			if number > 0:
				counter += 1
			print "found {} parses for sentence: \n   {}".format(number, sent)
			if toPrint or (number > 1 and toPrintRepetitions):
				
				for tree in self.parser.parse(sent.split()):
					print tree
					print "--------------"
		print "{}/{} sentences have been parsed.".format(counter, len(sents))



