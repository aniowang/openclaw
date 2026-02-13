---
name: stock-trade
description: 庫存查詢、個股資訊與模擬/真實委託買賣。支援台股（透過 Shioaji API）與全球股市。
---

# 股票交易管理技能 (Stock Trade Management)

此技能專注於管理個人持股、查詢個股行情以及執行委託下單流程。支援模擬環境與永豐金 (Shioaji) 真實交易介面。

## 核心功能
1. **庫存查詢**: 
    - 預設優先調用 `D:\PythonQuantTrading_test` 下的永豐金 API 進行真實/模擬帳戶庫存查詢。
    - 備援方案：讀取本地 SQLite 資料庫。
2. **個股查詢**: 透過 `yfinance` 或 `shioaji` 獲取個股即時報價、成交量與走勢。
3. **委託下單**: 支援市價/限價之買入、賣出、融券放空、融券回補。

## 技術環境
- **API**: Shioaji (永豐金證券)
- **憑證位置**: `D:\PythonQuantTrading_test\Sinopac.pfx`
- **代碼參考**: `D:\PythonQuantTrading_test\stock_agent.py` (封裝好的 `StockAPIWrapper`)

## 標準執行流程

### 1. 庫存查詢 (Shioaji 範例)
```python
import shioaji as sj
api = sj.Shioaji(simulation=True) # 預設模擬
api.login(api_key=API_KEY, secret_key=SECRET_KEY)
positions = api.list_positions(api.stock_account)
```

### 2. 委託買賣
當使用者要求買入/賣出時，參考 `StockAPIWrapper` 中的 `market_buy`, `limit_buy` 等方法進行操作。

## 注意事項
- **安全性**: 嚴禁在對話中顯示 `credentials.py` 中的 SECRET_KEY 或身份證字號。
- **單位**: Shioaji 預設單位通常為股 (Share)，1張 = 1000股，下單時需確認單位轉換。
- **環境**: 需在擁有 `shioaji` 套件的 Python 環境下執行 (如 `yulon` venv)。
