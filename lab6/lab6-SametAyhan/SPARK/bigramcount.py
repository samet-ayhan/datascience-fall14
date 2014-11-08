from operator import add
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("BigramCount").setMaster("local")

sc = SparkContext(conf=conf)

sentences = sc.textFile('bible+shakes.nopunc') \
	.glom() \
	.map(lambda x: " ".join(x)) \
	.flatMap(lambda x: x.split("."))

bigrams = sentences.map(lambda x:x.split()) \
	.flatMap(lambda x: [((x[i],x[i+1]),1) for i in range(0,len(x)-1)])

bigrams_reduced = bigrams.reduceByKey(lambda x,y:x+y)

bigrams_reduced.sortByKey().saveAsTextFile("output")

