
import sys
import os
import shioaji as sj
import pandas as pd

# 加入 Python 路徑以導入 stock_agent 與 credentials
sys.path.append(r"D:\PythonQuantTrading_test")

try:
    from stock_agent import StockAPIWrapper
    import credentials

    # 初始化 Shioaji API
    api = sj.Shioaji(simulation=True)
    
    # 登入 (假設 credentials 有 PERSON_ID, PASSWD, API_KEY, SECRET_KEY)
    # 這裡根據一般的 Shioaji 使用方式
    api.login(
        api_key=credentials.API_KEY,
        secret_key=credentials.SECRET_KEY
    )

    # 封裝
    agent = StockAPIWrapper(api)
    
    # 獲取庫存 (這會返回一個 DataFrame)
    df_positions = agent.get_positions()
    
    if df_positions is None or df_positions.empty:
        print("目前無庫存資料。")
    else:
        print("--- 當前庫存清單 ---")
        # 篩選感興趣的欄位顯示
        # 欄位通常包含: code, quantity, last_price, pnl 等
        cols_to_show = ['code', 'quantity', 'last_price', 'pnl']
        # 檢查欄位是否存在
        available_cols = [c for c in cols_to_show if c in df_positions.columns]
        print(df_positions[available_cols].to_string(index=False))

except Exception as e:
    print(f"執行失敗: {e}")
