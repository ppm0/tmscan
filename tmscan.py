import argparse
import logging
import time

from tinyman.v1.client import TinymanMainnetClient
from tinyman.v1.pools import Pool

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()],
    )
    client = TinymanMainnetClient()
    parser = argparse.ArgumentParser()
    parser.add_argument("--asset1", type=int, required=True)
    parser.add_argument("--asset2", type=int, default=0)
    args = parser.parse_args()
    a1 = client.fetch_asset(args.asset1)
    a2 = client.fetch_asset(args.asset2)
    while True:
        p = Pool(client, a1, a2)
        logging.log(logging.INFO,
                    {"price": (p.asset1_price, p.asset2_price),
                     "reserve": (a1(p.asset1_reserves), a2(p.asset2_reserves))})
        time.sleep(0.9)
