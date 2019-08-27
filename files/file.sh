ls -lrt /usr/lib/jvm | awk -F" " 'NR==3{print $9}'

