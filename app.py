import streamlit as st
st.title('Semantic similarity Application')
sentences1=st.text_input('Insert sentences 1:')
sentences2=st.text_input('Insert sentences 2:')

st.write('Sentences1 is:', sentences1)
st.write('Sentences2 is:', sentences2)


if st.button('Submit'):
    st.write('sentences1 is:', sentences1)
    st.write('sentences2 is:', sentences2)
