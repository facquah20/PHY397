# Python Assignment on Heat Simulation

## The Heat Equation

Simulation of Fourier's heat equation using python.

### How to simulate this problem
According to Fourier's heat equation the rate of heat loss is directly proportional to temperature gradient where A and k are constants.

### The Algorithm
1. Calculate the rate of heat loss, p, using the initial temperature, equilibrium temperature (Te) and length l of the rod.
2. Now we will consider smaller distances dl and time dt to calculate the heat transfered dq. Since the simulation will run from 0 to t_final with an interval dt, the total simulation count will be t_final/dt.
3. As the time increases, l, is also considered to be dl x count.
4. Doing a simple substitution will get you the temperature T at any time dt x count
5. Ensure you store the values of heate transferred and temperature in an array for plotting.

### How to Run The Simulation
1. Ensure you have numpy,matplotlib and of course python installed on your local machine
2. Navigate to the directory containing heat_simulation.py
3. Type python heat_simulation.py to run the script