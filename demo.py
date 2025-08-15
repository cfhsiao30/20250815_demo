import numpy as np
import pandas as pd
import streamlit as st

st.title("AI DEMO PAGE")
st.write("## This is a demo page for AI applications.")
st.chat_input("Say something")

st.write("##### 互動式表格")
arr1=np.array([1, 2, 3, 4, 5])
arr2=np.array([6, 7, 8, 9, 10])
#st.write(arr1)

df1=pd.DataFrame([arr1, [11,12,13,14,15]])
df2=pd.DataFrame([arr2, [16,17,18,19,20]])
#st.write(df1)
#st.table(df1)

st.write("##### 核取方塊")
r1=st.checkbox("外帶")
if r1:
    st.info("餐點外帶")
else:
    st.info("餐點內用")

st.write("##### 橫向排列")
checks= st.columns(2)
txt=""
with checks[0]:
    r11=st.checkbox("A")
    if r11:
        txt += "A"

with checks[1]:
    r12=st.checkbox("B")
    if r12:
        txt += "B"  
st.info(txt)      

st.write("##### 選項按鈕")
b1=st.radio("想喝哪種飲品?", ["咖啡", "果汁", "茶"])
st.info(f"你選擇了: {b1}")
b2=st.radio("想吃哪種餐點?", ["漢堡", "薯條", "沙拉"])
st.info(f"你選擇了: {b2}")
b3=st.radio("想喝哪種飲品?", ["咖啡", "果汁", "茶"],key="b3")
st.info(f"你選擇了: {b3}")

st.write("##### 滑桿功能")
num=st.slider("選擇數字", 0, 20, step=1)
st.info(num)

st.write("##### 下拉選單")
city=st.selectbox("選擇城市", ["台北", "台中", "高雄"])
if city == "台北":
    st.info("A")
elif city == "台中":
    st.info("B")
else:
    st.info("C")

st.sidebar.write("##### 側邊攔按鈕")
b1=st.sidebar.radio("想玩哪個功能?", ["選項", "下拉", "滑桿"])
st.sidebar.info({b1})

st.write("##### botton按鈕")
a=st.number_input("輸入數字")
b=st.number_input("輸入數字",key="b")
if st.button("相加"):
    st.info(f"兩數相加: {a + b}")
    st.write("##### 互動",a+b)

st.text_input("First name")
st.date_input("Your birthday")
st.feedback("thumbs")
