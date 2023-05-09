cd ../../data 
cat final_train.txt | tr '[:space:]' '[\n*]' | grep -v "^\s*$" | sort | uniq -c | sort -bnr | sed 's/^[ \t]*//' > ../results/word_counts.txt
