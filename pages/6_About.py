import streamlit as st
from PIL import Image

st.set_page_config(
        page_title="About",
        page_icon=Image.open("data/icon.png"),
        layout="wide",
        initial_sidebar_state="expanded"
)
#st.subheader('DiPPI:  Drugs in Protein Protein Interface')
main_title = '<p style="font-family:sans-serif; color:#5E2750; font-size: 35px; font-weight:bold">DiPPI:  Drugs in Protein Protein Interface</p>'
st.markdown(main_title, unsafe_allow_html=True)
#st.title('About')
st.text('')
st.text('')
sub_title = '<p style="font-family:sans-serif; color:#77216F; font-size: 24px; font-weight:bold">About</p>'
st.markdown(sub_title, unsafe_allow_html=True)

st.markdown(""" 
 <style>
  .main-font
  { 
  font-family:sans-serif; font-size:14px;text-align: justify
  }
</style>""", unsafe_allow_html=True)
col1, col2  = st.columns(2)
with col1:
    text =  'Proteins communicate with one another at their interfaces, and impairments in protein-protein interactions ' \
            '(PPIs) have been linked to a number of diseases. Therefore, it\'s essential to understand the ' \
            'characteristics of drugs that target interfaces and drug-modulated PPIs. DiPPI ' \
            '(Drugs in Protein-Protein Interfaces), a website for the search of FDA-approved drugs and drug-like molecules ' \
            'in protein interfaces. It can be utilized for the investigation of interface-bound drugs and their binding' \
            ' interfaces for drug-repurposing studies.'
    st.markdown(f'<p class="main-font">{text}</p>', unsafe_allow_html=True)
with col2:
    st.markdown(
        """
        <style>
            button[title^=Exit]+div [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
            }
        </style>
        """, unsafe_allow_html=True
    )

    image1 = Image.open("data/icon1.png")
    new_image = image1.resize((424, 330))
    st.image(new_image)
    st.markdown(""" 
     <style>
      .center
      { 
      font-family:sans-serif; font-size:14px;text-align: center
      }
    </style>""", unsafe_allow_html=True)
    st.markdown(f'<p class="center"><em>1AAQ with bound ligand PSI</em></p>', unsafe_allow_html=True)


text = 'Proteins interact with other proteins or molecules through protein interfaces (PPIs). Drugs or small molecules ' \
       'can block or alter the activity of the proteins by binding to these sites. Characteristics of the interaction ' \
       'and interaction partners determine the downstream processes, and perturbations of such interactions are ' \
       'associated with various human diseases. Therefore, PPIs constitute a highly promising type of potential ' \
       'target for pharmacological intervention.'
st.markdown(f'<p class="main-font">{text}</p>', unsafe_allow_html=True)


text = 'Drug repurposing is an efficient strategy for identifying novel pharmacological activities or therapeutic ' \
       'properties for approved or investigational drugs. The key idea is that similar drugs target similar proteins. ' \
       'Therefore, targeting PPIs and investigating the properties of the interactions is critical for the identification' \
       ' of drug targets and alternative pathways for existing drugs.We used structural clusters of PPIs and drug-like ' \
       'ligands to facilitate their targeting by drugs. Our hypothesis is that if we can identify similar interfaces ' \
       'and similar drugs, search space for drug repurposing studies will be decreased dramatically and this, in turn, ' \
       'will increase the chances of hitting the correct target. '





# sub_title = '<p style="font-family:sans-serif; color:#77216F; font-size: 24px; font-weight:bold; text-align: center">DiPPI Flowchart</p>'
# st.markdown(sub_title, unsafe_allow_html=True)

# Load the image
image = Image.open('data/about.jpg')
new_image = image.resize((269,317))

new_image = image.resize((897, 1056))
st.image(new_image, caption='Flowchart of DiPPI process', use_column_width=True, width=50)

# Apply CSS styles to center the image with its original size
st.markdown(
    """
    <style>
    img {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)




st.write()
st.write()
st.write()
st.markdown('<p class="center"><a href="https://cosbilab.ku.edu.tr/">For your questions please contact [COSBI Lab]</a></p>', unsafe_allow_html=True)

