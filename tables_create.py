CUSTOM_NUMBER=50
ITEMS_NUMBER=100

from pandas import DataFrame
from random import randint

#sheet1
custom_id = []
sku = []
purch = []
retur = []

# customers column
for i in range(1,CUSTOM_NUMBER+1):
    #number of items requested by customer
    a=randint(0,10)
    for j in range(0,a):    
        custom_id.append(i)
    
# sku column
for i in range(0,len(custom_id)):
    n=randint(1,ITEMS_NUMBER)
    sku.append(n)

# purchase and return column
for i in range(0,len(custom_id)):
    n=randint(0,1)
    purch.append(n)
    
    if n==0:
        retur.append(1)
    else:
        retur.append(0)

df1=DataFrame({'Customer ID': custom_id, 'SKU': sku, 'Purchase': purch, 'Return': retur})

df1.to_excel('table.xlsx', sheet_name='sheet1', index=False)

#sheet2
custom_id2=[]
age=[]
city=[]
face_type=[]
fav_color=[]

#customers column
for i in range(1,CUSTOM_NUMBER+1):
    custom_id2.append(i)

#age column
for i in range(0, CUSTOM_NUMBER):
    n=randint(18,101)
    age.append(n)

#city column
for i in range(0, CUSTOM_NUMBER):
    n=randint(1,101)
    city.append(n)

#face type column
for i in range(0, CUSTOM_NUMBER):
    n=randint(1,6)
    face_type.append(n)

#favorite color column
for i in range(0, CUSTOM_NUMBER):
    n=randint(1,11)
    fav_color.append(n)

df2=DataFrame({'Customer ID': custom_id2, 'Age': age, 'City': city, 'Face type': face_type, 'Favorite color': fav_color})



df2.to_excel('table2.xlsx', sheet_name='sheet2', index=False)

#sheet3
sku_2=[]
color=[]
size=[]
graphic=[] #bool
typ=[]
fabric=[]

#SKU column
for i in range(1,ITEMS_NUMBER+1):
    sku_2.append(i)

#color column
for i in range(0, len(sku_2)):
    n=randint(1,21)
    color.append(n)

#size column (centimeters)
for i in range(0, len(sku_2)):
    n=randint(1,100)
    size.append(n)

#graphic column
for i in range(0, len(sku_2)):
    n=randint(0,1)
    graphic.append(n)

#type column
for i in range(0,len(sku_2)):
    n=randint(1,5)
    typ.append(n)

#fabric column
for i in range(0,len(sku_2)):
    n=randint(1,10)
    fabric.append(n)

df3=DataFrame({'SKU': sku_2, 'Color': color, 'Size': size, 'Graphic': graphic, 'Type': typ, 'Fabric': fabric})

df3.to_excel('table3.xlsx', sheet_name='sheet2', index=False)

# Convert to CSV
df1.to_csv('table1.csv', encoding='utf-8')
df2.to_csv('table2.csv', encoding='utf-8')
df3.to_csv('table3.csv', encoding='utf-8')
    











    
    







