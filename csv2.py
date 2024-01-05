import csv 
with open('mca.csv','w',newline='')as csvfile:
    data=csv.writer(csvfile)
    data.writerow(['id','name','mobile','email'])
    data2=[
        [1,'john',9024354657,'john@example.com'],
        []
    ]






