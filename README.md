# Pyro 

An object-based toolbox for robot dynamic simulation, analysis, control and planning. 

### A collection of dynamic systems 
<table>
  <tr>
    <th>
    <img src="https://user-images.githubusercontent.com/16725496/162986261-b3f6950b-e417-403b-8e81-81b30a542d6c.gif" alt="rocket" width="400"/>
    </th>
    <th>
    <img src="https://user-images.githubusercontent.com/16725496/163005905-ad2205b0-150d-44de-bd43-a3b31a0bf10e.gif" alt="cartpole" width="400"/>
    </th> 
  </tr>
  <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/16725496/163005883-5ec9b6f8-d8ab-44b1-bc9d-ac5ca2d6b4a9.gif" alt="drone" width="400"/>
    </td>
    <td>
    <img src="https://user-images.githubusercontent.com/16725496/163005950-665132ae-c1d5-486c-8bf1-3c3fa9aa4140.gif" alt="mass-spring" width="400"/>
    </td> 
  </tr>
</table>

### A collection of controller synthesis tools:
<table>
  <tr>
    Dynamic programming on a discretized grid
    <th>
    <img src="https://user-images.githubusercontent.com/16725496/197412634-9104f98d-d78b-4c77-a55f-ce175002f26f.gif" alt="cost2go" width="400"/>
    </th>
    <th>
      <img src="https://user-images.githubusercontent.com/16725496/197412247-ddd810b1-b533-4675-9b49-ceb67608e47c.gif" alt="policy" width="400"/>
    </th> 
  </tr>
</table>

### A collection of analysis tools:
<table>
<tr>
    <th>
     Computing time trajectory
    <img src="https://user-images.githubusercontent.com/16725496/197414346-35a5fa67-2e44-407c-9342-d9d6f7652716.png" alt="traj" width="400"/>
    </th>
    <th>
      Phase plane analysis
    <img src="https://user-images.githubusercontent.com/16725496/197414348-12fbdf3b-7d02-4ae4-b757-95fa701cbe81.png" alt="phase-plane" width="400"/>
    </th> 
  </tr>
  <tr>
    <th>
      Generating animated simulations
    <img src="https://user-images.githubusercontent.com/16725496/197414497-1eb6af93-fa28-4c63-bb5f-da661a98ac55.gif" alt="ani" width="400"/>
    </th>
    <th>

    </th> 
  </tr>
</table>

### Unified by a standardized "dynamic system" and "controller" class hierarchy

The concept of this toolbox is a hierachy of "dynamic system" objects, from the most generic representation (any non-linear differential equations) to more system specific representations such as mechanical system (second order equations), linear state space, manipulator equations, etc. This structure is then leveraged by analysis tools, from generic tools that work for all sub-class of dynamic systems such as running simulation and phase-plane analysis, to system-specific tools that leverage specific system propreties such as modal analysis for linear sub-class:

<img width="800" src="https://user-images.githubusercontent.com/16725496/163312294-e33d791f-9cc0-48e1-acb3-8a0ebfc0c067.jpg" class="center">

The core of the library is a mother "dynamic system" class defined by a differential equation $\dot{x} = f(x,u,t)$, an output equation $y = h(x,u,t)$ and a foward kinematic equation $lines = f_{kinematic}(x,u,t)$ that is used for generating animations:

<img width="500" src="https://user-images.githubusercontent.com/16725496/163312300-faa7fe2c-178e-4c58-ae6c-4b256fd9ab92.jpg" class="center">

## Pyro tools list ##

### Dynamic objects ###

- Continuous Dynamic system - $\dot{x} = f(x,u)$
- Linear System - $\dot{x} = A x + B u $
  - Transfer function 
  - Exemples: mass-spring-damper
- Mechanical System  - $H(q)\ddot{q} + C(\dot{q},q)\dot{q} = \sum F $
  - Manipulator Robot  - $\dot{r} = J(q) \dot{q}$
    - Exemples: two link plananr robot
    - Exemples: five link plannar robot
    - Exemples: three link robot
  - Exemples: single pendulum
  - Exemples: double pendulum
  - Exemples: cart-pole
  - Exemples: planar drone
  - Exemples: rocket
- Exemples: bicycle model (planar vehicle)


### Controller objects ###

- Linear
- PID
- LQR
- Computed-Torque
- Sliding-mode controller
- End-point impedance controller for robot arms
- End-point trajectory controller for robot arms
- Tabular look-up table controller (generated by the value-iteration algorithm)


### Planner objects ###

1. RRT tree search
2. Direct collocation trajectory optimisation
3. Dynamic programming and value-iteration 


### Analysis tool ###

- Copmuting simulation
- Phase-plane analysis
- Graphical animated output of the simulations
- Cost function computation
- Linearisation (from any dynamic class to the state-space class)
- Modal analysis
- Pole/zero computation
- Bode plot
- Reachability

# How to use #

To learn how to use pyro, see the following notebook tutorials hosted on colab:

1.   [The Dynamic System class and basic functionnality](https://colab.research.google.com/drive/18eEL-n-dv9JZz732nFCMtqMThDcfD2Pr?usp=sharing)
2.   [Creating a custom dynamic class](https://colab.research.google.com/drive/1ILfRpL1zgiQZBOxwtbbpe0nl2znvzdWl?usp=sharing)
3.   [Closed-loop system and controllers objects](https://colab.research.google.com/drive/1mog1HAFN2NFEdw6sPudzW2OaTk_li0Vx?usp=sharing)
4.   The Linear System class (comin soon..)
4.   The Mechanical System class (coming soon..)
5.   [The Manipulator Robot class](https://colab.research.google.com/drive/1OILAhXRxM1r5PEB1BWaYtbR147Ff3gr1?usp=sharing)

Also see exemples scripts in pyro/examples/ 


# Installation #

### Dependencies ####
Pyro is built only using core python librairies: 
* numpy
* scipy
* matplotlib

### Using in Colab ###

```
!git clone https://github.com/SherbyRobotics/pyro
import sys
sys.path.append('/content/pyro')
import pyro
```

### Using with Anaconda and Spyder IDE ###
1. Download anaconda distribution (including spyder IDE) available here: https://www.anaconda.com/products/individual

2. Dowload pyro source code. 
A simple option for development is simply to clone the repo:
```bash
git clone https://github.com/SherbyRobotics/pyro.git
```
then add the pyro folder to the pythonpath variable of your environment. In spyder this option is found in the menu at python/PYTHONPATH manager.

3. Change the graphical backend in Spyder for enabling animation
If graphical animations are not working, try changing the graphics backend in the menu at python/Preferences/IPython console/Backend. Inline does not allow animations, it is best to use Automatic (for Windows and Ubuntu) or OS X (for Mac).











