# -*- coding: utf-8 -*-
from frigg_coverage import parse_coverage


def test_parse_coverage():
    assert parse_coverage('', '') == NotImplemented
    assert parse_coverage('', 'python') is None
    assert parse_coverage('', 'clover') is None
    assert parse_coverage('', 'cobertura') is None
