#rate acc to no of bedrooms
from mrjob.job import MRJob

class RateByLoc(MRJob):
	def mapper(self,_,line):
		(price,area,loc,bed, *rest)=line.split(",")
		rate=float(price)/float(area)
		if int(bed):
			yield bed, float(rate)
	
	def reducer(self, bed, rate):
		total=0
		numelements=0
		for i in rate:
			total = total + i
			numelements = numelements + 1
         		
		yield bed, total/numelements

if __name__=="__main__":
	RateByLoc.run()
		
