f = open("Harry Potter Sorcerer's Stone.txt", "r")
lines = f.readlines()
f.close()

cnt = 1
fileName_Num = 1

for line in lines:
    fileName = "harry_potter_" + str(fileName_Num) + '.txt'
    
    fw = open(fileName, "a")
    fw.write(line)
    fw.close()
    
    if cnt == 40:
        fileName_Num = fileName_Num + 1
        cnt = 0
    
    cnt = cnt + 1
    
    

# Reference
# 파일을 원하는 만큼 분할(쪼개기) (Naver Blog 엠스방 해답을 찾기위해...)
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wwwkasa&logNo=220902577519