# -*- coding: utf-8 -*-
import os
import re
from .parsers import PARSERS


def parse_coverage(path_or_string, parser):
    """
    :param path_or_string: A path to an coverage fil or string with the contents of a coverage file
    :param parser: String with name of the parser to use
    :return: Total coverage
    """
    if re.match(r'^(/)?([^/\0]+(/)?)+$', path_or_string):
        if not os.path.isabs(path_or_string):
            path_or_string = os.path.join(os.getcwd(), path_or_string)

        if os.path.exists(path_or_string):
            with open(path_or_string) as f:
                string = f.read()
        else:
            string = None
    else:
        string = path_or_string

    if parser in PARSERS:
        if string:
            return PARSERS[parser].parse_coverage_report(string)
        return None
    return NotImplemented
