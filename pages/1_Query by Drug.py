
import streamlit as st
import pandas as pd
import numpy as np
import ast
from stmol import showmol, render_pdb
import py3Dmol
from datetime import datetime
from PIL import Image
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode,GridUpdateMode
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import base64
import json

#st.subheader('DiPPI:  Drugs in Protein Protein Interface')
original_title = '<p style="font-family:Trebuchet MS; color:#4682B4; font-size: 35px; font-weight:bold">DiPPI:  Drugs in Protein Protein Interface</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(""" 
 <style>
  .main-font
  { 
  font-family:Trebuchet MS; font-size:16px;text-align: justify
  }
</style>""", unsafe_allow_html=True)
# Read Data
drugs_in_interface = pd.read_csv('data/drugs_in_interface.txt', sep='\t')
drugs_in_interface.drop(columns = 'FDA approved', inplace=True)
proteins_df = pd.read_csv('data/protein_summary.txt', sep='\t')
proteins_df['Ligand_ID'] = proteins_df['Ligand_ID'].apply(lambda  x:x.split(','))
proteins_df['Ligand_ID'] = proteins_df['Ligand_ID'].apply(lambda  x:[i.strip() for i in x])
ligands_df = pd.read_csv('data/ligand_data.txt', sep = '\t')
ligands_df  = ligands_df.merge(drugs_in_interface, left_on = ['Ligand ID'], right_on =['ligand_id'], how ='right')
ligands_df.drop(columns = ['ligand_id'], inplace=True)

ligands_df_sub =ligands_df[['Ligand ID', 'FDA approved', 'SMILES']]
ligands_df_sub  = ligands_df_sub.merge(drugs_in_interface, left_on = 'Ligand ID' , right_on ='ligand_id', how ='right')
ligands_df_sub.drop(columns = ['ligand_id'], inplace=True)
# Fix Table
proteins_df = proteins_df.explode('Ligand_ID')
proteins_df.reset_index(inplace=True)
proteins_df.drop(columns=['index'], inplace=True)
proteins_df['Interface_ID'] = proteins_df.Interface_ID.apply(lambda x: x.split(',') if ',' in x else x)

display_df = proteins_df.groupby('Ligand_ID').agg({'PDB_ID': list, 'Interface_ID': list})
display_df = display_df.reset_index()
display_df.Interface_ID = display_df.Interface_ID.apply(lambda x: [item for sublist in [[item] if type(item) is not list else item for item in x] for item in sublist])
display_df.Interface_ID = display_df.Interface_ID.apply(lambda x: [i.strip() for i in x])
display_df = display_df.merge(ligands_df_sub, left_on='Ligand_ID', right_on='Ligand ID', how='left')
display_df['interface_count'] = [len(i) for i in display_df.Interface_ID]
display_df['pdb_count'] = [len(i) for i in display_df.PDB_ID]
display_df.PDB_ID = display_df.PDB_ID.apply(lambda x: ', '.join(x))
display_df.Interface_ID = display_df.Interface_ID.apply(lambda x: ', '.join(x))
display_df.drop(columns = ['Ligand_ID'], inplace=True)
selection = st.selectbox('Filter by', ("Filter by Ligand ID", "Filter by SMILES"))
if selection == 'Filter by Ligand ID':
    ligand_selection = st.multiselect("Filter by ligand ID", ligands_df['Ligand ID'])
    if len(ligand_selection) > 0:
        display_df = display_df[(display_df['Ligand ID'].isin(ligand_selection))]
    else:
        display_df = pd.DataFrame(columns  = display_df.columns)
elif selection == 'Filter by SMILES':
    ligand_selection = st.multiselect("Filter SMILES", ligands_df['SMILES'])
    if len(ligand_selection) > 0:
        display_df = display_df[(display_df['SMILES'].isin(ligand_selection))]
    else:
        display_df = pd.DataFrame(columns  = display_df.columns)

if len(display_df) != 0:

    int_builder = GridOptionsBuilder.from_dataframe(display_df[['Ligand ID', 'SMILES', 'PDB_ID',  'pdb_count','Interface_ID', 'interface_count', 'FDA approved']])
    int_builder.configure_default_column(editable=False, filterable=True, cellStyle={'text-align': 'center'})
    int_builder.configure_column("PDB_ID", header_name="PDB ID")
    int_builder.configure_column("pdb_count", header_name="PDB Structure Count")
    int_builder.configure_column('Interface_ID', header_name="Interface ID")
    int_builder.configure_column("interface_count", header_name="Interface Count")
    int_builder.configure_column("FDA approved", header_name="FDA Approved")
    int_builder.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
    int_builder.configure_selection(selection_mode='multiple', use_checkbox=True)
    st.markdown(f'<p class="main-font">List of selected ligands:</p>', unsafe_allow_html=True)

    gridoptions = int_builder.build()
    with st.spinner('Loading data...'):
        int_return = AgGrid(display_df,
                            width='100%',
                            height=(len(display_df) + 4) * 35.2 + 3,
                            theme='balham',
                            enable_enterprise_modules=False,
                            gridOptions=gridoptions,
                            fit_columns_on_grid_load=True,
                            update_mode=GridUpdateMode.SELECTION_CHANGED, # or MODEL_CHANGED
                            custom_css={".ag-header-cell-label": {"justify-content": "center;"}})

    # About selection: https://medium.com/@hhilalkocak/streamlit-aggrid-6dbbab3afe03
    # https://discuss.streamlit.io/t/aggrid-selection-clears-after-clicking-checkbox/29955/3
    # Downloaded on Jan 9, 2023
    if int_return["selected_rows"] != []:
        with st.spinner('Loading data...'):
            st.markdown(f'<p class="main-font">Detailed view of ligand information</p>', unsafe_allow_html=True)
            selected_row = int_return["selected_rows"]


        selected_df = pd.DataFrame(selected_row, columns=display_df.columns)
        selected_df.drop(columns=['FDA approved'], inplace=True)
        ligands_df.drop(columns = ['SMILES'], inplace=True)
        selected_df = selected_df.merge(ligands_df, on=['Ligand ID'], how ='left')
        column_names = ['PDB ID', 'Interface ID', 'Ligand ID', 'SMILES','Interface Count','PDB Structure Count']
        column_names = column_names + list(selected_df.columns[6:])
        selected_df = selected_df.rename(columns=lambda x: x.strip())
        selected_df.columns = column_names
        ordered = ['Ligand ID', 'SMILES'] + list(selected_df.columns[10:]) + ['FDA approved', 'Source Database', 'ECFP4 Members','Pharmacophore Members', 'PDB ID','PDB Structure Count','Interface ID','Interface Count']

        selected_df = selected_df[ordered]

        int_builder = GridOptionsBuilder.from_dataframe(selected_df)
        int_builder.configure_default_column(editable=False, filterable=True, cellStyle={'text-align': 'center'})
        int_builder.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
        int_builder.configure_selection(selection_mode='multiple', use_checkbox=True)
        gridoptions = int_builder.build()
        with st.spinner('Loading data...'):
            int_return = AgGrid(selected_df,
                            width='100%',
                            height=(len(selected_df) + 4) * 35.2 + 3,
                            theme='balham',
                            enable_enterprise_modules=False,
                            gridOptions=gridoptions,
                            fit_columns_on_grid_load=False,
                            update_mode=GridUpdateMode.SELECTION_CHANGED, # or MODEL_CHANGED
                            custom_css={".ag-header-cell-label": {"justify-content": "center"}})
        #st.dataframe(selected_df)



        import streamlit as st
        import os
        import base64

        import streamlit as st
        from rdkit import Chem
        from rdkit.Chem import Draw
        from PIL import Image
        # https://discuss.streamlit.io/t/grid-of-images-with-the-same-height/10668/6
        # https://towardsdatascience.com/molecular-visualization-in-streamlit-using-rdkit-and-py3dmol-4e8e63488eb8
        selected_row = int_return["selected_rows"]
        selected_df = pd.DataFrame(selected_row, columns=selected_df.columns)
        df_image = selected_df[['Ligand ID', 'SMILES']]

        idx = 0
        while idx < len(selected_row):
            for _ in range(len(selected_row)):
                cols = st.columns(4)

        # first, going to loop over the columns,
                for col_num in range(4):


        # next check that idx is in range, if it is then we add an image to the
        # column number we are on. If idx > len(filteredImages), it should
        # skip those columns, they will exist but we just wont put
        # anything in them
                    if idx < len(selected_row):
                        m = Chem.MolFromSmiles(df_image.at[idx, 'SMILES'])
                        im = Draw.MolToImage(m)

                        cols[col_num].image(im,
                             width=150, caption=df_image.at[idx, 'Ligand ID'])
                        idx+=1

        # Download code from here: https://discuss.streamlit.io/t/automatic-download-select-and-download-file-with-single-button-click/15141/3
        # Downloaded on Jan 9, 2023

        ################## pymol ile hot spot visulaization##################

        def download_button(object_to_download, download_filename):
            """
            Generates a link to download the given object_to_download.
            Params:
            ------
            object_to_download:  The object to be downloaded.
            download_filename (str): filename and extension of file. e.g. mydata.csv,
            Returns:
            -------
            (str): the anchor tag to download object_to_download
            """
            if isinstance(object_to_download, pd.DataFrame):
                object_to_download = object_to_download.to_csv(index=False)

            # Try JSON encode for everything else
            else:
                object_to_download = json.dumps(object_to_download)
            try:
                # some strings <-> bytes conversions necessary here
                b64 = base64.b64encode(object_to_download.encode()).decode()

            except AttributeError as e:
                b64 = base64.b64encode(object_to_download).decode()

            dl_link = f"""
            <html>
            <head>
            <title>Start Auto Download file</title>
            <script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
            <script>
            $('<a href="data:text/csv;base64,{b64}" download="{download_filename}">')[0].click()
            </script>
            </head>
            </html>
            """
            return dl_link


        def download_df():
            components.html(
                download_button(selected_df, st.session_state.filename),
                height=0,
            )


        with st.form("my_form", clear_on_submit=False):
            st.text_input("Enter filename", key="filename")
            submit = st.form_submit_button("Download", on_click=download_df)

