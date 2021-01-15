#Houses by no. of bedrooms
from mrjob.job import MRJob

class NumByBed(MRJob):
	def mapper(self,_,line):
		(price,area,loc,bed,*rest)=line.split(",")
		yield bed, 1
	
	def reducer(self, bed, occurences):
		yield bed, sum(occurences)

if __name__=="__main__":
	NumByBed.run()
		
