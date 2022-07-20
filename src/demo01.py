import sys, codecs, json, math, time, warnings
warnings.simplefilter( action='ignore', category=FutureWarning )

import nltk, scipy, sklearn, sklearn_crfsuite, sklearn_crfsuite.metrics, eli5
from sklearn.metrics import make_scorer
from collections import Counter
import matplotlib.pyplot as plt
from IPython.display import display

import logging
import tensorflow as tf
import absl.logging
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s %(asctime)s] %(message)s')
absl.logging.get_absl_handler().setFormatter(formatter)
absl.logging._warn_preinit_stderr = False
logger = tf.get_logger()
logger.setLevel(logging.INFO)

# number of CRF iterations to train for. Using 150 will provide much better results, but take a lot longer to compute.
max_iter = 20

# number of ontonotes training files to load. Using a value of None will load the entire dataset, taking the longest
# to train but providing a much larger sentence corpus to train over and thus is able to learn a larger vocabulary.
max_files = 50

# set of NE label types to display in results. this is simply to limit the amount of logging that is perfoemed later
# when displaying details such as state transitions and top N features per state.
display_label_subset = [ 'B-DATE', 'I-DATE', 'B-GPE', 'I-GPE', 'B-PERSON', 'I-PERSON', 'O' ]