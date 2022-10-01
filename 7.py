def expt(b, n):
    def exptIter(counter, product):
        if counter==0:
            return product
        return exptIter(counter-1, b*product)
    return exptIter(n,1)