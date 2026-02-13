---
name: fin-analysis
description: 使用 uv 管理 Python 環境，並透過 yfinance 進行金融數據 (股票、加密貨幣) 抓取、走勢圖繪製與營運分析。當使用者要求分析股市、虛擬貨幣或安裝相關套件時，請使用此技能。
---

# 金融數據分析技能 (Financial Analysis)

此技能封裝了使用 `uv` 管理虛擬環境以及透過 `yfinance` 獲取全球金融數據的標準化流程。

## 核心環境配置
- **uv 執行檔路徑**: `C:\Users\AA018534\.local\bin\uv.exe`
- **Python 虛擬環境**: `C:\Users\AA018534\.local\bin\.venv\yulon\Scripts\python.exe`
- **主要套件**: `yfinance`, `pandas`, `matplotlib`

## 使用方式

### 1. 使用 uv 安裝/更新套件
當需要新套件時，請使用以下標準指令格式：
```powershell
C:\Users\AA018534\.local\bin\uv.exe pip install <package_name> --python C:\Users\AA018534\.local\bin\.venv\yulon\Scripts\python.exe
```

### 2. 金融數據抓取樣板 (yfinance)
撰寫腳本時，必須包含以下編碼處理以防止 Windows 環境亂碼：

```python
import sys
import yfinance as yf
from datetime import datetime

# 解決 Windows Console 輸出亂碼關鍵
sys.stdout.reconfigure(encoding='utf-8')

def get_market_data(symbol):
    ticker = yf.Ticker(symbol)
    # period: 1d, 5d, 1mo, 1y, max
    # interval: 1m, 5m, 1h, 1d
    data = ticker.history(period="7d", interval="1h")
    return data
```

### 3. 視覺化規範
- **字型處理**: 繪圖時必須設定 `Microsoft JhengHei` 以顯示中文。
- **輸出格式**: 
    - 快速預覽: 生成 `.jpg` 並顯示。
    - 互動分析: 生成包含 `Chart.js` 的 `.html` 檔案。

```python
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False
```

## 常見代號參考
- 台股: `2330.TW` (台積電), `2317.TW` (鴻海)
- 美股: `TSM`, `AAPL`, `NVDA`
- 加密貨幣: `BTC-USD`, `ETH-USD`

## 注意事項
- **數據頻率**: `1m` (1分鐘) 數據僅保留最近 7 天；`5m/15m` 數據保留最近 60 天。
- **跨頻道限制**: 在 LINE 環境中無法直接發送圖片附件，需改發文字摘要並引導至 Discord 查看圖表。
