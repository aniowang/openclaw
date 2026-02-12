# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Cron Job (Scheduling) - Clawdbot API

**CRITICAL:** Must use this JSON format for `default_api:cron(action="add")` to add a new schedule.

- **`sessionTarget`** must be `"main"` or `"default"` for most common agent sessions.
- **`schedule`** must use `kind: "cron"` and a **6-part** `expr` (no explicit year).
- **`payload`** must use `kind: "systemEvent"` and `text`.

```json
{
  "action": "add",
  "job": {
    "name": "My Reminder Name",
    "sessionTarget": "main",
    "schedule": {
      "kind": "cron",
      "expr": "0 30 14 29 1 ?"  // Seconds:0, Minute:30, Hour:14, Day:29, Month:1, DayOfWeek:? (6 parts)
    },
    "payload": {
      "kind": "systemEvent",
      "text": "This is the message that will be delivered."
    }
  }
}
```

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

### Environment / Paths
- Node.js: "C:\Program Files\nodejs\node.exe" (Use absolute path when `node` is not in PATH)
- Python (Yulon venv): "C:\Users\AA018534\.local\bin\.venv\yulon\Scripts\python.exe"

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
