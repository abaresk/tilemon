import math
from scipy.optimize import fsolve
import numpy as np

n = 41
cum_p = .95



def binPmf(n,k,p):
	return choose(n,k) * p**k * (1-p)**(n-k)

def choose(n,k):
	return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def binCdf(n,k,p):
	total = 0 
	for i in range(k+1):
		total += binPmf(n,i,p)
	return total

# binPmf(n,k,p)
# binCdf(n,k,p)

class BinomialSovler():
	def __init__(self, n, k, cumProb):
		self.n = n
		self.cumProb = cumProb
		self.k = k

	def _choose(self,n,k):
		return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

	def _binPmf(self,n,k,p):
		return self._choose(n,k) * p**k * (1-p)**(n-k)

	def _binCdf(self,n,k,p):
		total = 0 
		for i in range(k+1):
			total += self._binPmf(n,i,p)
		return total

	def minimand(self,p):
		return self._binCdf(self.n, self.k ,p) - self.cumProb

	def probSolver(self):
		x0 = np.asarray([0.01])
		return fsolve(self.minimand,x0)[0]



bs = BinomialSovler(15, 2, .99)
x = bs.probSolver()

print()