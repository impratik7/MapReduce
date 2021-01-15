#Rate of new house in powai
from mrjob.job import MRJob

class RateByPowaiNew(MRJob):
	def mapper(self,_,line):
		(price,area,loc,bed,new, *rest)=line.split(",")
		rate=float(price)/float(area)
		if loc=="Powai" and int(new)==0:
			yield "Rate of new house in powai", float(rate)
	
	def reducer(self, bed, rate):
		total=0
		numelements=0
		for i in rate:
			total = total + i
			numelements = numelements + 1
         		
		yield bed, total/numelements

if __name__=="__main__":
	RateByPowaiNew.run()
		
