import streamlit as st
from PIL import Image

st.write("""
# DNA Nucleotide Translator

Translates DNA sequences into their proper amino acid names.

***
""")

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query\nGAACTGATAGCGATCGCATCGATCGACTAGCATCG\nGCCTATATCGCTACTCGACTACTAGCTAGCGATCGAGCT\nGATCTCGATATCTGCAGCGCTCGCCGTACGAGC"

sequence = st.text_area("Sequence input", sequence_input, height=25)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')
