#!/bin/bash
# takes a url and displays all HTTP methods the server will accept
curl -sI -X OPTIONS $1 | grep -i 'Allow:' | awk '{print substr($0, index($0, ":") + 2)}' 
