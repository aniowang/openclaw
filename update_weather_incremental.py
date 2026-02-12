import sqlite3
import pandas as pd
import os
import glob

# 設定路徑
DB_PATH = r"D:\00數據管理組\02工作\weatherapi.db"
CSV_DIR = r"D:\00數據管理組\02工作" # 根據 ipynb，CSV 可能直接在此目錄或子目錄

def update_weather_incremental():
    try:
        conn = sqlite3.connect(DB_PATH)
        
        # 1. 自動偵測欄位名稱 (處理亂碼)
        df_sample = pd.read_sql_query("SELECT * FROM weather LIMIT 1", conn)
        cols = df_sample.columns.tolist()
        col_id = cols[1]    # 代號
        col_time = cols[2]  # 觀測時間
        
        # 2. 取得資料庫中最新的觀測時間
        print("正在檢查資料庫現有資料時間...")
        last_time_query = f"SELECT MAX([{col_time}]) FROM weather"
        last_time_str = pd.read_sql_query(last_time_query, conn).iloc[0, 0]
        
        if last_time_str:
            last_time = pd.to_datetime(last_time_str)
            print(f"資料庫最新紀錄時間為: {last_time}")
        else:
            last_time = pd.Timestamp.min
            print("資料庫為空，將執行全量匯入。")

        # 3. 掃描 CSV 檔案
        # 搜尋包含 CWA_Weather 的 CSV 檔案
        csv_files = glob.glob(os.path.join(CSV_DIR, "**", "CWA_Weather_*.csv"), recursive=True)
        if not csv_files:
            print("找不到任何 CSV 檔案。")
            return

        print(f"找到 {len(csv_files)} 個檔案，準備進行增量比對...")

        total_new_rows = 0
        for file in sorted(csv_files): # 按日期排序處理
            try:
                # 預讀檔案，過濾掉舊日期
                # 使用 utf-8-sig 處理 BOM，如果還是亂碼則嘗試 big5
                try:
                    df = pd.read_csv(file, encoding='utf-8-sig')
                except:
                    df = pd.read_csv(file, encoding='big5')

                # 轉換 CSV 內的時間欄位
                df[col_time] = pd.to_datetime(df[col_time])
                
                # 【增量過濾】只保留比資料庫最新的資料
                new_data = df[df[col_time] > last_time]
                
                if not new_data.empty:
                    new_data.to_sql('weather', conn, if_exists='append', index=False)
                    total_new_rows += len(new_data)
                    # 更新 last_time 以供下一個檔案比對 (加速用)
                    last_time = new_data[col_time].max()
                    print(f"檔案 {os.path.basename(file)}: 匯入 {len(new_data)} 筆新資料。")
                else:
                    # print(f"檔案 {os.path.basename(file)}: 無新資料，跳過。")
                    pass
                    
            except Exception as e:
                print(f"處理檔案 {file} 時發生錯誤: {e}")

        # 4. 執行最終去重 (保險起見，針對可能重複的同秒資料)
        if total_new_rows > 0:
            print(f"共匯入 {total_new_rows} 筆資料。執行最後去重複作業...")
            cursor = conn.cursor()
            dedup_sql = f"""
            DELETE FROM weather 
            WHERE rowid NOT IN (
                SELECT MIN(rowid) 
                FROM weather 
                GROUP BY [{col_id}], [{col_time}]
            );
            """
            cursor.execute(dedup_sql)
            conn.commit()
            print(f"作業完成。資料庫現在是最新的。")
        else:
            print("沒有偵測到更新的資料。")

        conn.close()

    except Exception as e:
        print(f"增量更新作業失敗: {e}")

if __name__ == "__main__":
    update_weather_incremental()
