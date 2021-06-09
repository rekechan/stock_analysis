import streamlit as st
import numpy
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1h_qO5b41PXiOWdk4iV56i9UvtoEcBh8rKyT7Az2Y_g8/edit?usp=sharing'
dfs = pd.read_html(url,encoding = "utf-8")
df = dfs[0]
df.columns = df.iloc[0,].values.tolist()
df = df.drop(index = 0)
df = df.iloc[:,1:].dropna(how = "all")
df = df.reset_index(drop=True)

st.title("株解析bot")
day = df["date"][0]
st.write(f"{day} の解析結果")

for i in range(len(df)):
    stockname = df["stockname"][i]
    stockcode = df["stockcode"][i]
    weather = df["weather"][i]
    title = df["title"][i]
    price0 = df["現在株価"][i]
    price1 = df["目標株価"][i]
    price2 = df["アナリスト予想株価"][i]
    price3 = df["個人投資家予想株価"][i]
    price4 = df["理論株価"][i]

    link = f'[{stockcode}](https://s.kabutan.jp/stocks/{stockcode}/app_launchers/sbihyperkabu/)'
    
    if st.checkbox(f"{stockname}",value=True):
        st.markdown(f"{link}", unsafe_allow_html=True)
        st.write(f"{title}{weather}。")
        st.write(f"現在株価　　　： {price0} 円")
        st.write(f"目標株価　　　： {price1} 倍")
        st.write(f"アナリスト予想： {price2} 倍")
        st.write(f"個人投資家予想： {price3} 倍")
        st.write(f"理論株価　　　： {price4} 倍")
    st.write("")