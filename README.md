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
