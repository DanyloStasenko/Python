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

# todo: Currently program is only loading graph and showing operations inside.
#  Looking how to: 'send data to inputs' and 'get results'