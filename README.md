# Advent_of_Code_2024

# Day 1
Dependency that the input file needs to be modified. I did this by changing the triple spaces with commas.
```
$ sed -i 's/   /,/g' input.txt
```
Or in vim/neovim: `:%s/   /,/g`
