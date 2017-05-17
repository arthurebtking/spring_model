## spring model hexagonal lattice

a = 2
row_length = 10
num_rows = 3
pos = np.zeros((N,2))
x_coordinate = np.zeros(N)
x_coordinate_offset = np.zeros(N)
y_coordinate = np.zeros(N)
y_coordinate_offset = np.zeros(N)

for i in xrange(row_length):
	x_coordinate[i] = i*a
	x_coordinate_offset[i] = i*a + (0.5*a)
		
for j in range(num_rows):
	y_coordinate[i] = (np.sqrt(3) * 0.5)*a 
	
for j in xrange(num_rows):
	for i in xrange(row_length):
		if i % 2 ==0:
			pos[i,j] = x_coordinate[i],y_coordinate[j]
		else:
			pos[i,j] = x_coordinate_offset[i],y_coordinate[j]
		
	 
		
		

