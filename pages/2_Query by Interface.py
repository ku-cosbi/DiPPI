import ast
import json
import base64
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from PIL import Image
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(
        page_title="Query By Interface",
        page_icon=Image.open("data/icon.png"),
        layout="wide",
        initial_sidebar_state="expanded"
)

# Download code from here: https://discuss.streamlit.io/t/automatic-download-select-and-download-file-with-single-button-click/15141/3
# Downloaded on Jan 9, 2023

#st.subheader('DiPPI:  Drugs in Protein Protein Interface')
original_title = '<p style="font-family:sans-serif; color:#5E2750; font-size: 35px; font-weight:bold">DiPPI:  Drugs in Protein Protein Interface</p>'
st.markdown(original_title, unsafe_allow_html=True)

proteins_df = pd.read_csv('data/protein_summary.txt', sep='\t')
interfaces_df = pd.read_csv('data/interface_data.txt', sep='\t')
ligands_df = pd.read_csv('data/ligand_data.txt', sep = '\t')
interfaces_df = interfaces_df.drop(columns = ['fda_approved'])
proteins_df_sel = pd.DataFrame(columns = proteins_df.columns)


selection = st.selectbox('Filter by', ("Filter by PDB ID", "Filter by UniProt ID",  "Filter by Protein Name", "Filter by Uniprot Sequence"))

if selection == 'Filter by PDB ID':
    pdb_selection = st.multiselect("Filter by PDB ID", proteins_df.PDB_ID)
    ligand_selection = st.multiselect("Filter by Ligand ID", ligands_df['Ligand ID'])
    if len(pdb_selection) > 0:
        proteins_df_sel = proteins_df[proteins_df.PDB_ID.isin(pdb_selection)]
    if len(ligand_selection) > 0:
        proteins_df_sel['Ligand_ID'] = proteins_df_sel['Ligand_ID'].apply(lambda x: x.split(','))
        proteins_df_sel = proteins_df_sel.explode(['Ligand_ID'])
        proteins_df_sel.Ligand_ID = proteins_df_sel.Ligand_ID.apply(lambda x: x.strip())
        proteins_df_sel = proteins_df_sel[proteins_df_sel['Ligand_ID'].isin(ligand_selection)]
elif selection == 'Filter by UniProt ID':
    pdb_selection = st.multiselect("Filter by UniProt ID", proteins_df.UNIPROT_ID)
    ligand_selection = st.multiselect("Filter by Ligand ID", ligands_df['Ligand ID'])
    if len(pdb_selection) > 0:
        proteins_df_sel = proteins_df[proteins_df.UNIPROT_ID.isin(pdb_selection)]
    if len(ligand_selection) > 0:
        proteins_df_sel['Ligand_ID'] = proteins_df_sel['Ligand_ID'].apply(lambda x: x.split(','))
        proteins_df_sel = proteins_df_sel.explode(['Ligand_ID'])
        proteins_df_sel.Ligand_ID = proteins_df_sel.Ligand_ID.apply(lambda x: x.strip())
        proteins_df_sel = proteins_df_sel[proteins_df_sel['Ligand_ID'].isin(ligand_selection)]
elif selection == 'Filter by Uniprot Sequence':
    pdb_selection = st.multiselect("Filter by UniProt Sequence", proteins_df.UNIPROT_Sequence)
    ligand_selection = st.multiselect("Filter by Ligand ID", ligands_df['Ligand ID'])
    if len(pdb_selection) > 0:
        proteins_df_sel = proteins_df[proteins_df.UNIPROT_Sequence.isin(pdb_selection)]
    if len(ligand_selection) > 0:
        proteins_df_sel['Ligand_ID'] = proteins_df_sel['Ligand_ID'].apply(lambda x: x.split(','))
        proteins_df_sel = proteins_df_sel.explode(['Ligand_ID'])
        proteins_df_sel.Ligand_ID = proteins_df_sel.Ligand_ID.apply(lambda x: x.strip())
        proteins_df_sel = proteins_df_sel[proteins_df_sel['Ligand_ID'].isin(ligand_selection)]

elif selection == 'Filter by Protein Name':
    pdb_selection = st.multiselect("Filter by Protein Name", proteins_df.ProteinNames)
    ligand_selection = st.multiselect("Filter by Ligand ID", ligands_df['Ligand ID'])
    if len(pdb_selection) > 0:
        proteins_df_sel = proteins_df[proteins_df.ProteinNames.isin(pdb_selection)]
    if len(ligand_selection) > 0:
        proteins_df_sel['Ligand_ID'] = proteins_df_sel['Ligand_ID'].apply(lambda x: x.split(','))
        proteins_df_sel = proteins_df_sel.explode(['Ligand_ID'])
        proteins_df_sel.Ligand_ID = proteins_df_sel.Ligand_ID.apply(lambda x: x.strip())
        proteins_df_sel = proteins_df_sel[proteins_df_sel['Ligand_ID'].isin(ligand_selection)]

