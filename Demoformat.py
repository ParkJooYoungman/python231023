



#파일쓰기
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번쨰\n두번쨰\n세번쨰\n")
f.close()
#기존파일에 첨부
f = open("demo.txt", "wt", encoding = "utf-8")
f.write("다른 내용을 첨부\n")
f.close()

#파일읽기
f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)


#처음으로 리셋
f.seek(0)
print(f.readline(),end="")
print(f.readline(),end="")

f.seek(0)
lst = f.readlines()
for item in lst:
    print(item, end="")

f.close()
