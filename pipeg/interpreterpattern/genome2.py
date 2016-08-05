#__author__ = 'James'
#-*- coding:utf-8 -*-

import collections
import json
import os
import re
import subprocess
import sys

UTF8 = "utf-8"
TRANSFORM, SUMMARIZE = ("TRANSFORM", "SUMMARIZE")

Code = collections.namedtuple("Code", "name code kind")


def main():
    genome = 3 * GENOME
    for i, code in enumerate(CODE):
        context = dict(genome=genome, target="G[AC]{2}TT", replace="TCGA")
        execute(code, context)


if sys.version_info[:2] > (3, 1):
    def execute(code, context):
        module, offset = create_module(code.code, context)
        with subprocess.Popen([sys.executable, "-"], stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            communicate(process, code, module, offset)
else:
    def execute(code, context):
        module, offset = create_module(code.code, context)
        process = subprocess.Popen([sys.executable, "-"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        communicate(process, code, module, offset)


def create_module(code, context):
    lines = ["import json", "result = error = None"]
    for key, value in context.items():
        lines.append("{} = {!r}".format(key, value))        #'!s' which calls str() on the value, and '!r' which calls repr()
    offset = len(lines) + 1
    outputLine = "\nprint(json.dumps((result, error)))"
    return "\n".join(lines) + "\n" + code + outputLine, offset


def communicate(process, code, module, offset):
    stdout, stderr = process.communicate(module.encode(UTF8))
    if stderr:
        stderr = stderr.decode(UTF8).lstrip().replace(", in <module>", ":")
        stderr = re.sub(", line (\d+)",
                lambda match: str(int(match.group(1)) - offset), stderr)
        print(re.sub(r'File."[^"]+?"', "'{}' has an error on line "
                .format(code.name), stderr))
        return
    if stdout:
        result, error = json.loads(stdout.decode(UTF8))
        handle_result(code, result, error)
        return
    print("'{}' produced no result\n".format(code.name))


def handle_result(code, result, error):
    if error is not None:
        print("'{}' error: {}".format(code.name, error))
    elif result is None:
        print("'{}' produced no result".format(code.name))
    elif code.kind == TRANSFORM:
        genome = result
        try:
            print("'{}' produced a genome of length {}".format(code.name,
                    len(genome)))
        except TypeError as err:
            print("'{}' error: expected a sequence result: {}".format(
                    code.name, err))
    elif code.kind == SUMMARIZE:
        print("'{}' produced a result of {}".format(code.name, result))
    print()


CODE = (
    Code("Count",
"""
import re
matches = re.findall(target, genome)
if matches:
    result = len(matches)
else:
    error = "'{}' not found".format(target)
""", SUMMARIZE)
,
    Code("Replace",
"""
import re
result, count = re.subn(target, replace, genome)
if not count:
    error = "no '{}' replacements made".format(target)
""", TRANSFORM)
,
    Code("Exception Test",
"""
result = 0
for i in range(len(genome)):
    if genome[i] = "A":
        result += 1
""", SUMMARIZE)
,
    Code("Error Test",
"""
import re
matches = re.findall(target * 5, genome)
if matches:
    result = len(matches)
else:
    error = "'{}' not found".format(target)
""", TRANSFORM)
,
    Code("No Result Test",
"""
# No result
""", TRANSFORM)
,
    Code("Wrong Kind Test",
"""
result = len(genome)
""", TRANSFORM)
,
    Code("Termination Test",
"""
import sys
result = "terminating"
sys.exit()
""", SUMMARIZE)
,
    Code("Length",
"""
result = len(genome)
""", SUMMARIZE)
)


GENOME = """TGTTAGTCGCTCCTCGGTCTAAGACATCAAAGTCGGTCTGCGCGGCTGCTCCCTTAGCGCTG
CATAAGAGCGGGGCAGAGAGAGATAGGCGTTTTGACCGTGGCGAGCAAGGCGCGTCATAGTGTCGCCGTGACTG
ATCCTACTGGGTTCTTGCTACTGCCCGGGTCGCAATCCAAAATCTCCACGCGCTGCCACCCCGAAGAAGATATA
TGTCACTGAATTGTATTGGTAACATAGTCGAATTGGGTTCAGGTAAGTTAGTCGTTTAGCCGCTGCGACAGTGG
TGGAAGGGCGAATAGTGTAAAATTTCGCCTGTTAGTGAACATTATCAGGCTGCCATCGTTGATCGCCCCTCTTA
AACTCAGTCTTAAATGAGTTCCCGCCTAAGGTCATTCGTGCCTTGATGATTGATAGCTCGATTGGTCCCTTATG
AAACCGGACCAGAAATGTACCCGCTGAACCGGTGTCATAAGTGTCGCCGTCCCTACGATCGACACTTCCTGAGC
ACGAACGATTTGCGACGCTGTAATGCCACGAGGACTGCATTGAAGATTTTTTGTCCTAGGTGTATGTGCTTCTC
AGGAAGATGCACTACGCACTCCCCTTATCACGGGTGTGACCATCAGGTAGCGTAGGAAGATTAAGACCGCGTAA
CTATCCCTTTCCGTCGCACTCCGACGTCTCAGCACATGTGCGGGGGCCCCTAATTGAGAAACAGTCCATGGTTG
TCCGTAAGTTTCGGAAATCAACTTCACTGCTAGATGGTTGGACGCCAAGGCTCAATAGGTTGGACTCTAAGAAG
""".replace("\n", "")


if __name__ == "__main__":
    main()
