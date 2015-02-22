# -*- coding: utf-8 -*-
from decimal import Decimal
import xml.etree.ElementTree as ET


def parse_coverage_report(string):
    report = ET.fromstring(string)
    metrics = report.find('project').find('metrics')
    covered = int(metrics.get('coveredstatements'))
    statements = int(metrics.get('statements'))
    return float(round(Decimal(covered / statements) * 100, 2))
