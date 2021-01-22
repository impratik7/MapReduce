# Find Flat with cheapest rate
from mrjob.job import MRJob
from mrjob.step import MRStep


class CheapestByRate(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(mapper=self.mapper2, reducer=self.reducer2)
        ]

    def mapper1(self, _, line):
        (price, area, loc, bed, *rest) = line.split(",")
        rate = float(price)/float(area)
        yield (loc, price, area, bed), rate

    def reducer1(self, info, rate):
        total = 0
        numelements = 0
        for i in rate:
            total = total + i
            numelements = numelements + 1

        yield None, (total/numelements, info)

    def mapper2(self, key, value):
        yield key, value

    def reducer2(self, key, value):
        yield min(value)


if __name__ == "__main__":
    CheapestByRate.run()
