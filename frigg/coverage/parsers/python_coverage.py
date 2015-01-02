# -*- coding: utf-8 -*-
from lxml import etree


def parse_coverage_report(path):
    with open(path) as f:
        report = etree.parse(f)
    return float(report.getroot().get('line-rate'))

