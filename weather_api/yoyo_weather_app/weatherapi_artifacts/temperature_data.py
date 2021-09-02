import statistics


def maximum_temperature(temperatures):
    return max(temperatures)


def minimum_temperature(temperatures):
    return min(temperatures)


def average_temperature(temperatures):
    return statistics.mean(temperatures)


def median_temperature(temperatures):
    return statistics.median(temperatures)