# OpenClaw 技術評估報告

---

## 介紹 OpenClaw(Moltbot/Clawdbot)

### 什麼是 OpenClaw？

OpenClaw是一個開源的 AI Agent 框架，專為企業級對話機器人設計。其核心特色包括：

| 特性                 | 說明                                                         |
| -------------------- | ------------------------------------------------------------ |
| **開源免費**   | MIT License，社群維護，無授權費用                            |
| **多平台整合** | 支援 Line、Telegram、Discord、Slack、WhatsApp 等主流通訊軟體 |
| **Agent 架構** | 基於 Sub-Agent 的設計，可獨立執行複雜任務                    |
| **技能擴充**   | 支援自定義 Skill 模組，透過 JavaScript/Node.js 擴充功能      |
| **地端部署**   | 可完全運行於內部伺服器，資料不出企業網域                     |
| **記憶體管理** | 內建 MEMORY.md 長期記憶與每日筆記機制                        |

### 官方網頁

[https://docs.openclaw.ai/](https://docs.openclaw.ai/)

### 適用場景

- 企業內部行政助理
- 客服機器人
- 專案管理助手
- 工作流程自動化

---

## 1. 環境選擇

### 1.1 地端部署 (On-Premise)

#### 優勢

- **資料主權完整**：所有對話資料、Token 記錄均儲存於內部伺服器，符合資安法規
- **無外部依賴**：不需連線至國外 API 服務(自營運LLM)，網路中斷時仍可運作
- **成本可控**：一次性硬體投資，無訂閱制費用

#### 劣勢

- **維護成本**：需 IT 人力進行系統更新、安全修補
- **擴充彈性受限**：硬體容量固定，瞬間高負載可能造成效能瓶頸
- **Ngrok 需求**：若需串接外部 Webhook，仍需透過 Ngrok 或類似工具建立通道

#### 建議硬體規格

```
CPU: 4 核心以上
RAM: 8GB 以上
SSD: 50GB 以上
OS: Windows 10/11 或 Linux (Ubuntu 20.04+) 或 Mac
```

---

### 1.2 雲端部署 (Cloud)

#### 優勢

- **快速上線**：無需準備實體伺服器，帳號開通即可使用
- **彈性擴充**：可隨流量需求調整資源 (Auto-scaling)
- **高可用性**：雲端供應商提供 SLA 保障 (通常 99.9% 以上)
- **跨地點存取**：團隊成員可從任何地點連線管理後台

#### 劣勢

- **月費成本**：依據使用量計費，長期營運成本較高
- **資料外流疑慮**：對話資料存放於雲端，需評估供應商資安等級
- **網路依賴**：完全仰賴網路連線，斷線即無法使用

---

## 2. 安裝指引

### 2.1 前置作業

#### 通用環境需求

```bash
# Node.js 版本需求
node --version  # 需為 v18 或 v20 LTS

# Git (用於版本控制與更新)
git --version

# 套件管理工具
npm --version   # 需為 v9 或 v10
```

#### Windows 環境額外需求

- **Windows Terminal** (建議)：提供更好的命令列體驗 (CMD 或 PowerShell)

#### 地端部署額外準備

- **防火牆設定**：允許 inbound/outbound HTTP/HTTPS 連線
- **網域或 IP**：Ngrok tunnel 或固定 IP 用於 Webhook 接收，預設會用18789 Port
- **備份機制**：定時備份 `/memory` 與 `/data` 目錄

---

### 2.2 安裝語法(示範版本是2026.1.24-3所以語法會是clawdbot)

#### 標準安裝 

```bash
# 1. Windows 安裝 Clawdbot CLI  
iwr -useb https://molt.bot/install.ps1 | iex 

# 2. 初始化專案 
clawdbot onboard --install-daemon 

# 3. 啟動服務
clawdbot gateway

# 4. commandline介面
clawdbot tui

# 5. WebUI介面
clawdbot dashboard

```

#### Docker 部署 (推薦用於雲端，廠商經常有一鍵佈署)

```bash
# 使用官方映像檔
docker pull clawdbot/clawdbot:latest

# 執行容器
docker run -d \
  --name clawdbot \
  -p 3000:3000 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/memory:/app/memory \
  clawdbot/clawdbot:latest
```

---

### 2.3 組態檔介紹

#### 主要設定檔結構

```yaml
# config.yaml 或 config.json
bot:
  name: "MyAgent"
  session: "main"
  model: "opencode/minimax-m2.1-free"  # 或其他模型供應商

channels:
  line:
    enabled: true
    channelId: "${LINE_CHANNEL_ID}"
    channelSecret: "${LINE_CHANNEL_SECRET}"
    accessToken: "${LINE_ACCESS_TOKEN}"
  telegram:
    enabled: false
    token: "${TELEGRAM_BOT_TOKEN}"

system:
  logLevel: "info"  # debug | info | warn | error
  dataDir: "./data"
  memoryDir: "./memory"

features:
  heartbeatEnabled: true
  autoRestart: true
  maxMemoryAgeDays: 30
```

#### 環境變數管理 (建議)

```bash
# 使用 .env 檔案管理敏感資訊
CLAWDBOT_LINE_CHANNEL_ID=your_channel_id
CLAWDBOT_LINE_CHANNEL_SECRET=your_channel_secret
CLAWDBOT_LINE_ACCESS_TOKEN=your_access_token
OPENAI_API_KEY=your_openai_key  # 若使用 OpenAI 模型
```

### LLM模型授權檔(重要)

```bash
# 通常是用來保存金鑰，切勿洩漏
C:\Users\USER\\.clawdbot\agents\main\agent\auth-profiles.json
```

---

## 3. 串接 Line

### 3.1 前置作業

#### Ngrok 設定 (開發測試用)

```bash
# 安裝 Ngrok
npm install -g ngrok

# 官網取得靜態網址作為Line的Webhook

# 環境內登入取得憑證
ngrok config add-authtoken [金鑰]

# 啟動 tunnel 到 Clawdbot 預設 port (18789)
ngrok http --url=[申請的靜態網址] 18789

```

#### Line Official Account (LINE OA) 設定

1. **建立 LINE OA**

   - 登入 [LINE Developers Console](https://developers.line.biz/)
   - 建立 Provider (若無)
   - 建立 Channel → 選擇 "LINE Official Account API"
2. **取得金鑰**

   - Channel ID
   - Channel Secret
   - Access Token (需設定短期或長期有效期限)
3. **Webhook 設定**

   ```text
   Webhook URL 格式：
   https://你的網域/callback/line

   或使用 Ngrok 測試：
   https://abcd-1234.ngrok.io/callback/line
   ```

---

### 3.2 設定 Channel 與測試 Webhook

### 透過config可以更快速設定

#### 1. 設定 Channel 配置

```yaml
# config.yaml
channels:
  line:
    enabled: true
    webhookPath: "/callback/line"
    verify: true  # 啟用 Webhook 驗證
```

#### 2. 測試 Webhook 連線

```bash
# 開發模式下測試
clawdbot dev --inspect

# 使用 LINE Developer Tools 測試
# Messaging API → Webhook → 使用 "Verify" 功能
```

#### 3. 驗證回調 (Callback)

```javascript
// LINE Webhook 事件類型
const lineEvents = [
  "message",      // 文字、圖片、語音等訊息
  "follow",       // 加入好友
  "unfollow",     // 封鎖
  "join",         // 加入群組
  "leave",        // 離開群組
  "memberJoined", // 群組新成員
  "postback",     // Postback 動作
  "beacon"        // Beacon 設備
];
```

#### 4. 測試腳本

```bash
# 發送測試訊息至 LINE
curl -X POST https://api.line.me/v2/bot/message/push \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LINE_ACCESS_TOKEN" \
  -d '{
    "to": "USER_ID",
    "messages": [{
      "type": "text",
      "text": "Clawdbot 串接成功！"
    }]
  }'
```

---

### 3.3 Channels後臺驗證好友

### 後臺驗證(建議)

```plaintext
OpenClaw: access not configured.

Your lineUserId: U0d68147d573e7cac834a51c6e49b8dd2

Pairing code: NXL7EN26

Ask the bot owner to approve with:
openclaw pairing approve line <code>
```

---

## 4. Agent 設定

### 4.1 MD 檔作用說明

#### 核心 MD 檔架構

```
├── SOUL.md          # Agent 角色定義 (人格、說話風格)
├── USER.md          # 使用者偏好設定
├── AGENTS.md        # 工作區指南 (給其他 Agent 看的)
├── TOOLS.md         # 工具清單與偏好設定
├── MEMORY.md        # 長期記憶 (跨 Session 持久化)
├── HEARTBEAT.md     # 心跳任務清單 (背景工作)
└── IDENTITY.md      # Agent 身份識別資訊
```

#### SOUL.md 範例

```markdown
# SOUL.md - Who You Are

## Core Truths
- Be genuinely helpful, not performatively helpful
- Have opinions and preferences
- Be resourceful before asking
- Earn trust through competence

## Boundaries
- Private things stay private
- Ask before acting externally

## Vibe
Be the assistant you'd actually want to talk to.
```

#### MEMORY.md 用途

- 記錄重大決策與上下文
- 長期累積使用者偏好
- 跨 Session 保持對話連續性
- **注意**：僅在主對話載入，團體聊天中不載入 (資安考量)

---

### 4.2 排程功能說明

#### Crontab 排程 (Cron Job)

```json
{
  "action": "add",
  "job": {
    "name": "每日天氣報告",
    "sessionTarget": "main",
    "schedule": {
      "kind": "cron",
      "expr": "0 8 * * 1-5"  // 週一至週五 08:00
    },
    "payload": {
      "kind": "systemEvent",
      "text": "早安！今日台北天氣：晴朗，氣溫 28-32 度"
    }
  }
}
```

#### 排程指令管理

```bash
# 列出所有排程
clawdbot cron list

# 手動執行排程
clawdbot cron run <jobId>

# 刪除排程
clawdbot cron remove <jobId>
```

#### 心跳任務 (Heartbeat)

```markdown
# HEARTBEAT.md

定期檢查項目：
1. 郵件檢查 (每 30 分鐘)
2. 日曆事件 (每小時)
3. 系統健康狀態 (每 15 分鐘)

注意事項：
- 深夜 (23:00-08:00) 除非緊急，否則不主動通知
- 批量檢查以節省 API 呼叫
```

---

### 4.3 Tool跟Skill

### Tools（Clawdbot 內建工具）

| 類別           | Tool                 | 功能                                                          |
| -------------- | -------------------- | ------------------------------------------------------------- |
| **檔案** | `read`             | 讀取檔案                                                      |
|                | `write`            | 寫入檔案                                                      |
|                | `edit`             | 編輯檔案                                                      |
|                | `apply_patch`      | 結構化修補                                                    |
| **執行** | `exec`             | 執行 Shell 命令                                               |
|                | `process`          | 管理背景程序                                                  |
| **網頁** | `web_search`       | 網頁搜尋（Brave API）                                         |
|                | `web_fetch`        | 擷取網頁內容                                                  |
|                | `browser`          | 瀏覽器控制，需要安裝插件 (clawdbot browser extension install) |
| **記憶** | `memory_search`    | 搜尋長期記憶                                                  |
|                | `memory_get`       | 讀取記憶片段                                                  |
| **對話** | `message`          | 發送訊息（Line/Telegram/Discord 等）                          |
| **排程** | `cron`             | 排程管理                                                      |
|                | `gateway`          | Gateway 重啟/更新                                             |
| **節點** | `nodes`            | 配對節點控制                                                  |
|                | `canvas`           | Canvas 渲染                                                   |
| **會話** | `sessions_list`    | 列出會話                                                      |
|                | `sessions_history` | 查看歷史                                                      |
|                | `sessions_send`    | 發送訊息到會話                                                |
|                | `sessions_spawn`   | 生成子代理                                                    |
|                | `session_status`   | 會話狀態                                                      |
|                | `agents_list`      | 列出可用代理                                                  |
| **圖片** | `image`            | 圖片分析                                                      |
| **其他** | `tts`              | 文字轉語音                                                    |

#### Skills（自訂技能）

| Skill                  | 功能                             | 位置                          |
| ---------------------- | -------------------------------- | ----------------------------- |
| **stock-trade**  | 股票交易（Shioaji API）          | `clawd/skills/stock-trade`  |
| **fin-analysis** | 金融分析（yfinance）             | `clawd/skills/fin-analysis` |
| **GitHub**       | GitHub 操作（gh CLI / REST API） | Clawdbot 全域技能             |
| **slack**        | Slack 控制                       | Clawdbot 全域技能             |
| **notion**       | Notion API                       | Clawdbot 全域技能             |
| **bluebubbles**  | BlueBubbles 外部通道             | Clawdbot 全域技能             |

#### Skill 結構

```
skills/
├── skill-name/
│   ├── SKILL.md      # 技能說明文件
│   ├── index.js      # 主要程式碼
│   └── package.json  # 依賴設定
```

#### 基礎 Skill 範例

```javascript
// skills/hello/SKILL.md
/*
# Hello Skill
說明：簡單的問候技能
*/

// skills/hello/index.js
module.exports = {
  name: 'hello',
  description: 'Say hello to the user',
  async execute(context) {
    const { message, agent } = context;
    await message.reply('你好！我是 Clawdbot，很高興見到你！');
  }
};
```

---

### 4.4 容災機制

#### 自動重啟

```yaml
# config.yaml
system:
  autoRestart:
    enabled: true
    maxRestarts: 5
    restartDelayMs: 10000
    crashReport: true
```

#### ~資料備份策略(尚未驗證)~

```bash
# 定時備份 script (建議配合 crontab)
#!/bin/bash
BACKUP_DIR="/backup/clawdbot"
DATE=$(date +%Y%m%d_%H%M%S)

# 備份 memory 目錄
tar -czf $BACKUP_DIR/memory_$DATE.tar.gz /path/to/memory

# 備份 config
cp /path/to/config.yaml $BACKUP_DIR/config_$DATE.yaml

# 保留最近 30 天備份
find $BACKUP_DIR -name "*.tar.gz" -mtime +30 -delete
```

#### 健康檢查端點

```yaml
# config.yaml
system:
  healthCheck:
    enabled: true
    endpoint: "/health"
    intervalMs: 30000
```

---

### 4.5 Token 使用量控制

#### 模型用量監控

```yaml
# config.yaml
monitoring:
  tokenTracking:
    enabled: true
    dailyLimit: 100000    # 每日上限
    warnThreshold: 0.8    # 80% 時警告
    logPath: "./logs/tokens.log"
```

#### 用量查詢指令

```bash
# 查看今日用量
clawdbot status

# 查看詳細報告
clawdbot report --period weekly
```

#### 單一對話(Session)執行壓縮來減少上下文長度

```bash
# 壓縮上下文
/compact
```

#### 成本優化建議

1. **模型選擇**：依任務複雜度選擇模型，避免過度使用高價模型
2. **快取機制**：重複問題使用快取回答
3. **對話摘要**：長對話自動摘要以減少 Token 消耗
4. **Prompt 優化**：精簡 Prompt 避免冗贅

---

## 5. 資安考量

### 5.1 優勢

| 資安面向             | 說明                                               |
| -------------------- | -------------------------------------------------- |
| **地端部署**   | (包含LLM的情況下)資料完全不外流，符合 GDPR、個資法 |
| **開源透明**   | 原始碼可審計，無後門疑虑                           |
| **自定義整合** | 可串接企業內部認證 (LDAP/OAuth)                    |
| **通道加密**   | LINE API 本身使用 HTTPS 加密傳輸                   |
| **權限管控**   | 可細緻控制 Agent 能力與存取範圍                    |
| **審計日誌**   | 完整記錄所有 API 呼叫與對話內容                    |
| **隔離設計**   | Agent 間相互隔離，單點失效不影響全局               |

---

### 5.2 劣勢與風險

| 風險項目                   | 說明                                 | 緩解措施                      |
| -------------------------- | ------------------------------------ | ----------------------------- |
| **自行維護負擔**     | 地端部署需自行處理資安更新           | 建立定期修補流程              |
| **Ngrok 依賴**       | 測試環境需使用 Ngrok，可能成為攻擊面 | 生產環境使用正式網域與 SSL    |
| **LLM 供應商信任**   | 若使用外部 LLM API，對話資料會外流   | 優先使用地端 LLM 或可信供應商 |
| **Prompt Injection** | 使用者可能嘗試注入惡意指令           | 輸入過濾 + 輸出驗證           |
| **敏感資訊外洩**     | Agent 可能意外透露機密資訊           | 建立敏感資訊過濾規則          |
| **權限過大**         | Agent 可能取得超出所需的系統權限     | 最小權限原則 + 沙箱隔離       |
| **人為疏失**         | 錯誤的配置可能導致資安漏洞           | 建立配置審核流程              |

---

## 6. 總結與建議

### 評估摘要

| 項目               | 地端部署       | 雲端部署     |
| ------------------ | -------------- | ------------ |
| **初期成本** | 高 (硬體投資)  | 低           |
| **長期成本** | 低(自有LLM)    | 高 (訂閱制)  |
| **資安等級** | 高             | 中           |
| **維護難度** | 高             | 低           |
| **擴充彈性** | 低             | 高           |
| **建議對象** | 高資安需求企業 | 快速驗證需求 |

### 推薦策略

1. **POC 階段**：使用雲端 Ngrok 快速驗證功能
2. **試運行**：地端部署，串接內部系統
3. **正式上線**：評估是否遷移至雲端或持續地端
4. **定期審計**：每季檢視資安配置與依賴更新

---

**文件版本**：v1.1
**更新日期**：2026-02-12
**維護人員**：Anio
