#!/bin/bash

JSON_RPC_NOTIFICATION=$(curl -s --data-binary '{"jsonrpc": "2.0", "method": "GUI.ShowNotification", "params": {"title": "Please Wait", "message": "Running RetroArch Launch Script" },  "id":1}' -H 'content-type: application/json;' http://127.0.0.1:8080/jsonrpc)

if [ -f "$2" ]
then
    mv "$2" "$2.old"
fi

echo "JSONRPC response: $JSON_RPC_NOTIFICATION" > "$2"

sleep 1s

JSON_RPC_NOTIFICATION=$(curl -s --data-binary '{"jsonrpc": "2.0", "method": "Application.Quit", "id":1}' -H 'content-type: application/json;' http://127.0.0.1:8080/jsonrpc)

echo "JSONRPC response: $JSON_RPC_NOTIFICATION" >> "$2"

# Wait for the quit
sleep 5s

retroarch --menu >> "$2" 2>&1

echo "Restarting Kodi with $1" >> "$2"
eval "$1"
