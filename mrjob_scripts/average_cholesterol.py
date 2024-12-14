from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class AverageCholesterol(MRJob):
    def mapper(self, _, line):
        reader = csv.reader([line])
        for row in reader:
            try:
                cholesterol = float(row[2])
                heart_disease = int(row[6])
                if cholesterol > 0:
                    yield heart_disease, (cholesterol, 1)
            except ValueError:
                pass

    def reducer(self, key, values):
        total_cholesterol = 0
        count = 0
        for cholesterol, num in values:
            total_cholesterol += cholesterol
            count += num
        if count > 0:
            yield key, total_cholesterol / count

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer)]
