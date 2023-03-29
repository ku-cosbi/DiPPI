import streamlit as st
from PIL import Image


import streamlit as st

#st.subheader('DiPPI:  Drugs in Protein Protein Interface')
original_title = '<p style="font-family:Trebuchet MS; color:#4682B4; font-size: 35px; font-weight:bold">DiPPI:  Drugs in Protein Protein Interface</p>'
st.markdown(original_title, unsafe_allow_html=True)
original_title = '<p style="font-family:Trebuchet MS; color:#4682B4; font-size: 24px; font-weight:bold">User Guide</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.text('')
st.text('')
sub_title = '<p style="font-family:Trebuchet MS; color:#1f537f; font-size: 18px; text-align: justified"><u><i>Query By Drug</i></u></p>'
st.markdown(sub_title, unsafe_allow_html=True)

st.markdown(""" 
 <style>
  .main-text
  { 
  font-family:Trebuchet MS; font-size:14px;text-align: justify;font-weight:bold
  }
</style>""", unsafe_allow_html=True)


text = 'Users can search for a ligand of interest using Query by Ligand section. '
st.markdown(f'<p class="title-text">{text}</p>', unsafe_allow_html=True)
text = 'Option 1: Multiselect area allows filtering via individual ligand identifiers from PDB. Click on the checkbox ' \
       'next to the ligand you want to expand.'
st.markdown(f'<p class="main-text">{text}</p>', unsafe_allow_html=True)
st.image('data/ug_1.png')


text = 'Option 2: Click on the checkbox next to the ligand you want to expand by selecting from the list.'
st.markdown(f'<p class="main-text">{text}</p>', unsafe_allow_html=True)
st.image('data/ug_2.png')


text = 'Select dataframe allows visualization of molecular descriptors for selected ligand, along with other relevant data.'
st.markdown(f'<p class="main-text">{text}</p>', unsafe_allow_html=True)
st.image('data/ug_3.png')

text = 'Click on the checkbox next to the ligand you want to download data for. This option allows for the' \
       ' visualization of the ligand as well.'
st.markdown(f'<p class="main-text">{text}</p>', unsafe_allow_html=True)
st.image('data/ug_4.png')


#### Same for the interface part.


st.text('')
st.text('')
sub_title = '<p style="font-family:Trebuchet MS; color:#1f537f; font-size: 18px; text-align: justified"><u><i>Query By Interface</i></u></p>'
st.markdown(sub_title, unsafe_allow_html=True)

st.markdown(""" 
 <style>
  .main-text
  { 
  font-family:Trebuchet MS; font-size:14px;text-align: justify;font-weight:bold
  }
</style>""", unsafe_allow_html=True)

text = 'Users can search for a structure of interest using Query by Interface section. '
st.markdown(f'<p class="main-text">{text}</p>', unsafe_allow_html=True)

text = 'Option 1: Multiselect area allows filtering via individual structure identifiers from PDB. Click on the checkbox ' \
       'next to the structure identifier if you want it to appear in Selected Table.'
st.markdown(f'<p class="main-text">{text}</p>', unsafe_allow_html=True)
st.image('data/ug_5.png')


text = 'Multiselect area for ligand ID further allows the limiting the view only to interfaces with selected ligand.'
st.markdown(f'<p class="main-text">{text}</p>', unsafe_allow_html=True)
st.image('data/ug_6.png')


text = 'Selected Table shows interface residues and the subset of interface residues that are in contact with the ligand.' \
       ' Download button downloads the selected view.'
st.markdown(f'<p class="main-text">{text}</p>', unsafe_allow_html=True)
st.image('data/ug_7.png')



text = 'Legends for the tables can be accessed through the README file in Downloads tab.'
st.markdown(f'<p class="main-text">{text}</p>', unsafe_allow_html=True)
