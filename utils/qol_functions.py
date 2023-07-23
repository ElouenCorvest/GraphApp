import streamlit as st

def center_vertically():
    st.write(
            """<style>
            [data-testid="stHorizontalBlock"] {
                align-items: center;
            }
            </style>
            """,
            unsafe_allow_html=True
        )