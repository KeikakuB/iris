#!/bin/bash

iris -s data/sources.txt > out/news.txt
cat out/news.txt | poet poem > out/poem.txt
cat out/poem.txt
