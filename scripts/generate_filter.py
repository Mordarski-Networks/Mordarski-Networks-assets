# SPDX-License-Identifier: MIT
# Copyright (c) 2024 Mordarski Networks

"""This script generates a filter and copies it to the clipboard."""
import platform
import subprocess
import re

def main():
    """This function generates a filter."""
    websites = input("Enter websites separated by spaces: ")
    websites_list = re.sub(" ", " ", websites).lower().split()
    filter_list = []

    for i in websites_list:
        filter_list.extend(
            [
                f"bing.com#?#[id$=\"results\"] cite:has-text({i}):upward(li)",
                f"bing.com#?#a[href*=\"{i}\"]:upward(li[data-idx][style^=\"width\"])",
                f"bing.com#?#[id*=\"video\"] > [href*=\"{i}\"]:upward(.dg_u)",
                f"bing.com##.news-card[url*=\"{i}\"]",
                f"www.google.*##.g:has(a[href*=\"{i}\"])",
                f"www.google.*##a[href*=\"{i}\"]:upward(1)",
                f"www.google.*##[data-lpage*=\"{i}\"]",
                f"duckduckgo.com##ol.react-results--main a[href*=\"{i}\"]:upward(article)",
                f"duckduckgo.com##.tile-wrap a[href*=\"{i}\"]:upward(.tile)"
            ]
        )

    filter_list = "\n".join(filter_list)

    if platform.system() == "Windows":
        subprocess.run("clip", check=False, shell=True, input=filter_list.encode())
        return True
    if platform.system() == "Linux":
        subprocess.run("xclip -sel clip", check=False, shell=True, input=filter_list.encode())
        return True
    if platform.system() == "Darwin":
        subprocess.run("pbcopy", check=False, shell=True, input=filter_list.encode())
        return True
    return False

if __name__ == "__main__":
    if main():
        print("Copied filter to the clipboard.")
    else:
        print("This OS is not supported.")
