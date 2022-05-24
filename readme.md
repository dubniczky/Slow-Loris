# Slow Loris DoS Attack

Python implementation of the Slow Loris denial of service attack

[[_TOC_]]

## Disclaimer

This tool is intended for demonstrational purposes, so only use against your own systems or against ones you have authorization for. I take no responsibility for your actions.

## Introduction

Slow Loris is a low-bandwidth denial of service attack, utilizing lots of connections to the same host and keeping them alive, while sending minimal data.

When receiving a GET request, the server will wait until an empty line is sent to transmit the requested resource. We don't want any data in return, only to occupy the given connection.

The HTTP standard does not define a limit to the header count, but most frameworks have a limit defined in bytes, after which they will abort the connection. A default NodeJS 14+ setup has an upper limit of 16 kb. Using our current header size (average 15 bytes per header), it will take ~1,000 headers to fill this up.

If we consider an average of 5 seconds as a timeout period, one connection can occupy a channel for about 5000 seconds, or around 1 hour 23 minutes. This happens while sending only 16kb of data.

This attack is most effective if:

- The host has a hard limited number of possible connections at a time
- The host has no load balacing or firewalls
- The host has no DoS protection
- The attack is carried out by a distributed network of systems

## Requirements

- Python 3.10+
- Optional: NodeJS 16+

## Usage

```bash
python main.py HOST_IP [OPTIONS]
```

Help:

Use the following command to get a list of options.

```bash
python main.py -h
```

## Demo server

The demo server is written in native NodeJS with zero dependencies. You can start it by using:

```bash
node testserver.node PORT
```

> Please not that on UNIX systems, root privileges are required to run this script on port lower thatn 1024

## License

[MIT](./LICENSE)