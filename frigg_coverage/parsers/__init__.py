# -*- coding: utf-8 -*-
from frigg_coverage.parsers import python_coverage, clover, cobertura

PARSERS = {
    'python': python_coverage,
    'clover': clover,
    'cobertura': cobertura
}
