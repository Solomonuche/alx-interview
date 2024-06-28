#!/usr/bin/python3
import sys
"""
Supplies a script that reads stdin line by line and computes metrics
"""
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        split_line = line.split(" ")

        if len(split_line) > 4:
            status_code = split_line[-2]
            size = int(split_line[-1])
            if status_code in status_codes.keys():
                status_codes[status_code] += 1
            file_size += size
            line_count += 1
        if line_count == 10:
            line_count = 0
            print('File size: {}'.format(file_size))

            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))
except Exception:
    pass
finally:
    print('File size: {}'.format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
