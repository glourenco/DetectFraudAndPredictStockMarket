import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

placeholder_1 = tf.placeholder(dtype=tf.float32)
placeholder_2 = tf.placeholder(dtype=tf.float32)

session = tf.Session()
print(session.run(placeholder_1,{placeholder_1:[1.0,2.0,3.0]}))