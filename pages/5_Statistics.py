import numpy as np
import pandas as pd
import streamlit as st



#st.subheader('DiPPI:  Drugs in Protein Protein Interface')
original_title = '<p style="font-family:Trebuchet MS; color:#4682B4; font-size: 35px; font-weight:bold">DiPPI:  Drugs in Protein Protein Interface</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.text('')
st.text('')


new_title = '<p style="font-family:Trebuchet MS; text-align: left; color:#4682B4; font-size: 24px;">Statistics</p>'
st.markdown(new_title, unsafe_allow_html=True)

df = pd.DataFrame(columns= (range(2)))
df.loc[0] = ['Number of investigated proteins', '98,632']
df.loc[1] = ['Number of investigated interfaces', '534,203']
df.loc[2] = ['Number of interfaces belonging to proteins with bound drugs (any region)', '335,648']
df.loc[3] = ['Number of interfaces to which at least one drug-like molecule binds to', '53,452']
df.loc[4] = ['Number of interfaces to which at least one FDA-drug binds to', '22,575']
df.loc[5] = ['Number of investigated drug-like small molecules', '11,011']
df.loc[6] = ['Number of eliminated small molecules', '402']
df.loc[7] = ['Number of investigated FDA-approved drugs', '1,615']
df.loc[8] = ['Number of drug-like small molecules that bind to at least one interface residue', '2,214']
df.loc[9] = ['Number of FDA-approved drugs that bind to at least one interface residue', '335']


style = df.style.set_properties(**{'font-size': '10pt', 'font-family': 'Trebuchet MS','border-collapse': 'collapse','border': '1px solid black'}).hide_index()
style.hide_columns()
#st.write(style.to_html(), unsafe_allow_html=True)
st.markdown(style.to_html(), unsafe_allow_html=True)

st.text('')
st.text('')
st.text('')
st.text('')


st.markdown('<p style="font-size: 14px;font-family: Trebuchet MS">From 343 FDA-approved drugs which are bound to at least one interface:</p>', unsafe_allow_html=True)
st.markdown('''
<ul>
    <li style="font-size: 14px;font-family: Trebuchet MS">247 of them has no violations to Lipinski’s rules</li>
    <li style="font-size: 14px;font-family: Trebuchet MS">166 of them has no violations to Ghose criteria</li>
    <li style="font-size: 14px;font-family: Trebuchet MS">274 of them has no violations to Veber criteria</li>
    <li style="font-size: 14px;font-family: Trebuchet MS">260 of them has no violations to Egan criteria</li>
    <li style="font-size: 14px;font-family: Trebuchet MS">173 of them has no violations to Muegge criteria</li>
    <li style="font-size: 14px;font-family: Trebuchet MS">57 of these drugs show lead-like properties according to SwissADME</li>

</ul>
<style>
ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)


