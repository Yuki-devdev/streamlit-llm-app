import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 専門家の種類とシステムメッセージ
EXPERT_SYSTEM_MESSAGES = {
    "ITコンサルタント": "あなたは優秀なITコンサルタントです。技術的な観点から分かりやすく回答してください。",
    "キャリアアドバイザー": "あなたは経験豊富なキャリアアドバイザーです。親身になってアドバイスしてください。"
}

def get_llm_response(user_input: str, expert_type: str) -> str:
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=EXPERT_SYSTEM_MESSAGES[expert_type]),
        HumanMessage(content=user_input)
    ]
    result = llm(messages)
    return result.content

st.title("LLM搭載 専門家相談アプリ")
st.write("""
このアプリは、AIが「ITコンサルタント」または「キャリアアドバイザー」としてあなたの質問に回答します。  
下記のフォームに質問内容を入力し、相談したい専門家の種類を選択して送信してください。
""")

expert_type = st.radio(
    "相談したい専門家を選択してください：",
    ("ITコンサルタント", "キャリアアドバイザー")
)

user_input = st.text_area("質問内容を入力してください：", height=100)

if st.button("送信"):
    if user_input.strip():
        with st.spinner("AIが回答中です..."):
            response = get_llm_response(user_input, expert_type)
        st.markdown("#### 回答")
        st.write(response)
    else:
        st.warning("質問内容を入力してください。")