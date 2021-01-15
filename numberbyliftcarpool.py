#no. of luxury flat (lift+carpark+pool)
from mrjob.job import MRJob

class NumByLuxury(MRJob):
    def mapper(self, _, line):
        (price, area, loc, bed, old, gym, lift,car, *rest, pool) = line.split(",")
        if int(lift) == 1 and int(car)==1 and int(pool)==1:
            yield "Luxury flat", 1

    def reducer(self, pool, occurences):
        yield pool, sum(occurences)


if __name__ == "__main__":
    NumByLuxury.run()
