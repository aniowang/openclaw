import requests
import json
import datetime
import os

# 設定 API URL
BASE_URL = 'https://etp.taipower.com.tw/api/asdemand/edreg/query'

def get_today_data():
    # 獲取今天日期 YYYY-MM-DD
    today = datetime.date.today().strftime('%Y-%m-%d')
    
    print(f"正在查詢日期: {today} ...")
    
    try:
        # 發送 GET 請求
        response = requests.get(f"{BASE_URL}?queryDate={today}", timeout=15)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('code') != 200:
            print(f"API 錯誤: {data.get('msg', '未知錯誤')}")
            return

        records = data.get('data', [])
        
        if not records:
            print("今天沒有數據。")
            return

        # 準備輸出內容
        output_lines = []
        output_lines.append(f"--- E-dReg 需求數據: {today} ---")
        output_lines.append(f"資料筆數: {len(records)}")
        output_lines.append("-" * 30)
        output_lines.append("日期, 容量(MW), 價格")
        
        for item in records:
            demand_date = item.get('demandDate', '')
            capacity = item.get('capacity', 0)
            price = item.get('price', 0)
            output_lines.append(f"{demand_date}, {capacity}, {price}")
            
        # 定義檔案名稱
        filename = f"edreg_data_{today}.txt"
        
        # 寫入檔案
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))
            
        print(f"成功！數據已儲存至: {filename}")
        
        # 顯示摘要以供確認
        print(f"摘要: 共 {len(records)} 筆資料，第一筆容量: {records[0].get('capacity')} MW")

    except requests.RequestException as e:
        print(f"網路請求失敗: {e}")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    get_today_data()
