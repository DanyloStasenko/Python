import tensorflow as tf
from tensorflow.python.platform import gfile
GRAPH_PB_PATH = 'frozen_graph_def.pb'
with tf.Session() as sess:
   print("load graph")
   with gfile.FastGFile(GRAPH_PB_PATH,'rb') as f:
       graph_def = tf.GraphDef()
   graph_def.ParseFromString(f.read())
   sess.graph.as_default()
   tf.import_graph_def(graph_def, name='')
   graph_nodes=[n for n in graph_def.node]
   names = []
   for t in graph_nodes:
      names.append(t.name)
   print(names)

# These names are part of the model and cannot be changed.
output_layer = 'action:0'
input_node = 'vector_observation:0'
input_node2 = 'action_masks:0'


with tf.Session() as sess:
   import numpy as geek

   observations = geek.empty(6, dtype=float)
   masks = geek.empty(8, dtype=float)
   masks[0] = 1
   masks[1] = 1
   masks[2] = 1
   masks[3] = 1
   masks[4] = 1
   masks[5] = 1
   masks[6] = 1
   masks[7] = 1

   observations[0] = -0.9
   observations[1] = -0.1
   observations[2] = -0.1
   observations[3] = -0.3
   observations[4] = -0.1
   observations[5] = -0.1

   try:
      prob_tensor = sess.graph.get_tensor_by_name(output_layer)
      predictions, = sess.run(prob_tensor, {input_node: [observations], input_node2:[masks]})
      print("Results:")
      print(predictions[0])
      print(predictions[1])
      print(predictions[2])
      print(predictions[3])
      print(predictions[4])
      print(predictions[5])
      print(predictions[6])
      print(predictions[7])
   except KeyError:
      print("Couldn't find classification output layer: " + output_layer + ".")
      print("Verify this a model exported from an Object Detection project.")
      exit(-1)

# todo: Continue playing with input
#  Got first results:
# -22.331755
# 0.0
# 0.0
# -22.332441
# -0.89462394
# -0.52553546
# -2.0909839
# -0.1318933

# need to investigate how they were formed
# and how it will change according to changed input values
