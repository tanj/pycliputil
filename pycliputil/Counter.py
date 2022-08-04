# Counters can increment in defined ways


class CounterBase(object):
    def __init__(self, start, end=None, step=1, match=None):
        self.start = start
        self.end = end
        self.step = step
        self.count = self.start
        self.match = match

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.end:
            raise StopIteration
        else:
            return self.inc()

    def reset(self):
        """
        @brief      reset count

        @details    reset counter to `start`

        @param      self

        @return     return old count
        """
        temp = self.count
        self.count = self.start
        return temp

    def inc(self):
        """
       @brief      increment counter

       @details    increment self.counter

       @param      none

       @return     return previous count (for use in __next__)
       """
        self.count += self.step
        return self.count - self.step
