from dotenv import load_dotenv
load_dotenv()

import streamlit as st
#from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

st.title('Kevin의 인공지능 시인')
chat_model = ChatOpenAI()
content = st.text_input('시의 주제를 제시해주세요.!')

if st.button('시 작성 요청하기'):
    with st.spinner('Wait fro it...'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)
