#!/bin/bash
#fetches header of a given server response and extracts the value of content-Length
curl -sI "$1" | awk 'tolower($1) == "content-length:" {print $2}'
