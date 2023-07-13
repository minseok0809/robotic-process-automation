from glob import glob

file_list = glob("harry_potter_" +"*.txt")
with open("Harry Potter Sorcerer's Stone.txt", "w") as f:
    for file in file_list:
        with open(file) as text:
            for line in text:
                f.write(line)
       

# Reference
# [Python] Merge Files (파일 병합, 파일 합치기) (Tistory Blog IT Log)
# https://newly0513.tistory.com/183