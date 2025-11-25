def detect_anomalies( df ):
    """Detect simple price or volatility anomalies."""
    alerts = []

    if df[ "zscore" ].iloc[ -1 ] > 3:
        alerts.append( "High positive deviation (z > 3)" )
    if df["zscore"].iloc[-1] < -3:
        alerts.append( "High negative deviation (z < -3)" )
    if df[ "volatility" ].iloc[ -1 ] > df[ "volatility" ].rolling( 100 ).mean().iloc[ -1 ] * 2:
        alerts.append( "Volatility spike detected" )

    return alerts
