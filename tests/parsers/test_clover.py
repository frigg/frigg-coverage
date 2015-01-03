# -*- coding: utf-8 -*-
from frigg_coverage.parsers.clover import parse_coverage_report


def test_parse_coverage_report():
    assert parse_coverage_report('fixtures/clover.xml') == 88.24
    assert parse_coverage_report('bad-path') is None
