# Contributing Guide Lines

Before contributing to this filter list, read the following below.

---

## Reporting Issues

You can report filter list issues [here](https://github.com/MordarskiNET/mordnet-assets/issues).

## Submitting Contributions

You can create a pull request [here](https://github.com/MordarskiNET/mordnet-assets/pulls).

## Code Formatting

### Title

Each title should start with a name, followed by a info section and syntax usage section.

```
!--- Example Title ---!
! Info: example.com
! Syntax: ||example.net^$all
```

### Subtitle

After the title, there should be a subtitle for each sub section.

```
!--- Example Title ---!
! Info: example.com
! Syntax: ||example.net^$all

! Example Subtitle
```

### Filter Rules

Every filter rule should go below a subtitle and be correctly placed in the corresponding section.

```
!--- Domain Blocking ---!
! Info: example.com
! Syntax: ||example.net^$all

! Blocks example.net
||example.net^$all

! Blocks example.org
||example.org^$all

!--- Filter Seach Results ---!
! Info: example.com
! Syntax: example.net##

! Blocks example.net from search results
example.net##

! Blocks example.org from search results
example.org##
```

## Website Requests

If you want to suggest for a website to be added to the filter list, you can do it [here](https://github.com/MordarskiNET/mordnet-assets/discussions).
