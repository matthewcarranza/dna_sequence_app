import streamlit as st
import pandas as pd
import altair as alt

st.write("""
# DNA Nucleotide Translator

Translates DNA sequences into their proper amino acid names.

***
""")

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query\nGAACTGATAGCGATCGCATCGATCGACTAGCATCG\nGCCTATATCGCTACTCGACTACTAGCTAGCGATCGAGCT\nGATCTCGATATCTGCAGCGCTCGCCGTACGAGC"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d
  
X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

st.subheader('2. Print text')
st.write(f"There are {str(S['A'])} adenine (A)")
st.write(f"There are {str(S['T'])} thymine (T)")
st.write(f"There are {str(S['G'])} guanine (G)")
st.write(f"There are {str(S['C'])} cytosine (C)")
          
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80)
)
st.write(p)
