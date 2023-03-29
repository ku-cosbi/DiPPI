import ast
import json
import base64
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


# Download code from here: https://discuss.streamlit.io/t/automatic-download-select-and-download-file-with-single-button-click/15141/3
# Downloaded on Jan 9, 2023
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
        download_button(df_result, st.session_state.filename),
        height=0,
    )


#st.subheader('DiPPI:  Drugs in Protein Protein Interface')
original_title = '<p style="font-family:Trebuchet MS; color:#4682B4; font-size: 35px; font-weight:bold">DiPPI:  Drugs in Protein Protein Interface</p>'
st.markdown(original_title, unsafe_allow_html=True)

proteins_df = pd.read_csv('data/protein_summary.txt', sep='\t')
interfaces_df = pd.read_csv('data/interface_data.txt', sep='\t')
ligands_df = pd.read_csv('data/ligand_data.txt', sep = '\t')
interfaces_df = interfaces_df.drop(columns = ['fda_approved'])


pdb_selection = st.multiselect("Filter by PDB ID", proteins_df.PDB_ID)
ligand_selection = st.multiselect("Filter by ligand ID", ligands_df['Ligand ID'])

if len(pdb_selection) > 0:
    proteins_df = proteins_df[proteins_df.PDB_ID.isin(pdb_selection)]
if len(ligand_selection) > 0:
    proteins_df['Ligand_ID'] = proteins_df['Ligand_ID'].apply(lambda x: x.split(','))
    proteins_df = proteins_df.explode(['Ligand_ID'])
    proteins_df.Ligand_ID = proteins_df.Ligand_ID.apply(lambda x: x.strip())
    proteins_df = proteins_df[proteins_df['Ligand_ID'].isin(ligand_selection)]

sel_prot = proteins_df.copy()
int_builder = GridOptionsBuilder.from_dataframe(sel_prot[["PDB_ID", "Interface_ID", "Ligand_ID", "Number_of_ligands", "FDA_approval"]]) # "Ligand_ID", "Number_of_interfaces", "Number_of_ligands",
int_builder.configure_default_column(editable=False, filterable=True, cellStyle={'text-align': 'center'})
int_builder.configure_column("PDB_ID", header_name="PDB ID", editable=False, )
int_builder.configure_column("Interface_ID", header_name="Interfaces")
int_builder.configure_column("Ligand_ID", header_name="Ligands")
#int_builder.configure_column('Number_of_interfaces', header_name="# of Interfaces")
int_builder.configure_column("Number_of_ligands", header_name="# of Ligands")
#int_builder.configure_column("FDA_approval", header_name="FDA Approved")
int_builder.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
int_builder.configure_selection(selection_mode='multiple',use_checkbox=True)

st.markdown(f'<p class="main-font">Or select from the list:</p>', unsafe_allow_html=True)

gridoptions = int_builder.build()


with st.spinner('Loading data...'):
    int_return = AgGrid(sel_prot,
                        width='100%',
                        theme='light',
                        enable_enterprise_modules=False,
                        gridOptions=gridoptions,
                        fit_columns_on_grid_load=True,
                        update_mode=GridUpdateMode.SELECTION_CHANGED, # or MODEL_CHANGED
                        custom_css={".ag-header-cell-label": {"justify-content": "center;"}})

# About selection: https://medium.com/@hhilalkocak/streamlit-aggrid-6dbbab3afe03
# https://discuss.streamlit.io/t/aggrid-selection-clears-after-clicking-checkbox/29955/3
# Downloaded on Jan 9, 2023
with st.spinner('Loading data...'):
    st.markdown(f'<p class="main-font">Selected</p>', unsafe_allow_html=True)
    selected_row = int_return["selected_rows"]


column_names = ['PDB ID', 'Chain 1', 'Chain 2','Contacting Residues (Chain 1)', 'Nearby Residues (Chain 1)',
               'Contacting Residues (Chain 2)','Nearby Residues (Chain 2)','Ligand_ID', 'Ligand_Positions','Ligand Position in Chain 1 (Contact Res.)',
               'Ligand Position in Chain 1 (Nearby Res.)', 'Ligand Position in Chain 2 (Contact Res.)',
               'Ligand Position in Chain 2 (Nearby Res.)','Interface Cluster Members','Interface_ID', 'Number_of_ligands'] #  'Ligand Position in Chain 2 (Nearby Res.)','FDA', 'Interface_ID',
#'Interface_ID', 'Number_of_interfaces','Number_of_ligands'
selected_df = pd.DataFrame(selected_row, columns=sel_prot.columns)
selected_df = selected_df.rename(columns=lambda x: x.strip())
selected_ids = selected_df.PDB_ID.to_list()


df_result = interfaces_df[interfaces_df['pdbID'].isin(selected_ids)]
if  len(ligand_selection) >0:
    df_result = df_result[df_result['ligands'].isin(ligand_selection)]

df_result = df_result.reset_index()
df_result.drop(columns = ['index'], inplace=True)

df_result['Interface_ID'] = df_result['pdbID']  + '_'+df_result['chain_1']  + '_'+ df_result['chain_2']

#sel_prot = sel_prot[['Interface_ID', 'Number_of_interfaces', 'Number_of_ligands']]
sel_prot = sel_prot[['Interface_ID', 'Number_of_ligands']]

df_result = df_result.merge(sel_prot, on = ['Interface_ID'], how='left')

df_result.columns = column_names

df_result = df_result[['Interface_ID','Ligand_ID', 'Ligand Position in Chain 1 (Contact Res.)', # 'Ligand_ID', 'FDA', 'Ligand Position in Chain 1 (Contact Res.)',
               'Ligand Position in Chain 1 (Nearby Res.)', 'Ligand Position in Chain 2 (Contact Res.)',
               'Ligand Position in Chain 2 (Nearby Res.)' , 'Contacting Residues (Chain 1)', 'Nearby Residues (Chain 1)',
               'Contacting Residues (Chain 2)','Nearby Residues (Chain 2)','Number_of_ligands', 'Interface Cluster Members']] # 'Nearby Residues (Chain 2)','Number_of_interfaces','Number_of_ligands'
int_builder = GridOptionsBuilder.from_dataframe(df_result)
int_builder.configure_default_column(editable=False, filterable=True, cellStyle={'text-align': 'center'})
int_builder.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
#int_builder.configure_selection(selection_mode='multiple', use_checkbox=True)
gridoptions = int_builder.build()
with st.spinner('Loading data...'):
    int_return = AgGrid(df_result,
                    width='100%',
                    theme='light',
                    enable_enterprise_modules=False,
                    gridOptions=gridoptions,
                    fit_columns_on_grid_load=False,
                    update_mode=GridUpdateMode.SELECTION_CHANGED, # or MODEL_CHANGED
                    custom_css={".ag-header-cell-label": {"justify-content": "center"}})




with st.form("my_form", clear_on_submit=False):
    st.text_input("Enter filename", key="filename")
    submit = st.form_submit_button("Download", on_click=download_df)
