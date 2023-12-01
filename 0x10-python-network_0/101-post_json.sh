#!/bin/bash
# POST Request JSON, display body of response
curl -sX POST $1 -H"Content-Type: application/json" -d @$2 -L
