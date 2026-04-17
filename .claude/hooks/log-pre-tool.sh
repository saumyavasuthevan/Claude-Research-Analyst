#!/bin/bash
# Pre-tool hook: logs tool name + inputs before every Claude tool call
INPUT=$(cat)

# --- Session ID management (60-min inactivity reset) ---
SESSION_FILE="/tmp/claude-session-$PPID"
SESSION_MAX_AGE=3600

if [ -f "$SESSION_FILE" ]; then
    FILE_AGE=$(( $(date +%s) - $(date -r "$SESSION_FILE" +%s) ))
    if [ "$FILE_AGE" -gt "$SESSION_MAX_AGE" ]; then
        SESSION_ID="${PPID}-$(date +%s)"
        echo "$SESSION_ID" > "$SESSION_FILE"
        rm -f "/tmp/claude-seq-${SESSION_ID}"
    else
        SESSION_ID=$(cat "$SESSION_FILE")
        touch "$SESSION_FILE"
    fi
else
    SESSION_ID="${PPID}-$(date +%s)"
    echo "$SESSION_ID" > "$SESSION_FILE"
fi

# --- Sequence counter (increments per pre_tool event) ---
SEQ_FILE="/tmp/claude-seq-$SESSION_ID"
if [ -f "$SEQ_FILE" ]; then
    SEQ=$(( $(cat "$SEQ_FILE") + 1 ))
else
    SEQ=1
fi
echo "$SEQ" > "$SEQ_FILE"

# --- Extract fields ---
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // "unknown"')
TOOL_INPUT=$(echo "$INPUT" | jq -c '.tool_input // {}')
PROJECT=$(basename "$PWD")
PROJECT_PATH="$PWD"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# --- Write log ---
LOG_DIR="$HOME/claude-logs/$PROJECT/$(date +%Y-%m-%d)"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/$SESSION_ID.jsonl"

printf '%s\n' "$(jq -nc \
  --arg ts "$TIMESTAMP" \
  --arg sid "$SESSION_ID" \
  --arg proj "$PROJECT" \
  --arg path "$PROJECT_PATH" \
  --arg tool "$TOOL_NAME" \
  --argjson seq "$SEQ" \
  --argjson input "$TOOL_INPUT" \
  '{ts: $ts, session_id: $sid, project: $proj, project_path: $path, event: "pre_tool", tool: $tool, seq: $seq, input: $input}'
)" >> "$LOG_FILE"
