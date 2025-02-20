
MIN_MARKET_CAP = 0
MIN_DAILY_VOLUME = 0
MIN_PRICE_CHANGE_24h = 0      # e.g., percent change
MIN_LIQUIDITY_USD = 0
MIN_BUY_SELL_RATIO = 0

def token_meets_criteria(token):
    try:
        market_cap = token.get("marketCap", 0)
        daily_volume = token.get("volume", {}).get("24h", 0)
        price_change = token.get("priceChange", {}).get("24h", 0)
        liquidity = token.get("liquidity", {}).get("usd", 0)
        txns = token.get("txns", {})
        buys = txns.get("buys", 0)
        sells = txns.get("sells", 0)
        buy_sell_ratio = (buys / sells) if sells > 0 else float("inf")

        return (market_cap >= MIN_MARKET_CAP and
                daily_volume >= MIN_DAILY_VOLUME and
                abs(price_change) >= MIN_PRICE_CHANGE_24h and
                liquidity >= MIN_LIQUIDITY_USD and
                buy_sell_ratio >= MIN_BUY_SELL_RATIO)
    except Exception as e:
        print(f"Error in filtering token: {e}")
        return False
