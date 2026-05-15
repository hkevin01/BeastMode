#!/bin/bash
# BeastMode Agent Setup Automation Script
# Adds VS Code Copilot custom agent configuration to any project

set -e

BEASTMODE_PATH="/home/kevin/Projects/BeastMode"
VSCODE_SETTINGS_FILE=".vscode/settings.json"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== BeastMode Agent Setup ===${NC}\n"

# Check if we're in a project directory
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}Warning: Not in a git repository root${NC}"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Create .vscode directory if it doesn't exist
mkdir -p .vscode

# Create or update settings.json with BeastMode agent configuration
if [ ! -f "$VSCODE_SETTINGS_FILE" ]; then
    echo -e "${BLUE}Creating .vscode/settings.json...${NC}"
    cat > "$VSCODE_SETTINGS_FILE" << 'EOF'
{
  "chat.agentFilesLocations": [
    "/home/kevin/Projects/BeastMode"
  ]
}
EOF
else
    echo -e "${BLUE}Updating existing .vscode/settings.json...${NC}"
    # Use jq to add/update the setting if jq is available
    if command -v jq &> /dev/null; then
        # Check if chat.agentFilesLocations already exists
        if jq -e '.["chat.agentFilesLocations"]' "$VSCODE_SETTINGS_FILE" > /dev/null 2>&1; then
            # If it exists but doesn't have BeastMode, add it
            if ! jq -e '.["chat.agentFilesLocations"] | map(select(. == "/home/kevin/Projects/BeastMode")) | length > 0' "$VSCODE_SETTINGS_FILE" > /dev/null 2>&1; then
                jq '.["chat.agentFilesLocations"] += ["/home/kevin/Projects/BeastMode"]' "$VSCODE_SETTINGS_FILE" > "$VSCODE_SETTINGS_FILE.tmp"
                mv "$VSCODE_SETTINGS_FILE.tmp" "$VSCODE_SETTINGS_FILE"
            fi
        else
            # Add the setting
            jq '.["chat.agentFilesLocations"] = ["/home/kevin/Projects/BeastMode"]' "$VSCODE_SETTINGS_FILE" > "$VSCODE_SETTINGS_FILE.tmp"
            mv "$VSCODE_SETTINGS_FILE.tmp" "$VSCODE_SETTINGS_FILE"
        fi
    else
        # Fallback: Add it as a comment if jq is not available
        if ! grep -q "chat.agentFilesLocations" "$VSCODE_SETTINGS_FILE"; then
            # Insert before the last closing brace
            sed -i '$ s/}/,\n  "chat.agentFilesLocations": ["/home\/kevin\/Projects\/BeastMode"]\n}/' "$VSCODE_SETTINGS_FILE"
        fi
    fi
fi

echo -e "${GREEN}✓ Settings configured${NC}"

# List available agents
echo -e "\n${BLUE}Available BeastMode Agents:${NC}\n"
for mode_dir in "$BEASTMODE_PATH"/modes/*/; do
    mode_name=$(basename "$mode_dir")
    agent_count=$(find "$mode_dir" -maxdepth 1 -name "*.agent.md" | wc -l)
    echo -e "  ${GREEN}✓${NC} $mode_name ($agent_count agent(s))"
done

echo -e "\n${BLUE}Settings File Location:${NC}"
echo "  $VSCODE_SETTINGS_FILE"

echo -e "\n${GREEN}Setup Complete!${NC}"
echo "BeastMode agents are now discoverable in VS Code Copilot."
echo -e "\n${YELLOW}Next Steps:${NC}"
echo "  1. Reload VS Code (Cmd+Shift+P -> Developer: Reload Window)"
echo "  2. Open Copilot Chat (Cmd+Shift+I)"
echo "  3. Select a BeastMode agent from the dropdown"
