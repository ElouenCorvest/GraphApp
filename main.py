import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils.graph_ui import *

col1, col2 = st.columns([1,1])

with col2:
    graph_type = st.selectbox(
                    label="What type of graph do you want to create?",
                    options=["Line Chart", "Boxplot"]
    )

    if graph_type == 'Line Chart':
        fig, code = linegraph_ui()

with col1:
    st.pyplot(fig)

st.code(code, language='python')
st.info('This is a purely informational message', icon="ℹ️")