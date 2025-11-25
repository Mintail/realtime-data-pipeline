def compute_signal( df ):
    """
    A simple baseline signal:
    - Buy when price is below rolling mean (z < -1)
    - Sell when price is above rolling mean (z > 1)
    """
    if df.empty or df[ "zscore" ].isna().all():
        return "neutral"

    last_z = df[ "zscore" ].iloc[ -1 ]

    if last_z < -1:
        return "buy"
    elif last_z > 1:
        return "sell"
    else:
        return "neutral"
