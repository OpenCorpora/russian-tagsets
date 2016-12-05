# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import pytest

from russian_tagsets import converters, ud
#from .opencorpora_aot_data import PARSE_RESULTS

class TestInternalConversion(object):
    TEST_DATA = [
        ['власть', 'NOUN,inan,femn sing,nomn', 'NOUN Animacy=Inan|Case=Nom|Gender=Fem|Number=Sing'],
        ['поменяться', 'INFN,perf,intr', 'VERB Aspect=Perf'],
        ['.', 'PNCT', 'PNCT punct'],
    ]

    @pytest.mark.parametrize(("word", "internal", "ud"), TEST_DATA)
    def test_from_internal(self, word, internal, external):
        converted = converters.convert(internal, 'opencorpora-int', 'ud')
        assert converted == external


def _remove_unsupported(ud_tag):
    pos, info = ud.split_tag(ud_tag)
#    info.difference_update(
#        set(['од', 'но', '2', 'имя', 'фам', 'лок', 'кач', 'разг'])
#    )
#    if pos == 'ДЕЕПРИЧАСТИЕ':
#    info.discard('дст')
#
#    if pos == 'С':
#        if 'аббр' in info:
#            info.difference_update(set(aot.CASES.keys()))

    return ud.join_tag(pos, info)


#class TestAotConversion(object):
#
#    @pytest.mark.parametrize(("word", "open_tag", "ud_tag"), PARSE_RESULTS)
#    def test_to_aot(self, word, open_tag, ud_tag):
#        converted = converters.convert(open_tag, 'opencorpora-int', 'ud')
#        assert ud.split_tag(_remove_unsupported(converted)) == ud.split_tag(_remove_unsupported(ud_tag))
