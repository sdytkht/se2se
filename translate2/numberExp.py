# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:20:24 2017

@author: kht
"""
import random
#import numpy as np

charmap={"+":"19","-":"20","*":"21","/":"22","^":"23","n":"24","end":"25"}
def createExp(maxlen,batchsize):
    y=[]
    x=[]
    max_xlen=1
    max_ylen=1
    for i in range(batchsize):
        x1=[]
        y1=[]
        
        num1=random.randint(0,10**maxlen)
        num2=random.randint(0,10**maxlen)
        res=num1+num2
        
        yi=0
        if res==0:
            y1.append(int(yi))
        while res>0:
            yi=res%10
            y1.append(int(yi))
            res=res//10
        y1.append(19)
        
        if max_ylen<len(y1):
            max_ylen=len(y1)
            
        if num1==0 and num2==0:
            x1.append(0)
        while num1>0 or num2>0:
            a1=int(num1%10)
            a2=int(num2%10)
            xi=a1+a2
            x1.append(int(xi))
            num1=num1//10
            num2=num2//10
        x1.append(19)
        if max_xlen<len(x1):
            max_xlen=len(x1)
        
        x.append(x1)
        y.append(y1)
    '''    
    x_n=np.zeros((max_xlen,batchsize))
    x_mask=np.zeros((max_xlen,batchsize))
    y_n=np.zeros((max_ylen,batchsize))
    y_mask=np.zeros((max_ylen,batchsize))
    for i in range(batchsize):
        for j in range(len(x[i])):
            x_n[j,i]=x[i][j]
            x_mask[j,i]=1
        for j in range(len(y[i])):
            y_n[j,i]=y[i][j]
            y_mask[j,i]=1
    '''
    return x,y
    
if __name__=='__main__':
    x_n,y_n,=createExp(10,5)
    print(x_n)
    print('----------------------------------------------')
    print(y_n)