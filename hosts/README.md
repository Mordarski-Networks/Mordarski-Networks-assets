# Mordarski Networks assets hosts file

A hosts file equivalent of *main.txt*. For right now I will not put *extra.txt* and *dev.txt* websites into *hosts.txt*.

## What is a hosts file?

Wikipedia has a pretty good article on what a hosts file is. You can read the article [here](https://en.wikipedia.org/wiki/Hosts_(file)).

## How do I add this to my hosts file?

For Windows 10 and Windows 11, rename *hosts.txt* to hosts (Without .txt) and overwrite the file

```
C:\Windows\System32\drivers\etc\hosts
```

For Linux, rename *hosts.txt* to hosts (Without .txt) and overwrite the file

```
/etc/hosts
```

For MacOS, rename *hosts.txt* to hosts (Without .txt) and overwrite the file

```
/private/etc/hosts
```

*Note: If you don't want to overwrite the hosts file, you can simply copy the text in hosts.txt and put it into your own hosts file. There is a 0.0.0.0 version available in the zero folder.*

## Is there any GUI programs that allow you to edit a hosts file?

For Windows, you can use a program called [HostsMan](https://www.abelhadigital.com/hostsman/). It allows you to export and import hosts files around the Internet. It hasn't been updated since 2017 but still works for editing and updating hosts files.

## Special thanks to

- https://someonewhocares.org/hosts/

Without this information, I wouldn't be able to make this hosts file.
