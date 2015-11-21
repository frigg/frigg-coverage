# -*- coding: utf-8 -*-
from decimal import Decimal


def parse_coverage_report(string):
    lines = string.splitlines()[1:]  # Skip cover mode def.
    statements = len(lines)
    covered = sum([line.split()[-1] != '0' and 1 or 0 for line in lines])
    return float(round(Decimal(float(covered) / float(statements)) * 100, 2))
