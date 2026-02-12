import sys
sys.path.append(r'D:\PythonQuantTrading_test')
import shioaji as sj
from stock_agent import StockAPIWrapper
import os

# 建立 Shioaji API 實例 (使用模擬模式)
api = sj.Shioaji(simulation=True)

# 登入
api_key = os.environ.get('SHIOAJI_API_KEY', '')
secret_key = os.environ.get('SHIOAJI_SECRET_KEY', '')

if api_key and secret_key:
    api.login(api_key=api_key, secret_key=secret_key)
else:
    try:
        from credentials import API_KEY, SECRET_KEY
        api.login(api_key=API_KEY, secret_key=SECRET_KEY)
    except:
        print("無法找到有效的 API 憑證")
        sys.exit(1)

wrapper = StockAPIWrapper(api)

stock_id = "00991A"
quantity = 1000 # 1 張 = 1000 股

print(f"正在為 {stock_id} 獲取最新價格...")
contract = wrapper.get_contract(stock_id)

# 獲取最新成交價作為市價單的參考價格 (Shioaji市價單也需要一個參考價)
# 由於是模擬交易，這裡先簡單地用 K 線的收盤價作為參考
from datetime import datetime, timedelta
start_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

try:
    kbars = wrapper.get_kbars(stock_id=stock_id, start_date=start_date, end_date=end_date)
    if not kbars.empty:
        latest_price = kbars['Close'].iloc[-1]
        print(f"最新參考價格為: {latest_price}")
        print(f"正在下達 {stock_id} 買進 {quantity} 股的市價單...")
        trade = wrapper.market_buy(contract, latest_price, quantity)
        if trade and hasattr(trade, 'order') and hasattr(trade.order, 'id'):
            print(f"買進委託成功！訂單ID: {trade.order.id}")
        else:
            print("買進委託成功，但無法取得訂單ID。")
    else:
        print(f"無法獲取 {stock_id} 的最新價格，請稍後再試。")
except Exception as e:
    print(f"下單失敗: {e}")


api.logout()
