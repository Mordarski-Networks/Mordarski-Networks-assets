"""
SPDX-License-Identifier: MIT
Copyright (c) 2024 Mordarski Networks
"""

# Modules
import platform
import subprocess
from datetime import datetime, timezone

# Functions
def main():
    """Copies UTC date to the clipboard"""
    utc_time = datetime.now(timezone.utc).strftime('%A, %B %d, %Y %I:%M:%S %p %Z')

    if platform.system() == "Windows":
        subprocess.run("clip", check=False, shell=True, input=utc_time.encode())
        return True
    if platform.system() == "Linux":
        subprocess.run("xclip -sel clip", check=False, shell=True, input=utc_time.encode())
        return True
    if platform.system() == "Darwin":
        subprocess.run("pbcopy", check=False, shell=True, input=utc_time.encode())
        return True
    return False

# Main
if __name__ == "__main__":
    if main():
        print("Copied UTC time to the clipboard.")
    else:
        print("This OS is not supported.")
