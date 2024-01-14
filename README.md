# projects-Eyantra_lunarScout
 Our project is a self-balancing remote control bike designed for the Eyantra Lunar Scout competition. It incorporates advanced balancing algorithms and precise control mechanisms for lunar exploration challenges.
This repo contains the mathematical models and simulations done by us in octave(a similar software as that of matlab) and coppeliasim. We are currently working on the hardware part

## Files details

### Function_File.m: 
Its an octave file and the code written is similar to matlab code.
To run this you need to install control and sym library in octave.
It contains functions to calculate the state space model as well as K matrix of lqr controller for a given system defined using set of differential equations.
It is the state space modelling of a non-linear dynamical system
### Main_File.m: 
It uses the Function_file.m file to give it input and shows the output.
### Task_1A.m: 
It contains the octave code of mathematical state space model of an inverted pendulum.
### Task_1B.ttt: 
It contains the coppeliasim model of three inverted pendulum which we are trying to balance using pendulumA.py, pendulumB.py, pendulumC.py files. These files must be attached to Motor_A, Pivot_B, Motor_C objects respectively of the coppeliasim model.
### Task_2A.ttt: 
It contains the coppeliasim model of our self balancing lunar scout bike.
### Task_2B.ttt: 
It contains the coppeliasim model of our self balancing lunar scout bike where we were trying to balance it in one position.
### task2b_solution.py
It contains the python code for the coppeliasim model Task_2B.ttt. The script must be attached to the front_motor

### Task_2C.ttt: 
It contains the coppeliasim model of our self balancing lunar scout bike where we were trying to balance it in one position as well as moving the bike using some key presses.
### task2c_solution.py
It contains the python code for the coppeliasim model Task_2C.ttt. The script must be attached to the front_motor
