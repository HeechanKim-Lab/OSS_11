#!/usr/bin/env bash
# ==============================================================================
#  DAILY GRASS SUSTENANCE - LOCAL LAUNCHD INSTALLER
#  Installs a macOS LaunchAgent to automatically run feed_the_grass.sh every day
# ==============================================================================

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLIST_LABEL="com.heechan.dailygrass"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_LABEL}.plist"
LOG_DIR="$REPO_DIR/reports"
mkdir -p "$LOG_DIR"

echo "=== 🌿 GitHub Contribution Grass Sustenance Installer ==="
echo "Repo path: $REPO_DIR"

cat <<EOF > "$PLIST_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${PLIST_LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${REPO_DIR}/feed_the_grass.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>15</integer>
    </dict>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/Library/Frameworks/Python.framework/Versions/3.13/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    </dict>
    <key>StandardOutPath</key>
    <string>${LOG_DIR}/launchd_grass.log</string>
    <key>StandardErrorPath</key>
    <string>${LOG_DIR}/launchd_grass.err</string>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
EOF

chmod 644 "$PLIST_PATH"

# Unload previous if exists, then load
launchctl unload "$PLIST_PATH" 2>/dev/null || true
launchctl load "$PLIST_PATH"

echo ">>> [SUCCESS] LaunchAgent installed and loaded at $PLIST_PATH"
echo ">>> It will automatically execute feed_the_grass.sh every day at 09:15 local time!"
echo ">>> To test run manually anytime: ./feed_the_grass.sh"
echo ">>> To uninstall: launchctl unload $PLIST_PATH && rm $PLIST_PATH"
