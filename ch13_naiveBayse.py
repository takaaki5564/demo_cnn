#coding:utf-8
import math
import sys
from collections import defaultdict

class NaiveBayse:
    """Multinominal Naive Bayse"""
    def __init__(self):
        self.categories = set()    # カテゴリの集合
        self.vocabularies = set()  # ボキャブラリの集合
	self.wordcounta
