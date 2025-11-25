import pandas as pd

def compute_features( df: pd.DataFrame ):
    """Compute simple features for analytics and signals."""
    df[ "price" ] = pd.to_numeric( df[ "price" ], errors = "coerce" )
    df[ "return" ] = df[ "price" ].pct_change()
    df[ "volatility" ] = df[ "return" ].rolling( 20 ).std()
    df[ "zscore" ] = ( df[ "price" ] - df[ "price" ].rolling( 20 ).mean() ) / df[ "price" ].rolling( 20 ).std()
    return df
