import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 設定字體以支援中文
matplotlib.rc('font', family='Microsoft JhengHei')

db_path = r"D:\00數據管理組\02工作\weatherapi.db"

def search_xindian_and_plot():
    try:
        conn = sqlite3.connect(db_path)
        
        # 讀取全部資料表內容來進行模糊匹配（解決編碼顯示問題）
        df_all = pd.read_sql_query("SELECT * FROM weather", conn)
        conn.close()

        station_col = df_all.columns[0]
        time_col = df_all.columns[2]
        rain_col = df_all.columns[27]

        # 直接找尋包含「新店」二字的站點 (不論它顯示成什麼亂碼)
        # 由於剛才 list_stations.py 顯示的結果有亂碼，我們試著直接用正確的「新店」字串去 filter
        # 如果 sqlite 裡的資料是正確的 utf-8 或 big5，這應該能運作
        
        target_station = "新店"
        df_xindian = df_all[df_all[station_col].str.contains(target_station, na=False, case=False)]

        if df_xindian.empty:
            print("無法直接匹配『新店』，改為搜尋可能代表新店的站點編號...")
            # 新店站通常編號是 C0A520 或類似
            id_col = df_all.columns[1]
            df_xindian = df_all[df_all[id_col].astype(str).str.contains("C0A520", na=False)]

        if df_xindian.empty:
            print("依舊找不到新店資料。目前有的站名範例:")
            print(df_all[station_col].unique()[:20])
            return

        print(f"找到 {len(df_xindian)} 筆新店相關資料。")

        # 資料整理
        df_xindian[time_col] = pd.to_datetime(df_xindian[time_col])
        df_xindian[rain_col] = pd.to_numeric(df_xindian[rain_col], errors='coerce').fillna(0)
        df_xindian = df_xindian.sort_values(by=time_col)

        # 繪圖
        plt.figure(figsize=(12, 6))
        plt.plot(df_xindian[time_col], df_xindian[rain_col], marker='o', markersize=4, linestyle='-', color='#1f77b4')
        plt.title('新店地區降雨量變化圖 (全部資料區間)', fontsize=15)
        plt.xlabel('觀測時間', fontsize=12)
        plt.ylabel('累積降雨量 (mm)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # 儲存圖片
        output_image = "xindian_rain_chart_final.png"
        plt.savefig(output_image)
        print(f"圖表已生成: {output_image}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_xindian_and_plot()
