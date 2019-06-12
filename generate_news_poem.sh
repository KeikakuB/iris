#!/bin/bash

echo "http://cnn.com" | iris > out/news.txt
cat out/news.txt | poet poem > out/poem.txt
cat out/poem.txt
