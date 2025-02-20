# 2021Fall_finals


## Wifi Simulation


## Introduction:


More and more households and businesses are moving to WiFi networks as their preferred method of providing Internet access. Wireless networks are more convenient for end users and enable everyone to take full advantage of their mobile devices. They also eliminate the cabling necessary to implement a more traditional wired network. The benefits of WiFi networks are accompanied by some additional concerns. For those of us with home WiFi networks, we are our own network admins and one of the characteristics of our network that we need to understand is the WiFi signal strength. This value will be a determining factor in the activities for which your network can be used. The strength of the WiFi signal throughout the network’s coverage area directly impacts the ability of users to perform various activities in a timely manner. A weak Wifi signal is a modern day nightmare. Poor loading times and lost connections can test your patience which as students, with having to study and work on assignments, is not the situation one will want to be in. 


## Team members:
1. Bharat Jhawar
2. Ketan Mahajan(Github id - github.com/ketan96-m)
3. Shivani Edison(Github id - github.com/shivani-edison)

**Aim:** To resolve this, we have come up with a possible solution to find how to achieve the optimal WiFi signal strength to all the connecting devices. 

## Requirements:
Install pygame using `pip install pygame` in your python environment

Other packages necessary are `numpy`, `pandas` and `matplotlib`


## Code Implementation:

* The project is implemented using a GUI module named _pygame_. Pygame is a Python module which incudes computer graphics and sound library designed to use with python programming language. It allow to write rich multimedia python program for every platform that supports them.

* There are 3 key components in this simulation, which are walls, access points(the devices) and wifi router. In the simulation few combination of components will be user input on the GUI window. Also, there are user defined inputs like dimension of 2D background layout ranging in width & height of (300, 300) to (1500, 800), and wall thickness in range(1,20). **All the dimensions are in pixel size.**

**Following are the steps in code execution & simulation:**
1. When the code is executed, user is asked for an console input for background layout dimensions and wall thickness parameters. 
![image](https://user-images.githubusercontent.com/40893179/145723175-861d2578-1231-4ea3-804d-199507a52833.png)

2. Further, user provide the input for parameters in the defined range, a GUI 2D window pops up with the given layout dimensions.
3. Now on the GUI window, user has to provide the position for walls and access points. By drag and dropping the left mouse key button user can provide the location of room with rectangular peripheral walls( _higlighting in red color_) having thickness which was provided earlier, and location of access points by pressing the right mouse key button( _higlighting in blue color_ ).
![image](https://user-images.githubusercontent.com/40893179/145723498-9778254b-5fbd-441e-9bf5-64a227510b28.png)
![image](https://user-images.githubusercontent.com/40893179/145723539-91e0cbcf-2b3a-44e3-89ee-964bc85aed51.png)

4. User has to press the "Enter key" to run the simulation. In simulation, the router position is randomized across the layout( _higlighting in green color_ ).
5. At each position of router, a signal is generate which travels from router to the access point( _higlighting in magenta color_ ). This signal calculates the path distance between wifi router and access point(in pixels), also it identifies the obstacles(walls) in the pathway for calculating loss of strength.
![image](https://user-images.githubusercontent.com/40893179/145723435-51643465-76a6-4357-be72-e8596fb2c3cb.png)
6. For calculation of loss of strength, assuming the strength reduces by 0.10% for each pixel in free space and reduces by 5% for each wall pixel.
7. For each position, average of strength signal and total distance from each access point is calculated.
8. The code iterates continuously for computing the optimised position of wifi router until user presses any key.
9. At the end of simulation, the program converses towards optimised wifi router position which is showed as a yellow cross on the layout.
![image](https://user-images.githubusercontent.com/40893179/145723450-960ad014-e560-4a5c-9566-662cc02ee6c1.png)

The graph is to preview that with each iteration, the router gets closer to the optimal location as the sum of distances with all its access points keeps decreasing. The percentage of signal strength is also labelled in the the graph for each access point. This graph finding convergence proves the working of our Monte Carlo Simulation. 

![image](https://user-images.githubusercontent.com/42794476/145723846-23f76fa8-0d2b-4d0c-a921-f2b6225a5b68.png)

Entire simulation can be seen in the video linked below:

https://user-images.githubusercontent.com/40893179/145723386-9d432abf-f221-444a-a9c1-8e7bab2437b1.mp4
