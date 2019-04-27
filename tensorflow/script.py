import tensorflow as tf
import numpy as np
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

   observations[0] = 0.8
   observations[1] = -0.5

   try:
       prob_tensor = sess.graph.get_tensor_by_name(output_tensor_actions)
       result, = sess.run(prob_tensor, {in_tensor_observations: [observations], in_tensor_actions: [masks]})
       print("In:")
       print("", observations[0], observations[1])
       print("Out:")
       print("", getAction(result[0], result[1]), getAction(result[2], result[3]), getAction(result[4], result[5]),
             getAction(result[5], result[7]))
   except KeyError:
       print("Couldn't find classification output layer: " + output_tensor_actions + ".")
       print("Verify this a model exported from an Object Detection project.")
       exit(-1)