if len(proteins_df_sel) != 0:
    int_builder = GridOptionsBuilder.from_dataframe(proteins_df_sel[["PDB_ID", "Interface_ID", "Ligand_ID", "Number_of_ligands", "FDA_approval"]]) # "Ligand_ID", "Number_of_interfaces", "Number_of_ligands",
    int_builder.configure_default_column(editable=False, filterable=True, cellStyle={'text-align': 'center'})
    int_builder.configure_column("PDB_ID", header_name="PDB ID", editable=False, )
    int_builder.configure_column("Interface_ID", header_name="Interfaces")
    int_builder.configure_column("Ligand_ID", header_name="Ligands")
    #int_builder.configure_column('Number_of_interfaces', header_name="# of Interfaces")
    int_builder.configure_column("Number_of_ligands", header_name="# of Ligands")
    #int_builder.configure_column("FDA_approval", header_name="FDA Approved")
    int_builder.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
    int_builder.configure_selection(selection_mode='multiple',use_checkbox=True)

    st.markdown(f'<p class="main-font">Summary of selected structures. Select for a detailed view:</p>', unsafe_allow_html=True)

    gridoptions = int_builder.build()
    gridoptions["columnDefs"][0]["checkboxSelection"]=True
    gridoptions["columnDefs"][0]["headerCheckboxSelection"]=True	



    with st.spinner('Loading data...'):
        int_return = AgGrid(proteins_df_sel,
                            width='100%',
                            height=(len(proteins_df_sel) + 4) * 35.2,
                            theme='alpine',
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
            st.markdown(f'<p class="main-font">Detailed view of interface information:</p>', unsafe_allow_html=True)
            selected_row = int_return["selected_rows"]

        column_names = ['PDB ID', 'Chain 1', 'Chain 2','Contacting Residues (Chain 1)', 'Nearby Residues (Chain 1)',
                       'Contacting Residues (Chain 2)','Nearby Residues (Chain 2)','Ligand_ID', 'Ligand_Positions','Ligand Position in Chain 1 (Contact Res.)',
                       'Ligand Position in Chain 1 (Nearby Res.)', 'Ligand Position in Chain 2 (Contact Res.)',
                       'Ligand Position in Chain 2 (Nearby Res.)','Interface Cluster Members','Ligand Binding Hotspots in Chain 1','Ligand Binding Hotspots in Chain 2','Interface_ID', 'Number_of_ligands'] #  'Ligand Position in Chain 2 (Nearby Res.)','FDA', 'Interface_ID',
        #'Interface_ID', 'Number_of_interfaces','Number_of_ligands'
        selected_df = pd.DataFrame(selected_row, columns=proteins_df_sel.columns)
        selected_df = selected_df.rename(columns=lambda x: x.strip())
        selected_ids = selected_df.PDB_ID.to_list()

        df_result = interfaces_df[interfaces_df['pdbID'].isin(selected_ids)]
        if len(ligand_selection) >0:
            df_result = df_result[df_result['ligands'].isin(ligand_selection)]

        df_result = df_result.reset_index()
        df_result.drop(columns = ['index'], inplace=True)

        df_result['Interface_ID'] = df_result['pdbID']  + '_'+df_result['chain_1']  + '_'+ df_result['chain_2']
        #sel_prot = sel_prot[['Interface_ID', 'Number_of_interfaces', 'Number_of_ligands']]
        proteins_df_sel = proteins_df_sel[['Interface_ID', 'Number_of_ligands']]

        df_result = df_result.merge(proteins_df_sel, on = ['Interface_ID'], how='left')
        df_result.columns = column_names

        df_result = df_result[['Interface_ID','Ligand_ID', 'Ligand Position in Chain 1 (Contact Res.)', # 'Ligand_ID', 'FDA', 'Ligand Position in Chain 1 (Contact Res.)',
                       'Ligand Position in Chain 1 (Nearby Res.)', 'Ligand Position in Chain 2 (Contact Res.)',
                       'Ligand Position in Chain 2 (Nearby Res.)' , 'Contacting Residues (Chain 1)', 'Nearby Residues (Chain 1)',
                       'Contacting Residues (Chain 2)','Nearby Residues (Chain 2)','Number_of_ligands', 'Interface Cluster Members', 'Ligand Binding Hotspots in Chain 1','Ligand Binding Hotspots in Chain 2']] # 'Nearby Residues (Chain 2)','Number_of_interfaces','Number_of_ligands'
        int_builder = GridOptionsBuilder.from_dataframe(df_result)
        int_builder.configure_default_column(editable=False, filterable=True, cellStyle={'text-align': 'center'})
        int_builder.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
        int_builder.configure_selection(selection_mode='multiple', use_checkbox=True)
        gridoptions = int_builder.build()
        gridoptions["columnDefs"][0]["checkboxSelection"]=True
        gridoptions["columnDefs"][0]["headerCheckboxSelection"]=True

        with st.spinner('Loading data...'):
            int_return = AgGrid(df_result,
                            width='100%',
                            height=(len(df_result) + 4) * 35.2 + 3,
                            theme='alpine',
                            enable_enterprise_modules=False,
                            gridOptions=gridoptions,
                            fit_columns_on_grid_load=False,
                            update_mode=GridUpdateMode.SELECTION_CHANGED, # or MODEL_CHANGED
                            custom_css={".ag-header-cell-label": {"justify-content": "center"}})

        selected_row = int_return["selected_rows"]
        selected_df = pd.DataFrame(selected_row, columns=df_result.columns)
        st.write('dflsj')
        st.write(selected_df)


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

        st.markdown(f'<p class="main-font"> Select from the detailed interface information table to download: </p>',
                    unsafe_allow_html=True)

        with st.form("my_form", clear_on_submit=False):
            st.text_input("Enter filename", key="filename")
            submit = st.form_submit_button("Download", on_click=download_df)



new_title = '<p style="font-family: sans-serif; text-align: center; color:#77216F; font-size: 16px;">For more information about how to use this website, please visit User Guide Page in the navigation panel.</p>'
st.markdown(new_title, unsafe_allow_html=True)

