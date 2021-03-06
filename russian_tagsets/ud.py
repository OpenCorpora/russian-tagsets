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
            'ADJS': 'ADJ',
            'ADVB': 'ADV',
            'Apro': 'DET',
            'CONJ': 'CONJ',
            'GRND': 'VERB',
            'INFN': 'VERB',
            'INTJ': 'INTJ',
            'NOUN': 'NOUN',
            'NPRO': 'PRON',
            'NUMR': 'NUM',
            'PART': 'PRCL',
            'PNCT': 'PUNCT',
            'PRCL': 'PART',
            'PREP': 'ADP',
            'PRTF': 'ADJ',
            'PRTS': 'ADJ',
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
            'ADJS': 'Nom',
            'datv': 'Dat',
            'gen1': 'Gen',
            'gen2': 'Gen',
            'gent': 'Gen',
            'loc2': 'Loc',
            'loct': 'Loc',
            'nomn': 'Nom',
            'PRTS': 'Nom',
            'voct': 'Nom',
        },
        'Degree': {
            'COMP': 'Cmp',
            'Supr': 'Sup',
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
        'Person': {
            '1per': '1',
            '2per': '2',
            '3per': '3',
            'excl': '2',
            'incl': '1',
        },
        'Tense': {
            'futr': 'Fut',
            'past': 'Past',
            'pres': 'Pres',
        },
        'Variant': {
            'ADJS': 'Brev',
            'PRTS': 'Brev',
        },
        'VerbForm': {
            'GRND': 'Conv',
            'INFN': 'Inf',
            'PRTF': 'Part',
            'PRTS': 'Part',
            'VERB': 'Fin',
        },
        'Voice': {
            'actv': 'Act',
            'GRND': 'Act',
            'pssv': 'Pass',
        }
    }

    def __init__(self, oc_tag, word):
        self.pos = 'X'
        self.grammemes = dict()
        self.word = word
        self.unmatched = set()
        self._fill_from_oc(oc_tag)

    def _postprocess(self):
        while len(self.unmatched) > 0:
            gram = self.unmatched.pop()
            
            if gram in ('Name', 'Patr', 'Surn', 'Geox', 'Orgn'):
                self.pos = 'PROPN'
            elif gram == 'Auxt':
                self.pos = 'AUX'
            elif gram == 'Pltm':
                self.grammemes['Number'] = 'Ptan'

        # remove verbal grammemes from ex-participles
        if self.pos == 'ADJ':
            for group in ('Aspect', 'Tense', 'VerbForm', 'Voice'):
                if group in self.grammemes:
                    del self.grammemes[group]
        # change Voice to Mid for -sya-gerunds
        elif self.pos == 'VERB' and self.grammemes['VerbForm'] == 'Conv':
            if self.word.endswith(('ся', 'сь')):
                self.grammemes['Voice'] = 'Mid'

    def _fill_one_gram_oc(self, gram):
        match = False
        for categ, gmap in sorted(self.GRAM_MAP.items()):
            if gram in gmap:
                if categ == '_POS':
                    self.pos = gmap[gram]
                    match = True
                else:
                    self.grammemes[categ] = gmap[gram]
                    match = True

        if not match:
            self.unmatched.add(gram)

    def _fill_from_oc(self, oc_tag):
        grams = oc_tag.replace(' ', ',').split(',')
        for g in grams:
            self._fill_one_gram_oc(g)
        self._postprocess()

    def __str__(self):
        grams = '|'.join("{}={}".format(c, v) for c, v in sorted(self.grammemes.items()))
        return "{} {}".format(self.pos, grams if grams else '_')


def to_ud14(oc_tag, word=None):
    tag = Tag(oc_tag, word)
    return str(tag)

converters.add('opencorpora-int', 'ud14', to_ud14)
