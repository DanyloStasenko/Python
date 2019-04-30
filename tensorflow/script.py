# Main script which doing following things:
#   generating random X and Y values in range [-1, 1]
#   using generated values as input for trained tensorflow model
#   getting and printing result after neural network processing
# Example:
#   6381 2019-05-01 02:24:01.112620
#   In:  0.86 0.17
#   Out:  1 0 0 1
# Explanation:
#   Line 1: '6381' means 'count' - how many times script generated values and called nn to process it.
#           Then we can see 'date' and 'time' (useful for performance testing purposes)
#   Line 2: Input values
#   Line 3: Output values

import tensorflow as tf
import numpy as np
import random
import datetime

from tensorflow.python.platform import gfile

GRAPH_PB_PATH = 'model/cube.pb'

in_tensor_observations = 'vector_observation:0'
in_tensor_actions = 'action_masks:0'
output_tensor_actions = 'action:0'

def getAction(x, y):
    result = 0
    if (x - y > 1):
        result = 1
    return result

def getRandom():
    number = random.random()
    minus = random.random()
    if (minus < 0.5):
        number = number * -1
    return number

with tf.Session() as sess:
   with gfile.FastGFile(GRAPH_PB_PATH,'rb') as file:
       graph_def = tf.GraphDef()
   graph_def.ParseFromString(file.read())
   sess.graph.as_default()
   tf.import_graph_def(graph_def, name='')

   observations = np.empty(2, dtype=float)
   masks = np.empty(8, dtype=float)
   masks[0] = 1
   masks[1] = 1
   masks[2] = 1
   masks[3] = 1
   masks[4] = 1
   masks[5] = 1
   masks[6] = 1
   masks[7] = 1


   start = datetime.datetime.now()
   i = 0
   while ((datetime.datetime.now() - start).seconds <= 10):
       try:
           i = i + 1
           print(i, datetime.datetime.now())
           observations[0] = ("%.2f" % getRandom())
           observations[1] = "%.2f" % getRandom()

           prob_tensor = sess.graph.get_tensor_by_name(output_tensor_actions)
           result, = sess.run(prob_tensor, {in_tensor_observations: [observations], in_tensor_actions: [masks]})
           # print("In:")
           print("In: ", observations[0], observations[1])
           # print("Out:")
           print("Out: ", getAction(result[0], result[1]), getAction(result[2], result[3]), getAction(result[4], result[5]),
                 getAction(result[5], result[7]))
       except KeyError:
           print("Couldn't find classification output layer: " + output_tensor_actions + ".")
           print("Verify this a model exported from an Object Detection project.")
           exit(-1)
   print("Statistics: Operations:", i, ", Time: 10 seconds, Average per second:", i / 10)