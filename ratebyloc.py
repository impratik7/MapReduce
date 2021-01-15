#Find rate as per location
from mrjob.job import MRJob

class RateByLoc(MRJob):
	def mapper(self,_,line):
		(price,area,loc,*rest)=line.split(",")
		rate=float(price)/float(area)
		yield loc, float(rate)
	
	def reducer(self, loc, rate):
		total=0
		numelements=0
		for i in rate:
			total = total + i
			numelements = numelements + 1
			
		yield loc, total/numelements

if __name__=="__main__":
	RateByLoc.run()
		
