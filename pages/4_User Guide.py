import streamlit as st
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

import streamlit as st
st.set_page_config(
        page_title="User Guide",
        page_icon=Image.open("data/icon.png"),
        layout="wide",
        initial_sidebar_state="expanded"
)
#st.subheader('DiPPI:  Drugs in Protein Protein Interface')
original_title = '<p style="font-family:sans-serif; color:#5E2750; font-size: 35px; font-weight:bold">DiPPI:  Drugs in Protein Protein Interface</p>'
st.markdown(original_title, unsafe_allow_html=True)

original_title = '<p style="font-family:sans-serif; color:#77216F; font-size: 24px; font-weight:bold">User Guide</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.text('')
st.text('')

sub_title = '<p style="font-family:sans-serif; color:#2C001E; font-size: 18px; text-align: justified"><u><i>Query By Drug</i></u></p>'
st.markdown(sub_title, unsafe_allow_html=True)

text = 'Multiselect area allows filtering via individual ligand identifiers from PDB, or SMILES string of the small molecule.'
st.markdown(f'<p style="font-family:sans-serif; color:#2C001E; font-size: 18px;  class="main-text">{text}</p>', unsafe_allow_html=True)
st.image('data/drug_explain.png',output_format="PNG")



st.text('')
st.text('')
sub_title = '<p style="font-family:sans-serif; color:#2C001E; font-size: 18px; text-align: justified"><u><i>Query By Interface</i></u></p>'
st.markdown(sub_title, unsafe_allow_html=True)

text = 'Multiselect area allows filtering via either PDB ID, UniProt ID, Protein Name or UniProt Sequence.'
st.markdown(f'<p style="font-family:sans-serif; color:#2C001E; font-size: 18px; class="main-text">{text}</p>', unsafe_allow_html=True)
st.image('data/interface_explain.png',output_format="PNG")

# text = 'More details about the legends for the tables can be accessed through the README file in Downloads tab.'
# st.markdown(f'<p style="font-family:sans-serif; color:#2C001E; font-size: 18px; class="main-text">{text}</p>', unsafe_allow_html=True)


st.text('')

text = 'Protein interfaces are defined by considering both contacting and nearby residues which are given separately in the table for convenience. ' \
       'Chain 1 and Chain 2 represent two chains of the interface with the order that appears in the interface ID column. Columns 3-6 provide information about the ' \
       'ligand-bound interface residues, while columns 7-10 provide information about the interface residues regardless of small molecule information. ' \
       'For more detail, please refer to the article. '
st.markdown(f'<p style="font-family:sans-serif; color:#2C001E; font-size: 18px;text-align: justified; class="main-text">{text}</p>', unsafe_allow_html=True)
