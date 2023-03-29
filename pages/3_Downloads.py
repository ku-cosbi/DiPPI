import streamlit as st
import pandas as pd
import numpy as np
from stmol import showmol, render_pdb
import py3Dmol
from datetime import datetime
from PIL import Image
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode


import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import base64
import json


#st.subheader('DiPPI:  Drugs in Protein Protein Interface')
original_title = '<p style="font-family:Trebuchet MS; color:#4682B4; font-size: 35px; font-weight:bold">DiPPI:  Drugs in Protein Protein Interface</p>'
st.markdown(original_title, unsafe_allow_html=True)
interfaces_df = pd.read_csv('data/interface_data.txt', sep='\t')
proteins_df = pd.read_csv('data/protein_summary.txt', sep='\t')
ligands_df = pd.read_csv('data/ligand_data.txt', sep='\t')
eliminated_df = pd.read_csv('data/eliminatedMolecules.txt', sep='\t')
interface_drugs_df = pd.read_csv('data/drugs_in_interface.txt', sep='\t')
interfaces_fda_df = pd.read_csv('data/interface_data_fda.txt', sep='\t')
proteins_fda_df = pd.read_csv('data/protein_summary_fda.txt', sep='\t')
ligands_fda_df = pd.read_csv('data/ligand_data_fda.txt', sep='\t')
#readme = pd.read_csv('data/readme.txt')
# Download code from here: https://discuss.streamlit.io/t/automatic-download-select-and-download-file-with-single-button-click/15141/3
# Downloaded on Jan 9, 2023
# buna da bak: https://stackoverflow.com/questions/73414235/download-multiple-files-in-streamlit


# From: https://docs.streamlit.io/library/api-reference/widgets/st.download_button,jan 9, 2023

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(sep='\t', index=False,encoding='utf-8')
def main():
    csv_int = convert_df(interfaces_df)
    csv_prot = convert_df(proteins_df)
    csv_lig = convert_df(ligands_df)
    csv_eliminated= convert_df(eliminated_df)
    csv_interface_drugs = convert_df(interface_drugs_df)
    csv_int_fda = convert_df(interfaces_fda_df)
    csv_prot_fda = convert_df(proteins_fda_df)
    csv_lig_fda = convert_df(ligands_fda_df)

    st.markdown("""
    <style>
    .big-font {
        font-size:17px ;
    }
    </style>
    """, unsafe_allow_html=True)


    original_title = '<p style="font-size: 20px;font-family:Trebuchet MS">Interface Dataset: Information about' \
                     ' residues for interfaces that have a bound drug-like ligand.</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.download_button(
        label="Download Interface Data as CSV",
        data=csv_int,
        file_name='interface_data.txt',
        mime='text/csv',
    )
    st.empty()
    st.empty()

    original_title = '<p style="font-size: 20px;font-family:Trebuchet MS">Interface Dataset FDA-approved drugs subset</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.download_button(
        label="Download Interface Data (FDA-approved subset) as CSV",
        data=csv_int_fda,
        file_name='interface_data_fda.txt',
        mime='text/csv',
    )
    st.empty()
    st.empty()

    original_title = '<p style="font-size: 20px;font-family:Trebuchet MS">Protein Dataset: Contains summary information about PDB structures.</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.download_button(
        label="Download Summary Data as CSV",
        data=csv_prot,
        file_name='protein_summary.txt',
        mime='text/csv',
    )

    st.empty()
    st.empty()

    original_title = '<p style="font-size: 20px;font-family:Trebuchet MS">Protein Dataset FDA-approved drugs subset</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.download_button(
        label="Download Summary Data (FDA-approved subset) as CSV",
        data=csv_prot_fda,
        file_name='protein_summary_fda.txt',
        mime='text/csv',
    )


    st.empty()
    st.empty()
    original_title = '<p style="font-size: 20px;font-family:Trebuchet MS">Ligand Dataset FDA-approved drugs subset</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.download_button(
        label="Download Ligand Data as CSV",
        data=csv_lig,
        file_name='ligand_data.txt',
        mime='text/csv',
    )
    st.empty()
    st.empty()
    original_title = '<p style="font-size: 20px;font-family:Trebuchet MS"> Ligand Dataset FDA-approved drugs subset</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.download_button(
        label="Download Ligand Data (FDA-approved subset) as CSV",
        data=csv_lig_fda,
        file_name='ligand_data_fda.txt',
        mime='text/csv',
    )
    st.empty()
    st.empty()
    original_title = '<p style="font-size: 20px;font-family:Trebuchet MS">Eliminated Molecules: Eliminated small-molecule list</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.download_button(
        label="Download Eliminated Molecule Data as CSV",
        data=csv_eliminated,
        file_name='eliminatedMolecules.txt',
        mime='text/csv',
    )

    st.empty()
    st.empty()
    original_title = '<p style="font-size: 20px;font-family:Trebuchet MS">List of Drugs that are found in the interfaces: 2,214 small-molecules that are found to be binding to at least one interface region</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.download_button(
        label="Download Ligands as CSV",
        data=csv_interface_drugs,
        file_name='drugs_in_interface.txt',
        mime='text/csv',
    )




main()