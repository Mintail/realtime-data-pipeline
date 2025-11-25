import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

import streamlit as st
from diagnostics.analytics import compute_diagnostics
from diagnostics.alerts import detect_anomalies
from models.baseline_signal import compute_signal


st.title( "Real-Time Data Pipeline Dashboard" )

df = compute_diagnostics()

if df.empty:
    st.warning( "No data available yet. Please start the pipeline." )
else:
    st.subheader( "Latest Price" )
    st.write( df[ "price" ].iloc[ -1 ] )

    st.subheader( "Signal" )
    st.write( compute_signal( df ) )

    st.subheader( "Diagnostics" )
    st.line_chart( df[ "price" ] )
    st.line_chart( df[ "return" ] )
    st.line_chart( df[ "volatility" ] )
    st.line_chart( df[ "zscore" ] )

    st.subheader( "Alerts" )
    alerts = detect_anomalies( df )
    if alerts:
        for a in alerts:
            st.error( a )
    else:
        st.success( "No anomalies detected." )
