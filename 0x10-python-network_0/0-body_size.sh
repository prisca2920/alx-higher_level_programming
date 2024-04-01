#!/bin/bash
# sends a request to a url
curl -s "$1" | wc -c
