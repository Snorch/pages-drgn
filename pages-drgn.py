#!/usr/bin/env drgn
# Copyright (c) Facebook, Inc. and its affiliates.
# SPDX-License-Identifier: GPL-3.0+

DESCRIPTION = """
drgn script to list pages
"""

from drgn.helpers.linux.mm import for_each_page, decode_page_flags

'''
PG_uptodate
PG_head
PG_reserved
PG_tail
PG_reclaim
PG_slab
PG_private
PG_active
PG_swapcache
PG_mappedtodisk
PG_savepinned
PG_slob_free
PG_swapbacked
PG_referenced
PG_lru
PG_dirty
'''
def main():

    cnt_all = 0
    cnt_err = 0
    cnt_PG_uptodate = 0
    cnt_PG_head = 0
    cnt_PG_reserved = 0
    cnt_PG_tail = 0
    cnt_PG_reclaim = 0
    cnt_PG_slab = 0
    cnt_PG_private = 0
    cnt_PG_active = 0
    cnt_PG_swapcache = 0
    cnt_PG_mappedtodisk = 0
    cnt_PG_savepinned = 0
    cnt_PG_slob_free = 0
    cnt_PG_swapbacked = 0
    cnt_PG_referenced = 0
    cnt_PG_lru = 0
    cnt_PG_dirty = 0

    for page in for_each_page(prog):
        cnt_all += 1
        flags = ''
        try:
            flags = decode_page_flags(page)
        except:
            cnt_err += 1

        if 'PG_uptodate' in flags:
            cnt_PG_uptodate += 1
        if 'PG_head' in flags:
            cnt_PG_head += 1
        if 'PG_reserved' in flags:
            cnt_PG_reserved += 1
        if 'PG_tail' in flags:
            cnt_PG_tail += 1
        if 'PG_reclaim' in flags:
            cnt_PG_reclaim += 1
        if 'PG_slab' in flags:
            cnt_PG_slab += 1
        if 'PG_private' in flags:
            cnt_PG_private += 1
        if 'PG_active' in flags:
            cnt_PG_active += 1
        if 'PG_swapcache' in flags:
            cnt_PG_swapcache += 1
        if 'PG_mappedtodisk' in flags:
            cnt_PG_mappedtodisk += 1
        if 'PG_savepinned' in flags:
            cnt_PG_savepinned += 1
        if 'PG_slob_free' in flags:
            cnt_PG_slob_free += 1
        if 'PG_swapbacked' in flags:
            cnt_PG_swapbacked += 1
        if 'PG_referenced' in flags:
            cnt_PG_referenced += 1
        if 'PG_lru' in flags:
            cnt_PG_lru += 1
        if 'PG_dirty' in flags:
            cnt_PG_dirty += 1


    print(f'cnt_all = {cnt_all}')
    print(f'cnt_err = {cnt_err}')

    print(f'PG_uptodate = {cnt_PG_uptodate}')
    print(f'PG_head = {cnt_PG_head}')
    print(f'PG_reserved = {cnt_PG_reserved}')
    print(f'PG_tail = {cnt_PG_tail}')
    print(f'PG_reclaim = {cnt_PG_reclaim}')
    print(f'PG_slab = {cnt_PG_slab}')
    print(f'PG_private = {cnt_PG_private}')
    print(f'PG_active = {cnt_PG_active}')
    print(f'PG_swapcache = {cnt_PG_swapcache}')
    print(f'PG_mappedtodisk = {cnt_PG_mappedtodisk}')
    print(f'PG_savepinned = {cnt_PG_savepinned}')
    print(f'PG_slob_free = {cnt_PG_slob_free}')
    print(f'PG_swapbacked = {cnt_PG_swapbacked}')
    print(f'PG_referenced = {cnt_PG_referenced}')
    print(f'PG_lru = {cnt_PG_lru}')
    print(f'PG_dirty = {cnt_PG_dirty}')


if __name__ == "__main__":
    main()
