import httpx

async def fetch_and_map_random_value(api_url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        response.raise_for_status()
        data = response.json()

    original_value = data.get("random_number")
    if not isinstance(original_value, (int, float)):
        raise ValueError("API did not return a numeric value")

    # Map value from range (1, 100) to (0, 5)
    mapped_value = round((original_value - 1) * (5 / 99))

    return mapped_value

