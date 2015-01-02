# -*- coding: utf-8 -*-
from .parsers import PARSERS


def parse_coverage(path, parser):
    return PARSERS[parser](path)
