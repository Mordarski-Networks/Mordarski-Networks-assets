# SPDX-License-Identifier: MIT
# Copyright (c) 2024 Mordarski Networks

"""This script copies UTC date to the clipboard."""
import platform
import subprocess
from datetime import datetime, timezone


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
    utc_time = datetime.now(timezone.utc).strftime("%A, %B %d, %Y %I:%M:%S %p %Z")
    if copy(utc_time):
        print("Copied UTC time to the clipboard.")
    else:
        print("This OS is not supported.")
