# -*- coding: utf-8 -*-


def parse_coverage_report(string):
    # get cover of each pkg and remove % sign
    packages = [pkg for pkg in string.splitlines() if pkg[:2] == "ok" or pkg[:1] == "?"]
    coverages = [float(pkg.split()[-3][:-1]) for pkg in packages if pkg[:2] == "ok"]
    return round(sum(coverages) / len(packages), 2)
