import streamlit as st
from utils.graph_functions import *
from utils.qol_functions import *
from utils.graph_code import *

def linegraph_ui():
    line_number = st.number_input(
            label='Number of lines',
            min_value=1,
            step=1,
        )
    
    with st.expander(
           label='Axis Change'
    ):
        st.write('#### X-Axis:')

        st.write('Make limits of x relative to data:')

        col_axis1, col_axis2, col_axis3 = st.columns([0.5,0.2,1])

        with col_axis1:
            center_vertically()
            st.write('Left limit')

        with col_axis2:
            center_vertically()
            relative_xlim_bool_left = st.checkbox(
                label='relative_xlim_bool_left',
                label_visibility='collapsed',
                value=True
            )
            
        with col_axis3:
            relative_xlim_round_left = st.selectbox(
                label='Round to nearest:',
                options=['0','5','2'],
                index=0,
                help='Round your number to the nearest number with an ending of: -0, -5, -2',
                disabled=not(relative_xlim_bool_left),
                key=1
            )
    
        col_axis1, col_axis2, col_axis3 = st.columns([0.5,0.2,1])

        with col_axis1:
            center_vertically()
            st.write('Right limit')

        with col_axis2:
            center_vertically()
            relative_xlim_bool_right = st.checkbox(
                label='relative_xlim_bool_right',
                label_visibility='collapsed',
                value=True
            )
            
        with col_axis3:
            relative_xlim_round_right = st.selectbox(
                label='Round to nearest:',
                options=['0','5','2'],
                index=0,
                help='Round your number to the nearest number with an ending of: -0, -5, -2',
                disabled=not(relative_xlim_bool_right)
            )

        if not(relative_xlim_bool_left):
            abosolute_xlim_left = st.number_input(
                label='Absolute left limit',
                value=0.000
            )
        else:
            abosolute_xlim_left = None

        if not(relative_xlim_bool_right):
            abosolute_xlim_right = st.number_input(
                label='Absolute right limit',
                value=line_number
            )
        else:
            abosolute_xlim_right = None

    fig=linegraph(
        line_number=line_number,
        xlim_abosulute_left=abosolute_xlim_left,
        xlim_abosulute_right=abosolute_xlim_right,
    )
    code = linegraph_code(
        line_number=line_number,
        relative_xlim_round_left=relative_xlim_round_left,
        relative_xlim_round_right=relative_xlim_round_right,
        abosolute_xlim_left=abosolute_xlim_left,
        abosolute_xlim_right=abosolute_xlim_right
    )

    return fig, code