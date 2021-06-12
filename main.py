import streamlit as st
import numpy
import pandas as pd

def read_gsheet(url):
    dfs = pd.read_html(url,encoding = "utf-8")
    df = dfs[0]
    df.columns = df.iloc[0,].values.tolist()
    df = df.drop(index = 0)
    df = df.iloc[:,1:].dropna(how = "all")
    df = df.reset_index(drop=True)
    return df

df_1 = read_gsheet(st.secrets["sheeturl_1"])
df_2 = read_gsheet(st.secrets["sheeturl_2"])

st.title("株解析bot")
day = df_1["date"][0]
st.write(f"{day} の解析結果")

if st.checkbox("SBI/みんかぶスクレイピング"):
    for i in range(len(df_1)):
        stockname = df_1["stockname"][i]
        stockcode = df_1["stockcode"][i]
        weather = df_1["weather"][i]
        title = df_1["title"][i]
        price0 = df_1["現在株価"][i]
        price1 = df_1["目標株価"][i]
        price2 = df_1["アナリスト予想株価"][i]
        price3 = df_1["個人投資家予想株価"][i]
        price4 = df_1["理論株価"][i]

        link = f'[{stockcode}](https://s.kabutan.jp/stocks/{stockcode}/app_launchers/sbihyperkabu/)'
        
        if st.checkbox(f"{stockname}　@sbi/みんかぶ",value=True):
            st.markdown(f"{link}", unsafe_allow_html=True)
            st.write(f"{title}{weather}。")
            st.write(f"現在株価　　　： {price0} 円")
            st.write(f"目標株価　　　： {price1} 倍")
            st.write(f"アナリスト予想： {price2} 倍")
            st.write(f"個人投資家予想： {price3} 倍")
            st.write(f"理論株価　　　： {price4} 倍")
        st.write("")

st.write("")

if st.checkbox("最近上がり続けている株"):
    for i in range(len(df_2)):
        stockname = df_2["stockname"][i]
        stockcode = df_2["stockcode"][i]
        weather = df_2["weather"][i]
        title = df_2["title"][i]
        price0 = df_2["現在株価"][i]
        price1 = df_2["目標株価"][i]
        price2 = df_2["アナリスト予想株価"][i]
        price3 = df_2["個人投資家予想株価"][i]
        price4 = df_2["理論株価"][i]

        link = f'[{stockcode}](https://s.kabutan.jp/stocks/{stockcode}/app_launchers/sbihyperkabu/)'
        
        if st.checkbox(f"{stockname}　@最近上昇傾向",value=True):
            st.markdown(f"{link}", unsafe_allow_html=True)
            st.write(f"{title}{weather}。")
            st.write(f"現在株価　　　： {price0} 円")
            st.write(f"目標株価　　　： {price1} 倍")
            st.write(f"アナリスト予想： {price2} 倍")
            st.write(f"個人投資家予想： {price3} 倍")
            st.write(f"理論株価　　　： {price4} 倍")
        st.write("")