from operator import add
from pyspark import *
from pyspark.files import SparkFiles
from pyspark.serializers import read_int
sc = SparkContext()
f = sc.textFile("README.md")
wc = f.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
wc.saveAsTextFile("wc_out.txt")

#TRANSFORMATION

distFile = sc.textFile("README.md")
distFile.map(lambda x: x.split(' ')).collect()
distFile.flatMap(lambda x: x.split(' ')).collect()

#ACTION
from operator import add
f = sc.textFile("README.md")
words = f.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1))
words.reduceByKey(add).collect()

#PERSISTANCE
from operator import add
f = ("README.md")
w = tokens.(lambda x: x.split(' ')).map(lambda x: (x, 1)).cache()
w.reduceByKey(add).collect()


#BROADCAST VARIABLES
broadcastVar = sc.broadcast(list(range(1, 4)))
broadcastVar.value

#ACCUMULATOR
accum = sc.accumulator(0)
rdd = sc.parallelize([1, 2, 3, 4])


def f(x):
    global accum
    accum += x


rdd.foreach(f)
accum.value

#WORDCOUNT
from operator import add
f = sc.textFile("README.md")
wc = f.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
wc.saveAsTextFile("wc_out.txt")