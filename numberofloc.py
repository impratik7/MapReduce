#Houses in location
from mrjob.job import MRJob

class NumByLoc(MRJob):
	def mapper(self,_,line):
		(price,area,loc,*rest)=line.split(",")
		yield loc, 1
	
	def reducer(self, loc, occurences):
		yield loc, sum(occurences)

if __name__=="__main__":
	NumByLoc.run()
		
