#!/bin/bash
#send a request and retrieve status code of response
curl -s -o /dev/null -w "%{http_code}" $1 
