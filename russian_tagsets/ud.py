# -*- coding: utf-8 -*-
"""
Conversion between inner OpenCorpora format and Universal Dependencies 1.4
(http://universaldependencies.org/ru/pos/all.html)

Known issues:
TODO
"""

from __future__ import absolute_import, unicode_literals
from russian_tagsets import converters
from russian_tagsets.utils import invert_mapping

class Tag(object):

    GRAM_MAP = {
        '_POS': {
            'ADJF': 'ADJ',
            'ADVB': 'ADV',
            'INFN': 'VERB',
            'INTJ': 'INTJ',
            'NOUN': 'NOUN',
            'NPRO': 'PRON',
            'PNCT': 'PUNCT',
            'PRCL': 'PART',
            'VERB': 'VERB',
        },
        'Animacy': {
            'anim': 'Anim',
            'inan': 'Inan',
        },
        'Aspect': {
            'impf': 'Imp',
            'perf': 'Perf',
        },
        'Case': {
            'ablt': 'Ins',
            'accs': 'Acc',
            'datv': 'Dat',
            'gent': 'Gen',
            'loct': 'Loc',
            'nomn': 'Nom',
        },
        'Gender': {
            'femn': 'Fem',
            'masc': 'Masc',
            'neut': 'Neut',
        },
        'Mood': {
            'impr': 'Imp',
            'indc': 'Ind',
        },
        'Number': {
            'plur': 'Plur',
            'sing': 'Sing',
        },
        'Tense': {
            'past': 'Past',
        },
        'VerbForm': {
            'INFN': 'Inf',
            'VERB': 'Fin',
        },
    }

    def __init__(self, oc_tag):
        self.pos = 'X'
        self.grammemes = set()
        self.unmatched = set()
        self._fill_from_oc(oc_tag)

    def _postprocess(self):
        while len(self.unmatched) > 0:
            gram = self.unmatched.pop()
            
            if gram == 'Name':
                self.pos = 'PROPN'

    def _fill_one_gram_oc(self, gram):
        match = False
        for categ, gmap in self.GRAM_MAP.items():
            if gram in gmap:
                if categ == '_POS':
                    self.pos = gmap[gram]
                    match = True
                else:
                    self.grammemes.add((categ, gmap[gram]))
                    match = True

        if not match:
            self.unmatched.add(gram)

    def _fill_from_oc(self, oc_tag):
        grams = oc_tag.replace(' ', ',').split(',')
        for g in grams:
            self._fill_one_gram_oc(g)
        self._postprocess()

    def __str__(self):
        grams = '|'.join("{}={}".format(c, v) for c, v in sorted(list(self.grammemes)))
        return "{} {}".format(self.pos, grams if grams else '_')


def to_ud14(oc_tag, word=None):
    tag = Tag(oc_tag)
    return str(tag)

converters.add('opencorpora-int', 'ud14', to_ud14)