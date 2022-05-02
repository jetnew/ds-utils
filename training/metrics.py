class Mean:
    """
    Mean accumulator.
    Useful for accumulating the average metrics in a loop, e.g. in model training.
    ```
    a = Mean()
    b = Mean()
    for i in range(10):
        a.update(i)
        b.update(i * 2)
    c = a + b
    print(f"Average of {len(c)} numbers: {c}")
    ```    
    """
    def __init__(self, total=0, count=0):
        self.total = total
        self.count = count
    def update(self, val):
        self.total += val
        self.count += 1
    def __repr__(self):
        return str(self.total / self.count)
    def __add__(self, mean):
        return Mean(self.total + mean.total, self.count + mean.count)
    def __len__(self):
        return self.count