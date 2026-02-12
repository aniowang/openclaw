import sys
sys.path.append(r'D:\PythonQuantTrading_test')
import shioaji as sj
from stock_agent import StockAPIWrapper
import os
from datetime import datetime, timedelta

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
quantity = 133000 # 133 張 = 133000 股

print(f"正在為 {stock_id} 獲取最新價格...")
contract = wrapper.get_contract(stock_id)

start_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

try:
    kbars = wrapper.get_kbars(stock_id=stock_id, start_date=start_date, end_date=end_date)
    if not kbars.empty:
        latest_price = kbars['Close'].iloc[-1]
        print(f"最新參考價格為: {latest_price}")
        print(f"正在下達 {stock_id} 賣出 {quantity} 股的市價單...")
        trade = wrapper.market_sell(contract, latest_price, quantity)
        if trade and hasattr(trade, 'order') and hasattr(trade.order, 'id'):
            print(f"賣出委託成功！訂單ID: {trade.order.id}")
        else:
            print("賣出委託成功，但無法取得訂單ID。")
    else:
        print(f"無法獲取 {stock_id} 的最新價格，請稍後再試。")
except Exception as e:
    print(f"下單失敗: {e}")

api.logout()
