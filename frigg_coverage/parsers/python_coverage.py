# -*- coding: utf-8 -*-
import os
from lxml import etree


def parse_coverage_report(path):
    if os.path.exists(path):
        with open(path) as f:
            report = etree.parse(f)
        return float(report.getroot().get('line-rate')) * 100
