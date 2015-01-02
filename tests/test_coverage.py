# -*- coding: utf-8 -*-
from frigg.coverage import parse_coverage


def test_parse_coverage():
    assert parse_coverage('fixtures/python.xml', 'python') == 0.9317
