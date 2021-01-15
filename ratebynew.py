#Average rate of new house
from mrjob.job import MRJob

class RateByNew(MRJob):
	def mapper(self,_,line):
		(price,area,loc,bed,new, *rest)=line.split(",")
		rate=float(price)/float(area)
		if int(new)==0:
			yield "Average rate of new house", float(rate)
	
	def reducer(self, bed, rate):
		total=0
		numelements=0
		for i in rate:
			total = total + i
			numelements = numelements + 1
         		
		yield bed, total/numelements

if __name__=="__main__":
	RateByNew.run()
		
