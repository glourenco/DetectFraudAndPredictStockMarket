import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
const_node_1 = tf.constant(1.0, dtype=tf.float32)
const_node_2 = tf.constant(2.0)

session = tf.Session()


print(session.run([const_node_1,const_node_2]))
