# -*- coding: utf-8 -*-
from frigg_coverage.parsers.python_coverage import parse_coverage_report


def test_parse_coverage_report():
    assert parse_coverage_report('fixtures/python.xml') == 93.17
    assert parse_coverage_report('bad-path') is None
