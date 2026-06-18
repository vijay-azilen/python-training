import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a network delay
    print("Data fetched successfully!")

asyncio.run(fetch_data())
