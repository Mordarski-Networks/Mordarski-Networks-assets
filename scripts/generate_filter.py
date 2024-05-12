# SPDX-License-Identifier: MIT
# Copyright (c) 2024 Mordarski Networks

"""This script generates a filter and copies it to the clipboard."""
import argparse
import platform
import re
import subprocess
import sys


def main():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog="generate_filter", description="Generate a filter."
    )
    parser.add_argument(
        "-w",
        "--website",
        help="Give a sequence of websites separated by a space to generate the filter.",
    )
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    if copy(generate_filter(args.website)):
        print("Copied filter to the clipboard.")
    else:
        print("This OS is not supported.")


def generate_filter(website):
    """Generate a filter.

    Give a sequence of websites separated by a space to generate the filter.
    """
    website_list = re.sub(" ", " ", website).lower().split()
    filter_list = []

    for i in website_list:
        filter_list.extend(
            [
                f'bing.com#?#[id$="results"] cite:has-text({i}):upward(li)',
                f'bing.com#?#a[href*="{i}"]:upward(li[data-idx][style^="width"])',
                f'bing.com#?#[id*="video"] > [href*="{i}"]:upward(.dg_u)',
                f'bing.com##.news-card[url*="{i}"]',
                f'www.google.*##.g:has(a[href*="{i}"])',
                f'www.google.*##a[href*="{i}"]:upward(1)',
                f'www.google.*##[data-lpage*="{i}"]',
                f'duckduckgo.com##ol.react-results--main a[href*="{i}"]:upward(article)',
                f'duckduckgo.com##.tile-wrap a[href*="{i}"]:upward(.tile)',
            ]
        )

    filter_list = "\n".join(filter_list)
    return filter_list


def copy(string):
    """Copy a given argument to the clipboard.

    The argument should be a string.
    """
    os_dictionary = {"Windows": "clip", "Linux": "xclip -sel clip", "Darwin": "pbcopy"}

    for keys, values in os_dictionary.items():
        if platform.system() == keys:
            subprocess.run(values, check=False, shell=False, input=string.encode())
            return True

    return False


if __name__ == "__main__":
    main()
