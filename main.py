from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st 

# 모델 초기화
llm = ChatOllama(model="sam860/exaone-4.0:1.2b")
# 프롬프트 템플릿 설정
prompt = ChatPromptTemplate([
    ("system", "You are a helpful assitant."),
    ("user", "{input}")
])
# 출력 파서 
output_parser = StrOutputParser()
# 체인 설정
chain = prompt | llm | output_parser

# 제목
st.title("인공지능 시인")
# 시 주제 입력 필드
content = st.text_input("시의 주제를 제시해 주세요")
st.write("시의 주제는 ", content)

# 실행 버튼 
if st.button("시 작성 요청하기"):
    with st.spinner("wait for it ..."):
        print(content)
        result = chain.invoke({"input": content + "에 대한 시를 작성해 주세요"})
        print(result)
        st.write(result)
