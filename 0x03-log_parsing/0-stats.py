#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""


if __name__ == '__main__':

    import sys

    def print_stats(status_codes, file_size):
        """ Print the statistics """
        print("File size: {:d}".format(file_size))
        for code, val in sorted(status_codes.items()):
            if val:
                print("{:s}: {:d}".format(code, val))

    status_codes = {"200": 0,
                    "301": 0,
                    "400": 0,
                    "401": 0,
                    "403": 0,
                    "404": 0,
                    "405": 0,
                    "500": 0
                    }
    file_size = 0
    count_lines = 0

    try:
        for line in sys.stdin:
            if count_lines != 0 and count_lines % 10 == 0:
                print_stats(status_codes, file_size)
            count_lines += 1
            parsed_line = line.split()
            try:
                status_code = parsed_line[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                    file_size += int(parsed_line[-1])
            except Exception:
                pass
        print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        """ Keyboard interruption, print from the beginning """
        print_stats(status_codes, file_size)
        raise
