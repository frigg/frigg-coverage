# -*- coding: utf-8 -*-
from frigg_coverage import parse_coverage


def test_parse_coverage_report():
    with open('fixtures/go_coverprofile.out') as f:
        assert parse_coverage(f.read(), 'go-coverprofile') == 98.73
