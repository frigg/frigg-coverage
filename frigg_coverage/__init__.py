# -*- coding: utf-8 -*-
from .parsers import PARSERS


def parse_coverage(path, parser):
    if parser in PARSERS:
        return PARSERS[parser].parse_coverage_report(path)
    return NotImplemented
