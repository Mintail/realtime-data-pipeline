import time
from fetcher import fetch_price
from storage import append_price, init_db

def run_pipeline( sleep_seconds = 1 ):
    print( "Initializing DB..." )
    init_db()
    print( "Starting pipeline..." )

    while True:
        price, ts = fetch_price()
        if price is not None:
            append_price( ts, price )
            print( f"[Pipeline] {ts:.0f} → {price}" )
        time.sleep( sleep_seconds )

if __name__ == "__main__":
    run_pipeline()
