#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:01:56 2021

@author: shimingyu
"""
import pandas as pd
import altair as alt
import numpy as np

import streamlit as st

st.title("Data Information")

st.markdown('presented by Mingyu Shi, https://github.com/mingyus3?tab=repositories',unsafe_allow_html=True)

f = st.file_uploader("Upload Files", type = ['csv'])


def can_be_numeric(c):
    try:
        pd.to_numeric(df[c])
        return True
    except:
        return False

if f is not None:
    df = pd.read_csv(f)

        
    df = df.applymap(lambda x: np.nan if x == " " else x)
    
        
    good_cols = [c for c in df.columns if can_be_numeric(c)]
    df = df[good_cols].apply(pd.to_numeric, axis = 0)
    
    st.write(df)
    
    s = st.slider(("number of rows selected"),0,len(df),[0,len(df)-1])
    st.write(f"The range of the row you choose is {s}")
    
    a = st.selectbox("choose a x value", good_cols)
    b = st.selectbox("choose a y value", good_cols)
    
    r = list(s)
    
    plotrange = range(r[0],r[1])
    
    df = df.iloc[plotrange]

    c = alt.Chart(df).mark_circle().encode(
        x = str(a),
        y = str(b),
        tooltip = [str(a),str(b)]
    )
    st.altair_chart(c, use_container_width=True)
    

