def primeFactorsCalc(n):
  prime_factors = set()
  if n % 2 == 0:
    prime_factors.add(2)
  while n % 2 == 0:
    n = n // 2
    if n == 1:
      return prime_factors
  for factor in range(3, n + 1, 2):
    if n % factor == 0:
      prime_factors.add(factor)
      while n % factor == 0:
        n = n // factor
        if n == 1:
          return prime_factors

def persistanceCalc(n):
  start = n
  print("Start term  = ", n)
  persistance = 0
  while len(str(n)) > 1:
    next = 1
    for i in str(n):
      next *= int(i)
    n = next
    persistance += 1
    print("Term ", persistance + 1, " = ", n)
  print(str(start) + "\'s persistance is", persistance)
  print("Prime factors of", start, "are", primeFactorsCalc(start), "\n")

def quickPC(n):
  start = n
  persistance = 0
  while len(str(n)) > 1:
    next = 1
    for i in str(n):
      next *= int(i)
    n = next
    persistance += 1
  return (persistance, start)

xpoints = []
ypoints = []
largest = [0, 0]
for i in range(1000000):
  Pi = quickPC(i)
  if Pi[0] > largest[0]:
    persistanceCalc(i)
    largest = Pi
  xpoints.append(Pi)
  ypoints.append(i)

print(len(xpoints), len(ypoints))
plt.scatter(xpoints, ypoints)
plt.show()