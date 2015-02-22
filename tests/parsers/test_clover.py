# -*- coding: utf-8 -*-
from frigg_coverage import parse_coverage


def test_parse_coverage_report():
    assert parse_coverage('fixtures/clover.xml', 'clover') == 88.24
    assert parse_coverage('bad-path', 'clover') is None
