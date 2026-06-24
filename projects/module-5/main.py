import argparse
import asyncio
import time
import json
from dataclasses import asdict

from services.user_service import UserService
from utils.file_helper import save_users
from utils.logger import logger


async def run(user_ids):

    start = time.perf_counter()

    service = UserService()

    users = await service.fetch_users(
        user_ids
    )

    save_users(users)

    elapsed = (
        time.perf_counter() - start
    )

    print(
        f"\nFetched {len(users)} users"
    )

    print(
        f"Execution Time: "
        f"{elapsed:.2f} seconds"
    )

    print(json.dumps(
        [asdict(user) for user in users],
        indent=4
    ))
    
    logger.info(
        f"Fetched {len(users)} users"
    )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--ids",
        nargs="+",
        type=int,
        required=True,
        help="User IDs"
    )

    args = parser.parse_args()

    asyncio.run(
        run(args.ids)
    )


if __name__ == "__main__":
    main()
