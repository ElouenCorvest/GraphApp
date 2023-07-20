import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def graph(y):
    fig, ax = plt.subplots()
    ax.plot([1,y], [1,2])
    ax.set_ylim(0, 10)
    return fig

col1, col2 = st.columns([1,1])

with col2:
    y=st.slider('hello', min_value=0, max_value=10, value=2,step=1)
    col2_1, col2_2 = st.columns([1,1])
    with col2_2:
        st.write("hello")
with col1:
    fig = graph(y)
    st.pyplot(fig)

code = f"""
    
    fig, ax = plt.subplots()
    ax.plot([1,{y}])
    ax.set_ylim(0, 10)
"""

st.code(code, language='python')