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
        "-f",
        "--filter",
        nargs=2,
        type=str,
        help="Choose a filter. You should separate the filters by a space.",
    )
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    if args.filter[0] != ["search", "youtube"]:
        parser.error(
            "The argument is incorrect. The argument should be search or youtube."
        )
    elif args.filter:
        copy(generate_filter(args.filter[0], args.filter[1]))
        print("Copied filter to the clipboard.")
    else:
        print("This OS is not supported.")


def generate_filter(arg1, arg2):
    """Generate a filter.

    Give a sequence of websites separated by a space to generate the filter.
    """
    string = re.sub(" ", " ", arg2).lower().split()
    filter_list = []

    if arg1 == "search":
        for i in string:
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
    if arg1 == "youtube":
        for i in string:
            filter_list.extend(
                [
                    f'www.youtube.com##ytd-browse[page-subtype="home"] a[href*="@{i}"]:upward(ytd-rich-item-renderer)',
                    f'www.youtube.com##ytd-search a[href*="@{i}"]:upward(ytd-video-renderer,ytd-channel-renderer)',
                    f'www.youtube.com##ytd-shorts:matches-path(/shorts) a.ytd-reel-player-header-renderer[href*="@{i}"]:upward(ytd-reel-video-renderer)',
                    f'm.youtube.com##ytm-browse a[href*="@{i}"]:upward(ytm-rich-item-renderer)',
                    f'm.youtube.com##ytm-search a[href*="@{i}"]:upward(ytm-video-with-context-renderer,ytm-compact-channel-renderer)',
                    "youtube.com##ytd-rich-grid-row, #contents.ytd-rich-grid-row:style(display:contents !important;)",
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
