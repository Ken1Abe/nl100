#!/usr/bin/env python

import codecs
import random

fpos = codecs.open('rt-polarity.pos', 'r', 'latin_1')
fneg = codecs.open('rt-polarity.neg', 'r', 'latin_1')
fsen = codecs.open('sentiment.txt', 'w', 'latin_1')

if __name__ == "__main__":
  pos = ["+1 "+line for line in fpos]
  neg = ["-1 "+line for line in fneg]
  sentiment = pos + neg

  random.shuffle(sentiment)

  [fsen.writelines(line) for line in sentiment]

