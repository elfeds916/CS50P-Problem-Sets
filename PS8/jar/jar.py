class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity should be positive integer")
        # self.capacity is the total capacity of the jar
        self._capacity = capacity
        self._size = 0
    

    def __str__(self):
        # self.size is the number of cookies inside the jar
        return self.size * "🍪"

    
    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceeds the jar capacity")
        if self.size + n > self.capacity:
            raise ValueError("Jar cannot accommodate all the cookies")
        # incrementing the # of cookies in the jar by the # of cookies deposited
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        # decrementing the # of cookies in teh jar by the # of cookies withdrawn
        self._size -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size
