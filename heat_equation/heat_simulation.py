
import matplotlib.pyplot as plt
'''
Python program to simulate the rate of flow of heat using 
Fourier's law of heat conduction
dQ/dt = -KA(T-Te)/d

Given parameters k=0.1, A=1 d=0.1, Te=300, To = 500, dt=0.01 and tfinal=100

All parameters are in their SI units
'''


 # initialising parameters
k = 0.1
A = 1
d = 0.1
equilibrim_temp = 300
initial_temp = 500
t_final = 100
dt = 0.01
initial_heat = 0 # at t=0, heat absorbed is zero

 # Get rate of heat loss per second
p = k*A*((initial_temp-equilibrim_temp)/d)

temperatures = [initial_temp] # keeps track of the temperatures
heats_absorbed = [initial_heat] # keeps track of the heat energy absorbed


simulation_count = int(t_final/dt) # number of times simulation will run
count = 1 # keeps track of simulation count

dl = d/simulation_count #taking smaller distances of d

while count <= simulation_count:
	dq = p*dt*count 
	heats_absorbed.append(dq)

	temperature = initial_temp-((p*dl*count)/(A*k))
	temperatures.append(temperature)
	print('Heat transfered = {}J, temperature = {} K'.format(dq, temperature))

	count+=1


# plotting temperature against heat

plt.plot(heats_absorbed,temperatures)
plt.xlabel('Heat Absorbed')
plt.ylabel('Temperature')
plt.title("A Graph of Temperature Against Heat")
plt.show()