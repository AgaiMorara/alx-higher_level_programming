#!/bin/bash
# takes a url and displays all HTTP methods the server will accept
curl -s -X OPTIONS -i $1 | awk '/Allow:/ {print $2}'
