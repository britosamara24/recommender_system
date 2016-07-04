from __future__ import division
import pandas as pd
import numpy as np
import operator

CUSTOM_NUMBER=50
ITEMS_NUMBER=100
ITEMS_PER_CUST=10

df1=pd.read_csv('table1.csv')
df2=pd.read_csv('table2.csv')
df3=pd.read_csv('table2.csv')

customerid=df1['Customer ID']
sku=df1['SKU']
purch=df1['Purchase']
purch_customer_items=np.zeros((50,10))
retur_customer_items=np.zeros((50,10))

for i in range(0,CUSTOM_NUMBER):
    n=0
    m=0
    for j in range(0, len(customerid)):
        if (customerid[j]==(i+1) and purch[j]==1): # Filling row i with the items purchased by client i 
            purch_customer_items[i][n]=sku[j]
            n=n+1
        if (customerid[j]==(i+1) and purch[j]==0): # Filling row i with the items returned by client i
            retur_customer_items[i][m]=sku[j]
            m=m+1

# Jaccard similarity (intersection divided by union)
def jaccard(id1, id2, mat):
    intersec=0
    union=0
    for i in range(0,ITEMS_PER_CUST):
        for j in range(0,ITEMS_PER_CUST):
            a=mat[id1-1,i]    
            b=mat[id2-1,j]    
            if (a!=0 and b!=0):
                if a==b:
                    intersec=intersec+1

    for i in range(0,ITEMS_PER_CUST):
        if mat[id1-1,i]!=0: 
            union=union+1
        if mat[id2-1,i]!=0: 
            union=union+1
        for j in range(0,ITEMS_PER_CUST):
            if mat[id1-1,i]==mat[id2-1,j]:
                if mat[id1-1,i]!=0:
                    union=union-1
    if union<=0:
        result=0
    else:
        result=intersec/union
    return result

def similarity(id1,id2):
    jac_p=jaccard(id1,id2,purch_customer_items)
    jac_r=jaccard(id1,id2,retur_customer_items)
    result=(jac_p+0.2*jac_r)/1.2
    return result

def user_sim_list(customer):
    dic={}
    for j in range(0,CUSTOM_NUMBER):
        dic[j+1]=similarity(customer,j+1)
    sorted_dic=sorted(dic.items(),key=operator.itemgetter(1))
    return sorted_dic

for i in range(0,1): #for i in range(0,CUSTOM_NUMBER):
    print '\n'
    print 'Similarity list for customer ', (i+1)
    print '\n'
    print user_sim_list(i+1)
    print '\n'

print purch_customer_items
print retur_customer_items
print '\n'
