#!/bin/bash

DEFAULT_DAY=$(date +%d)
DAY=${1:-$DEFAULT_DAY}

echo "[*] Running day $DAY.."

cd $DAY
python3 $DAY.py