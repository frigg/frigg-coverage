# -*- coding: utf-8 -*-
from .parsers import PARSERS


def parse_coverage(path, parser):
    if parser in PARSERS:
        return PARSERS[parser](path)
    return NotImplemented
