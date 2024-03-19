#!/bin/bash

echo "Останавливаем"
pkill -9 -f python3
cd /app

python3 setup.py

echo "Стартуем"
nohup python3 main.py &
