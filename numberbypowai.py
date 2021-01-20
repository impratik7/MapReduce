#No of houses in powai
from mrjob.job import MRJob

class NumByPowai(MRJob):
    def mapper(self, _, line):
        (price, area, loc, *rest) = line.split(",")
        if loc == "Powai":
            yield loc, 1

    def reducer(self, loc, occurences):
        yield loc, sum(occurences)


if __name__ == "__main__":
    NumByPowai.run()
