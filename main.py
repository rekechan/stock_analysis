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

def view_df_at_st(df,name):
    if st.checkbox(name):
        if df.empty:
            st.write("該当する株はありませんでした。")
        else:
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
                
                if st.checkbox(f"{stockname}　@{name}",value=True):
                    st.markdown(f"{link}", unsafe_allow_html=True)
                    st.write(f"{title}{weather}。")
                    st.write(f"現在株価　　　： {price0} 円")
                    st.write(f"目標株価　　　： {price1} 倍")
                    st.write(f"アナリスト予想： {price2} 倍")
                    st.write(f"個人投資家予想： {price3} 倍")
                    st.write(f"理論株価　　　： {price4} 倍")
                st.write("")
    st.write("")



df_1 = read_gsheet(st.secrets["sheeturl_1"])
#df_1 = read_gsheet()
df_2 = read_gsheet(st.secrets["sheeturl_2"])
#df_2 = read_gsheet()

st.title("株解析bot")

view_df_at_st(df_1,"SBI/みんかぶスクレイピング")
view_df_at_st(df_2,"過去2週間上昇し続けている株")