import streamlit as st
from PIL import Image

import pandas as pd
import numpy as np
from stmol import showmol, render_pdb
import py3Dmol
from datetime import datetime
from PIL import Image
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode




from streamlit.components.v1 import html
import streamlit as st
from PIL import Image



PAGE_CONFIG = {"page_title":"DiPPI",

               "layout":"wide",
               "initial_sidebar_state":"auto"}
st.set_page_config(**PAGE_CONFIG)
#st.subheader('DiPPI:  Drugs in Protein Protein Interface')
#st.markdown('Welcome to **D**rugs **i**n **P**rotein-**P**rotein **I**nterface Website!')
# Fontsize and color :https://discuss.streamlit.io/t/change-font-size-and-font-color/12377, on Jan 4, 2023
# get colors from theme config file, or set the colours to altair standards


new_title = '<p style="font-family:Trebuchet MS; text-align: center; color:#4682B4; font-size: 36px;">Welcome to <strong>D</strong>rugs <strong>i</strong>n <strong>P</strong>rotein-<strong>P</strong>rotein <strong>I</strong>nterfaces Website</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.text("")
st.write('lsfjsl')


st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")


def nav_page(page_name, timeout_secs=1000):
    """
    From https://github.com/streamlit/streamlit/issues/4832, on Jan 4, 2023

    """
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.endsWith("/" + page_name)) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


col1, col2 = st.columns(2)
with col1:
    if st.button("Query by Interface"):
        nav_page("Query_by_Interface")

with col2:
    if st.button("Query by Drug"):
        nav_page("Query_by_Drug")

# Markdown code from this webpage: https://discuss.streamlit.io/t/how-to-build-an-unique-button-in-streamlit-web-program/12012/22,
# on Jan 4, 2023
# For content alignment this can be visited too: https://discuss.streamlit.io/t/alignment-of-content/29894/3


m = st.markdown(""" 
 <style>
 div.stButton > button:first-child {
    background-color:#4682B4;
	border-radius:3px; # 10px 10px 10px 10px
	border:1px solid #4682B4;
	height:3em;
    width:23.4em; # rougly centers the buttons
	display:inline-block;
	cursor:pointer;
	color:white;
	font-family:Trebuchet MS;
	font-size:25px;
	font-weight:bold;
	padding:12px 24px;
	text-decoration:none;
	text-shadow:0px -1px 0px #4682B4;
}
</style>""", unsafe_allow_html=True)


col1, col2  = st.columns(2)
with col1:
    image1 = Image.open("data/welcome1.png")
    st.image(image1)
    st.markdown(""" 
     <style>
      .center
      { 
      font-family:Trebuchet MS; font-size:14px;text-align: center
      }
    </style>""", unsafe_allow_html=True)

with col2:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    new_title = '<p style="font-family:Trebuchet MS; text-align: center; color:#4682B4; font-size: 20px;">DiPPI is a website for the search of interface bound drug-like molecules, and FDA-approved drugs.' \
                'It has two modules, one for the query of drug-boung interfaces via ligand ID, and the other one is through the PDB ID of the investigated protein structure. We also provide clustering and characterization' \
                'for selected ligands and interfaces. Users can enter single query or dpwnload batch data we provided.Our website provides an easy-to-follow scheme to guide users on the selection of alternative drugs or targets ' \
                'in a possible drug repurposing study through its well-curated and clustered interface and drug-like molecule data.</p>'
    st.markdown(new_title, unsafe_allow_html=True)

new_title = '<p style="font-family:Trebuchet MS; text-align: center; color:#4682B4; font-size: 16px;">For more information about how to use this website, please visit User Guide Page in the navigation panel.</p>'
st.markdown(new_title, unsafe_allow_html=True)

