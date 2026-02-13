# 設定 API URL
$baseUrl = "https://etp.taipower.com.tw/api/asdemand/edreg/query"

# 獲取今天日期 YYYY-MM-DD
$today = Get-Date -Format "yyyy-MM-dd"

Write-Host "正在查詢日期: $today ..."

try {
    # 發送 GET 請求
    $response = Invoke-RestMethod -Uri "$baseUrl?queryDate=$today" -Method GET -ErrorAction Stop
    
    if ($response.code -ne 200) {
        Write-Host "API 錯誤: $($response.msg)"
        exit
    }

    $records = $response.data
    
    if ($null -eq $records -or $records.Count -eq 0) {
        Write-Host "今天沒有數據。"
        exit
    }

    # 準備輸出內容
    $outputLines = @()
    $outputLines += "--- E-dReg 需求數據: $today ---"
    $outputLines += "資料筆數: $($records.Count)"
    $outputLines += "------------------------------"
    $outputLines += "日期, 容量(MW), 價格"
    
    foreach ($item in $records) {
        $line = "$($item.demandDate), $($item.capacity), $($item.price)"
        $outputLines += $line
    }
    
    # 定義檔案名稱
    $filename = "edreg_data_$today.txt"
    
    # 寫入檔案 (UTF-8)
    $outputLines | Out-File -FilePath $filename -Encoding utf8
    
    Write-Host "成功！數據已儲存至: $filename"
    Write-Host "摘要: 共 $($records.Count) 筆資料，第一筆容量: $($records[0].capacity) MW"

} catch {
    Write-Host "發生錯誤: $_"
}
