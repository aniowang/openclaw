import sys
sys.path.append(r'D:\PythonQuantTrading_test')
import shioaji as sj
from stock_agent import StockAPIWrapper

# 建立 Shioaji API 實例 (使用模擬模式)
api = sj.Shioaji(simulation=True)

# 登入 (使用環境變數或憑證)
import os
api_key = os.environ.get('SHIOAJI_API_KEY', '')
secret_key = os.environ.get('SHIOAJI_SECRET_KEY', '')

if api_key and secret_key:
    api.login(api_key=api_key, secret_key=secret_key)
else:
    # 嘗試從憑證文件讀取
    try:
        from credentials import API_KEY, SECRET_KEY
        api.login(api_key=API_KEY, secret_key=SECRET_KEY)
    except:
        print("無法找到有效的 API 憑證")
        sys.exit(1)

# 建立 StockAPIWrapper 並獲取持倉
wrapper = StockAPIWrapper(api)
positions = wrapper.get_positions()

if positions is not None and len(positions) > 0:
    print("=== 您的持股部位 ===")
    print(positions.to_string())
else:
    print("目前無持股部位")
