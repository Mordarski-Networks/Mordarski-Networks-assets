# Contributing Guide Lines

Before contributing to this filter list, read the following below.

---

## Reporting Issues

You can report filter list issues [here](https://github.com/Mordarski-Networks/Mordarski-Networks-assets/issues).

## Submitting Contributions

You can create a pull request [here](https://github.com/Mordarski-Networks/Mordarski-Networks-assets/pulls).

## Code Formatting

### Title

Each title should start with a name, followed by a info section and syntax usage section.

```adblock
!--- Example Title ---!
! Info: example.com
! Syntax: ||example.net^$all
```

### Subtitle

After the title, there should be a subtitle for each sub section. This sub section is for issue numbers from GitHub or comments.

```adblock
!--- Example Title ---!
! Info: example.com
! Syntax: ||example.net^$all

! Issue number or comment
```

### Filter Rules

Every filter rule should go below a subtitle and be correctly placed in the corresponding section.

```adblock
!--- Domain Blocking ---!
! Info: example.com
! Syntax: ||example.net^$all

! Issue number or comment
||example.net^$all

! Issue number or comment
||example.org^$all

!--- Filter Seach Results ---!
! Info: example.com
! Syntax: example.net##

! Issue number or comment
example.net##

! Issue number or comment
example.org##
```

### Hosts File

```hosts
127.0.0.1 example.net
127.0.0.1 www.example.net
```

The hosts file should have both the non www website and the www website because the hosts file does not understand that `example.net` is the same website as `www.example.net`.

## Updating Last Modified Timestamp

To update the last modified timestamp, run [get_utc_date.py](https://github.com/Mordarski-Networks/Mordarski-Networks-assets/blob/main/scripts/get_utc_date.py) and replace the old timestamp by selecting it and pasting the new timestamp on the selected text.

*Note: You will need to install [Python 3](https://www.python.org/) on your computer to run the [get_utc_date.py](https://github.com/Mordarski-Networks/Mordarski-Networks-assets/blob/main/scripts/get_utc_date.py) script.*

## Website Requests

If you want to suggest for a website to be added to the filter list, you can do it [here](https://github.com/Mordarski-Networks/Mordarski-Networks-assets/discussions).
