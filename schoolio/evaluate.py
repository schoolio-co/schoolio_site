#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import re
import random

def cleanup_text(text):
    text = re.sub(r"[^A-Za-z\s]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text
def extractwords(blurb):
    return re.split("[^A-Za-z]+", blurb)
def get_words_to_vects_from_DataFrame(filename = 'schoolio/standards/vocab_words_to_vects.csv'):
    df = pd.read_csv(filename, index_col=0)
    d = dict( (index, np.array(df.loc[index])) for index in df.index )
    d[' '] = np.array(([0.0] * 14) + [1.0])
    return d

def score(text, words_to_vects = get_words_to_vects_from_DataFrame(), verbose=True,
   normalizing_vector = np.array([3.54705117e-02, 1.11550042e-02, 2.59606981e-02, 4.65886871e-03,
  8.73045133e-03, 2.77074305e-03, 9.96858132e-04, 3.94153355e-03,
  2.43412391e-03, 6.61637174e-03, 4.02463865e-03, 6.43246708e-03,
  3.73455050e-03, 5.53467116e-03, 1.00000000e+00])):
    text = cleanup_text(text)
    words = extractwords(text)
    score = np.zeros(len(words_to_vects[' ']))
    
    for word in words:
        if word:
            if word.lower() in words_to_vects:
                score += words_to_vects[word.lower()]
            else:
                score += words_to_vects[' ']
    score = score / normalizing_vector
    if verbose:
        print("The text starting with {} had the following score:".format(repr(text.strip()[:100])))
        print("\t", score)
    return score

# Bloom level 1 KNOWLEDGE,Bloom level 2 COMPREHENSION,Bloom level 3 APPLICATION,
# Bloom level 4 ANALYSIS,Bloom level 5 SYNTHESIS,Bloom level 6 EVALUATE,
#
# Bodily Kinesthetic,Interpersonal,Intrapersonal,Logical - Mathematical,Musical,
# Naturalist,Verbal - Linguistic,Visual Spatial,
#
# Is word
def get_MI_BL(text, verbose=False):
    sc = score(text, verbose=verbose)
    BL_level_scores = (sc[0]+sc[1], sc[2]+sc[3], sc[4]+sc[5])
    BL = ("Low", "Medium", "High")[BL_level_scores.index(max(BL_level_scores))]
    MI_options = ("Bodily Kinesthetic,Interpersonal,Intrapersonal,"
                 "Logical - Mathematical,Musical,Naturalist,"
                 "Verbal - Linguistic,Visual Spatial").split(",")
    MI_scores = sc[6:14]
    MI_zipped = list(zip(MI_scores, MI_options))
    MI_zipped.sort()
    MI_1, MI_2, MI_3 = map(lambda p: p[1], MI_zipped[:3])
    return BL, MI_1, MI_2, MI_3