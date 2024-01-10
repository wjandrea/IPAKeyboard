#!/usr/bin/env python3
"""
Replace combining characters in XML (.onboard) with character references.

Usage:
$ ./xml_readable_combining.py layouts/*.onboard
"""

from unicodedata import combining

def replace_combining(s: str) -> str:
    return ''.join(
        f'&#x{ord(c):x};' if combining(c) else c
        for c in s)

def process_files(filenames: list[str]) -> None:
    for filename in filenames:
        print(f'Processing {filename}...')
        with open(filename, encoding='utf-8') as f_in:
            lines = f_in.readlines()

        with open(filename, 'w', encoding='utf-8') as f_out:
            for line in lines:
                f_out.write(replace_combining(line))

if __name__ == '__main__':
    import sys
    process_files(sys.argv[1:])
