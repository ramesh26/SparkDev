from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('spark://LAPTOP-LAI03S4B.localdomain:7077')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)

txt = sc.textFile('text.csv')
print(txt.count())
