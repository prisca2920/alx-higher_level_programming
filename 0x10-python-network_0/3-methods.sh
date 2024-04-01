#!/bin/bash
# shows all http methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
