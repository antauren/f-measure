# http://www.michurin.net/computer-science/precision-and-recall.html

import numpy as np



real = 'one,two,three,four,five'
forecast = 'one,two,three,four,four'

'''
real = 'mom, dad, white, black, good, bad, long, short'
forecast = 'mom, mom, black, black, good, bad, long, long'
'''

real = real.split(',')
forecast = forecast.split(',')

intervalsNormAsIs = []


for i in real + forecast:
	i = i.strip()
	if i not in intervalsNormAsIs:
		intervalsNormAsIs.append(i)

#print()
#print(intervalsNormAsIs)

real_dict = {}
forecast_dict = {} 

for i in range(len(real)):
	real_dict[i] = real[i]
	forecast_dict[i] = forecast[i]



print(real_dict)
print(forecast_dict)

n = len(real)
matr = [[0] * n for i in range(n)]
for i in range(len(real)):
	for j in range(len(real)):
		matr[i][j] = None
		#print(matr[i][j], end = '\t')
	#print()

#print()

for i in range(n):
	for j in range(n):
		if real_dict[i] == forecast_dict[j]:
			matr[i][j] = 1
		else:
			matr[i][j] = 0
		#print(matr[i][j], end = '\t')

	#print()

a = np.array(matr)

print()
print(a)
print()


sum_rows = a.sum(axis=0)
print(sum_rows, 'суммы столбцов')

sum_columns = a.sum(axis=1)
print(sum_columns, 'суммы строк') 

diagonal = np.diag(a)
print(diagonal, 'диагональ матрицы')

sr_r = []
sr_p = []

print('\nPrecision\tRecall')

for i in range(len(diagonal)):
	if sum_columns[i] != 0:
		print ( diagonal[i]/ sum_columns[i], end="\t"*2 )

		sr_p.append( diagonal[i]/ sum_columns[i]   )

	else:
		print(None, end ="\t"*2)


	if sum_rows[i] != 0:
		print ( diagonal[i]/ sum_rows[i] )

		sr_r.append( diagonal[i]/ sum_rows[i]   )
	else:
		print(None)

sr_p = np.array(sr_p)
sr_r = np.array(sr_r)


sr_p = sr_p.mean()
sr_r = sr_r.mean()

print("-------------------------")
print(sr_r, '\t'*2, sr_p)


f = 2 * sr_r * sr_p / (sr_p + sr_r)

print ("\nФ-мера: ", round(f, 5))


def f_measure(real, forecast):
	pass