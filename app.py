#Streamlit  code
import streamlit as st
from models import  generate_content

st.title('streamlit Gemini LLM App')
st.subheader('LLM')
st.text_area(
    "Enter your prompt",
    placeholder= "what is relativity gravity?"
)

if st.button("🎯 Send Prompt"):
    if user_input.strip() == '':
        st.warning('Write valid prompt!!')
    else:
        with st.spinner('Thinking....'):
            answer = generate_content(user_input)
            st.success('Generated Content!!')
            st.write(answer)