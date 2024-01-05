import re
st=input('enter the mail:-')
data=re.findall('[a-zA-Z]+[a-zA-Z0-9]*\@gmail\.com',st)
print(data)