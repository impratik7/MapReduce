#number of houses which are for resale
from mrjob.job import MRJob

class NumByOld(MRJob):
    def mapper(self, _, line):
        (price, area, loc, bed, old, *rest) = line.split(",")
        if int(old) == 1:
            yield old, 1

    def reducer(self, old, occurences):
        yield old, sum(occurences)


if __name__ == "__main__":
    NumByOld.run()
