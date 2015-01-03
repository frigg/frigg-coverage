# -*- coding: utf-8 -*-
import os
from decimal import Decimal
from lxml import etree


def parse_coverage_report(path):
    if os.path.exists(path):
        with open(path) as f:
            report = etree.parse(f)
            covered = int(report.getroot().find('project').find('metrics').get('coveredstatements'))
            statements = int(report.getroot().find('project').find('metrics').get('statements'))
        return float(round(Decimal(covered / statements) * 100, 2))
