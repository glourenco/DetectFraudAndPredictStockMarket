import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

# y = Wx + b
# x = [1,2,3,4]
# y = [0,-1,-2,-3]

W = tf.Variable([-.5],dtype=tf.float32)
b = tf.Variable([.5],dtype=tf.float32)

x = tf.placeholder(dtype=tf.float32)
y = tf.placeholder(dtype=tf.float32)

linear_model = W * x + b

loss = tf.reduce_sum(tf.square(linear_model - y))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]

session = tf.Session()
init = tf.global_variables_initializer()
session.run(init)
#print(session.run(loss,{x:x_train,y:y_train}))
for i in range(1000):
    session.run(train,{x:x_train,y:y_train})

new_W, new_b, new_loss = session.run([W,b,loss],{x:x_train,y:y_train})
#print("new_W: %s"%new_W)
#print("new_b: %s"%new_b)
#print("new_loss: %s"%new_loss)
print(session.run(linear_model,{x:[1,2,3,4]}))