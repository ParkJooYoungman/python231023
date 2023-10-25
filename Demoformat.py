#파일쓰기
f = open("domo.txt", "wt", encoding="utf-8")
f.write("첫번쨰\e두번쨰\n세번쨰\n")
f.close()

#파일읽기
f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
f.close()