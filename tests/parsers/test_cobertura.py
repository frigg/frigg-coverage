# -*- coding: utf-8 -*-
from frigg_coverage import parse_coverage


def test_parse_coverage_report():
    with open('fixtures/cobertura.xml') as f:
        assert parse_coverage(f.read(), 'cobertura') == 88.24
