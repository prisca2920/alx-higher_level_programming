#!/bin/bash
# takes in a url and sends a request

curl -s "$1" | wc -c
