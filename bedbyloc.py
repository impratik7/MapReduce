#No. of bedrooms in houses in powai
from mrjob.job import MRJob

class BedbyLoc(MRJob):
    def mapper(self, _, line):
        (price, area, loc,bed, *rest) = line.split(",")
        if loc == "Powai":
            yield bed, 1

    def reducer(self, bed, occurences):
        yield bed, sum(occurences)


if __name__ == "__main__":
    BedbyLoc.run()
