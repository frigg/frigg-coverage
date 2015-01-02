# -*- coding: utf-8 -*-
from frigg_coverage import parse_coverage


def test_parse_coverage():
    assert parse_coverage('fixtures/python.xml', 'python') == 93.17
