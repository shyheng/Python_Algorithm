import csv

# file = open("zph.csv","w",encoding="utf8",newline='')
# w = csv.writer(file)


# w.writerow(['name','age','sore'])
# w.writerow(['张三','12','90'])

# w.writerows(
#     [
#         ["name","age","sex"],
#         ["张","19","男"]
#     ]
# )

file = open("zph.csv",'r',encoding="utf8",newline='')
r = csv.reader(file)
for data in r:
    print(data)

file.close()