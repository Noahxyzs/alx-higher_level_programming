#!/bin/bash
# bash script for posting json data files and testing a server
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
