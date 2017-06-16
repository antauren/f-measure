# http://www.michurin.net/computer-science/precision-and-recall.html

import numpy as np

def f_measure(real, forecast):
	pass

#работает
real = 'one,two,three,four,five'
forecast = 'one,two,three,four,four'

#работает
#real ='ясно,ясно,дождь,ясно,ясно,дождь,дождь,ясно,снег,ясно'
#forecast = 'ясно,дождь,дождь,ясно,ясно,ясно,дождь,снег,снег,ясно'

#предварительная обработка данных
real = real.split(',')
forecast = forecast.split(',')

for i in range(len(real)):
	real[i] = real[i].strip()
	forecast[i] = forecast[i].strip()

headers = []
for i in real + forecast:
	i = i.strip()
	if i not in headers:
		headers.append(i)

dict_headers = {}
for i in range(len(headers)):
	dict_headers[headers[i]] = i

print(dict_headers)

real_dict = {}
forecast_dict = {}

m = len(real)
n = len(headers)

for i in range(m):
	real_dict[i] = real[i]
	forecast_dict[i] = forecast[i]

print(real_dict)
print(forecast_dict)

matr = np.zeros((n, n))

for i in range(m):
	j =  dict_headers[ real_dict[i] ]
	k =  dict_headers[ forecast_dict[i] ]
	matr[ k ][ j ] += 1

a = np.array(matr)

print('\n', a, '\n')

diagonal = np.diag(a)
print(diagonal, 'диагональ матрицы')

sum_columns = a.sum(axis=1)
print(sum_columns, 'суммы строк') 

sum_rows = a.sum(axis=0)
print(sum_rows, 'суммы столбцов')

sr_r = []
sr_p = []

print('\nPrecision\tRecall')

for i in range(len(diagonal)):
	if sum_columns[i] != 0:
		sr_r.append( diagonal[i]/ sum_columns[i]   )
	if sum_rows[i] != 0:
		sr_p.append( diagonal[i]/ sum_rows[i]   )

sr_p = np.array(sr_p)
sr_r = np.array(sr_r)

sr_p = sr_p.mean()
sr_r = sr_r.mean()

print("-------------------------")
print(round(sr_p, 5), '\t'*2, round(sr_r,5))

f = 2 * sr_r * sr_p / (sr_p + sr_r)

print ("\nФ-мера: ", round(f, 5))