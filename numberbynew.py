#number of houses which are new 
from mrjob.job import MRJob

class NumByNew(MRJob):
    def mapper(self, _, line):
        (price, area, loc, bed, new, *rest) = line.split(",")
        if int(new) == 0:
            yield new, 1

    def reducer(self, new, occurences):
        yield new, sum(occurences)


if __name__ == "__main__":
    NumByNew.run()
