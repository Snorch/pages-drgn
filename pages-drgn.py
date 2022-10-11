#!/usr/bin/env drgn
# Copyright (c) Facebook, Inc. and its affiliates.
# SPDX-License-Identifier: GPL-3.0+

DESCRIPTION = """
drgn script to list pages
"""

from drgn.helpers.linux.mm import for_each_page, decode_page_flags

def pages_tos(pages):
    kb = pages * 4
    if kb < 1024:
        return f'{kb:.2f} Kb'
    mb = kb / 1024
    if mb < 1024:
        return f'{mb:.2f} Mb'
    gb = mb / 1024
    return f'{gb:.2f} Gb'

class mydict(dict):
    def cntadd(self, item):
        self[item] = self.get(item, 0) + 1

def main():
    mycnt = mydict()

    for page in for_each_page(prog):
        mycnt.cntadd('all')
        flags = None
        try:
            flags = decode_page_flags(page)
        except:
            mycnt.cntadd('err')
            continue

        for flag in flags.split('|'):
            mycnt.cntadd(flag)

    for key in mycnt:
        print(f'{key} = {pages_tos(mycnt[key])}')

if __name__ == "__main__":
    main()
