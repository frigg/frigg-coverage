# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from decimal import Decimal


def parse_coverage_report(string):
    report = ET.fromstring(string)
    metrics = report.find('project').find('metrics')
    covered = int(metrics.get('coveredstatements'))
    statements = int(metrics.get('statements'))
    return float(round(Decimal(float(covered) / float(statements)) * 100, 2))
