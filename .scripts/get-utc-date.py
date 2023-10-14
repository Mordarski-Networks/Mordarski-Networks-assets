# MIT License
#
# Copyright (c) 2023 Mordarski Networks
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

import os
import subprocess
from datetime import datetime, timezone

utc_time = datetime.now(timezone.utc).strftime('%A, %B %d, %Y %I:%M:%S %p %Z')

# Copy utc_time to the clipboard
if os.name == 'nt':
    subprocess.run("clip", check=False, shell=True, input=utc_time.encode())
    print("Copied UTC time to the clipboard.")
elif os.name == 'posix':
    subprocess.run("xclip", check=False, shell=True, input=utc_time.encode())
    print("Copied UTC time to the clipboard.")
