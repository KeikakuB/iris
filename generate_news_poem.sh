#!/bin/bash

iris -s data/sources.txt -n 20 > out/news.txt
cat out/news.txt | poet poem > out/poem.txt
cat out/poem.txt
