with open('mca.csv','r') as csvfile :
    data = csv.reader(csvfile)
    for i in data:
        print(i)