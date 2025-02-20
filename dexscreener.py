import requests

DEX_API_URL = "https://api.dexscreener.com/token-profiles/latest/v1"

def fetch_tokens():
    """Fetch token data from DexScreener API."""
    try:
        response = requests.get(DEX_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("pairs", [])
    except Exception as e:
        print(f"Error fetching token data: {e}")
        return []
# import requests

# DEX_API_URL = "https://api.dexscreener.com/latest/dex/pairs/solana"

# def fetch_tokens():
#     """Fetch token data from DexScreener API for Solana."""
#     try:
#         response = requests.get(DEX_API_URL, timeout=10)
#         response.raise_for_status()
#         data = response.json()
#         return data.get("pairs", [])
#     except Exception as e:
#         print(f"Error fetching token data: {e}")
#         return []