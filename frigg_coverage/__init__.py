# -*- coding: utf-8 -*-
from .parsers import PARSERS

__version__ = '1.1.0'


def parse_coverage(coverage_report, parser):
    """
    :param coverage_report: A string with the contents of a coverage file
    :type coverage_report: String
    :param parser: A string with name of the parser to use
    :type parser: String
    :return: Total coverage
    """
    if parser in PARSERS:
        if coverage_report:
            return PARSERS[parser].parse_coverage_report(coverage_report)
        return None
    return NotImplemented
