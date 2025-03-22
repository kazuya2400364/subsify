import streamlit as st
import pandas as pd

# CSVファイルの読み込み
model_list = pd.read_csv("model_list.csv", encoding="shift_jis")

def find_matching_data(model_list, kw, year):
    matching_data = model_list[model_list['kW'] == kw]

    if not matching_data.empty:
        model = matching_data.iloc[0]['model']
        price = matching_data.iloc[0]['price']

        if year >= 15:
            subsidy = matching_data.iloc[0]['subsidy_long']
            
        else:
            subsidy = matching_data.iloc[0]['subsidy_normal']
          
        result_df = pd.DataFrame({
            'model': [model],
            'kW': [kw],
            'price': [price],
            'subsidy': [subsidy]
        })
        return result_df
    
    else:
        return "該当するデータが見つかりませんでした。"

# Streamlitアプリの作成
st.title("kWと年数から製品・補助金情報を検索")

# kWの入力
kw = st.number_input("定格能力(kW)を入力してください", step=0.1)

# 年数の入力
year = st.number_input("製造経過年数を入力してください", step=1)

# 検索ボタン
if st.button("検索"):
    result = find_matching_data(model_list, kw, year)
    st.write("おすすめ製品")
    st.write("型番：" + result.iloc[0]['model'])
    st.write("定格能力(冷房)：" + str(result.iloc[0]['kW']) + "kW")
    st.write("価格：" + str(result.iloc[0]['price']) + "円")
    st.write("補助金額：" + str(result.iloc[0]['subsidy']) + "pt")
    
