import requests
import time

API_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

def fetch_price():
    """Fetch latest BTC/USDT price from Binance public API."""
    try:
        resp = requests.get( API_URL, timeout = 3 )
        resp.raise_for_status()
        data = resp.json()
        return float( data[ "price" ] ), time.time()
    except Exception as e:
        print( f"[Fetcher] Error fetching data: {e}" )
        return None, None
