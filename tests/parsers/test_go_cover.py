# -*- coding: utf-8 -*-
from frigg_coverage import parse_coverage


def test_parse_coverage_report():
    with open('fixtures/go_cover.out') as f:
        assert parse_coverage(f.read(), 'go-cover') == 52.73
