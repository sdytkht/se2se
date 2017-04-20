# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 00:02:08 2017

@author: kht
"""
import tensorflow as tf
import translate as tl
import numpy as np

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape = shape)
    return tf.Variable(initial)
    
einputs,dinputs,res_logits,all_attens=tl.self_decode()
einputs_t=[]
dinputs_t=[]
res_logits_t=[]
num_exp=len(res_logits)
for i in range(100):
    einputs_t.append(einputs[num_exp-i-1])
    dinputs_t.append(dinputs[num_exp-i-1])
    res_logits_t.append(res_logits[num_exp-i-1])
batch_size=32  
maxlen=13
  
sess = tf.InteractiveSession()

w_fc2 = weight_variable([128, 20])
b_fc2 = bias_variable([20])
x=tf.placeholder(tf.float32,[None,128])
y_=tf.placeholder(tf.float32,[None,20])

y_conv = tf.nn.softmax(tf.matmul(x, w_fc2) + b_fc2)

# train and evaluate the model
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
res=tf.argmax(y_conv, 1)
resreal=tf.argmax(y_, 1)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

init=tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    saver = tf.train.Saver()
    saver.restore(sess, "train/NumAdd.ckpt")
        
    for i in range(len(res_logits_t)):
        din=dinputs_t[i]
        dlogit=res_logits_t[i]
        '''
        for j in range(batch_size):
            batch_x=[]
            batch_y=np.zeros([13,20],dtype=np.float32)
            for k in range(maxlen):
                batch_y[k][din[k][j]]=1
                dx=dlogit[k][j]
                batch_x.append(dx)
            print(sess.run(correct_prediction,feed_dict={x: batch_x, y_: batch_y}))
            print('-----------------------------------------------------------------------')
        print("**************************************************************************************")
        '''
        for j in range(batch_size):
            batch_x=[]
            batch_y=np.zeros([13,20],dtype=np.float32)
            for k in range(maxlen):
                batch_y[k][din[k][j]]=1
                dx=dlogit[k][j]
                batch_x.append(dx)
            print(sess.run(res,feed_dict={x: batch_x, y_: batch_y}))
            print(sess.run(resreal,feed_dict={x: batch_x, y_: batch_y}))
            print('-----------------------------------------------------------------------')
        
