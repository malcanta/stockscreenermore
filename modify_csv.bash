#! /usr/bin/bash
cut -d"," -f2- spy500_tickers.csv > spy_tickers.csv
sed '1d' spy_tickers.csv
