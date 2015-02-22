# -*- coding: utf-8 -*-
from frigg_coverage.parsers import clover, cobertura

PARSERS = {
    'python': cobertura,
    'clover': clover,
    'cobertura': cobertura
}
