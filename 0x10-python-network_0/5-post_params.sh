#!/bin/bash
#sends a post request to the passed URL, and displays the body of the response
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
