import re
with open(r"\Python\content.txt",'r+',encoding="utf8")as file:
    data=file.read()
    data1=re.sub('a','@',data)
    file.write(data1)