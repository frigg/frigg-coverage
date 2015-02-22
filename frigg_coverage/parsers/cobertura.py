# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


def parse_coverage_report(string):
    report = ET.fromstring(string)
    return float(report.get('line-rate')) * 100
