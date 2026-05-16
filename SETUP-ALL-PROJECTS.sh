#!/bin/bash

#############################################################################
# Batch Setup Script - Configure All Projects with BeastMode Agents
# Purpose: Set up all projects in a directory with BeastMode agent support
# Usage: ./SETUP-ALL-PROJECTS.sh /path/to/projects/directory
#############################################################################

set -e

PROJECTS_DIR="${1:-.}"
BEASTMODE_DIR="/home/kevin/Projects/BeastMode"
SETUP_SCRIPT="$BEASTMODE_DIR/setup-beastmode.sh"

if [ ! -f "$SETUP_SCRIPT" ]; then
    echo "Error: setup-beastmode.sh not found at $SETUP_SCRIPT"
    exit 1
fi

echo "=========================================="
echo "BeastMode - Batch Setup"
echo "=========================================="
echo ""
echo "Projects directory: $PROJECTS_DIR"
echo ""

total=0
configured=0
failed=0

for project in "$PROJECTS_DIR"/*/; do
    if [ -d "$project" ]; then
        project_name=$(basename "$project")
        
        # Check if it's a git repository or has .vscode
        if [ -d "$project/.git" ] || [ -d "$project/.vscode" ] || [ -f "$project/package.json" ]; then
            ((total++))
            
            echo "[$total] Configuring: $project_name"
            
            if "$SETUP_SCRIPT" --project "$project" > /dev/null 2>&1; then
                echo "    ✓ Setup complete"
                ((configured++))
            else
                echo "    ✗ Setup failed"
                ((failed++))
            fi
        fi
    fi
done

echo ""
echo "=========================================="
echo "Summary"
echo "=========================================="
echo "Total projects found: $total"
echo "Successfully configured: $configured"
echo "Failed: $failed"
echo ""
echo "Next: Reload VS Code to see agents in chat"
