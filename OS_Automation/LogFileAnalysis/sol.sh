#!/bin/bash

# Name of the log file and the file to store the line number
LOG_FILE="record.log"
LAST_READ_LINE_FILE="last_read_line.txt"


# If the line number file doesn't exist, create it and initialize it with 0
if [ ! -f "$LAST_READ_LINE_FILE" ]; then
    echo "0" > "$LAST_READ_LINE_FILE"
fi

# Read the line number from the file
LAST_READ_LINE=$(cat "$LAST_READ_LINE_FILE")

# Calculate the number of lines in the log file
TOTAL_LINES=$(wc -l < "$LOG_FILE")

# If new lines have been added since the last read
if [ "$TOTAL_LINES" -gt "$LAST_READ_LINE" ]; then
    # Get the new lines
    NEW_LINES=$(tail -n +$(($LAST_READ_LINE + 1)) "$LOG_FILE")

    # Search for WARNING and CRITICAL keywords in the new lines
    if echo "$NEW_LINES" | grep -E 'WARNING|CRITICAL'; then
        sudo echo "WARNING or CRITICAL found in $LOG_FILE" 
    fi

    # Update the line number file
    echo "$TOTAL_LINES" > "$LAST_READ_LINE_FILE"
fi
