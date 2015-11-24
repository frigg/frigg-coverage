# -*- coding: utf-8 -*-
from frigg_coverage.parsers import clover, cobertura, go_coverprofile, go_cover

PARSERS = {
    'python': cobertura,
    'clover': clover,
    'cobertura': cobertura,
    'go-coverprofile': go_coverprofile,
    'go-cover': go_cover
}
