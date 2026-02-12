# HEARTBEAT.md

## Periodic Tasks (Triggered by Heartbeat)

# (已取消) 新北市新店區天氣報告
# 1.  **新北市新店區天氣報告:**
#     *   **Check interval:** 30 minutes.
#     *   **Action:**
#         1.  Check `memory/heartbeat-state.json` to see if `weather_xindian` was run in the last 30 minutes.
#         2.  If not, perform `web_search(query='新北市新店區天氣')`.
#         3.  Summarize the results and send them as a message.
#         4.  Update the timestamp for `weather_xindian` in `memory/heartbeat-state.json`.

# Keep this file empty (or with only comments) to skip heartbeat API calls.
# Add tasks below when you want the agent to check something periodically.
