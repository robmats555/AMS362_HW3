
# Problem #1 

## Setup
In the first problem, we are given a 2D Cartesian coordinate system to represent a section of a river. 
We are also given the speed of the water based on the x-coordinate of the location in the river.
Finally, we are told that a ferryboat is attempting to cross from point (a,0) to (0,0) where a = 7777. 
Given three different initial speeds of the boat, 7, 14, and 21, we are told to graph the trajectory the boat would make on its path from east to west.

## Algorithm Description
First we must set up the differential equations for the boat. These are given in the image below:

<img src="ferryboat_de.PNG" width=500>

Then after eliminating the explicit dependence on t in the two DE's we get:

<img src="ferryboat_simpler_de.PNG" width=300>

Finally we can implement the Runge-Kutta method, starting *t* from *a* (7777) and with a step size *h* of -.1 all the way to zero. This algorithm is described in the image below.

<img src="rk.PNG" width=500>

The algorithm is run iteratively, using the previous iteration's result for *y* for the next *y* and at the same time decreasing the x-value by the step size *h*. 

## Pseudocode

    # h is step_size
    def runge_kutta(x, y, h, vb):
       k1 = f(x, y, vb)
       k2 = f(x + (.5*h), y + (.5 * h * k1), vb)
       k3 = f(x + (.5*h), y + (.5 * h * k2), vb)
       k4 = f(x + h, y + (h * k3), vb)
       return y * (1/6)*h*(k1 + 2k2 + 2k3 + k4)
       
    def f(x, y, vb):
      dx/dy provided in the setup for the problem
    
    def main():
      step_size = -0.1
      x = generate points from 7777 to 0 with step_size
      y = [0]
      vb = [7, 14, 21]
      
      for initial_speed in vb:
          for x_cor in x:
              append to y result from runge_kutta(x, y, h, vb)
          plot the points
          reset y
        

