# -*- coding: utf-8 -*-

from .python_coverage import parse_coverage_report as python_coverage

PARSERS = {
    'python': python_coverage
}
