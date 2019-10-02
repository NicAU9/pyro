# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:28:17 2018

@author: Alexandre
"""

import numpy as np

from pyro.dynamic  import pendulum
from pyro.planning import discretizer
from pyro.analysis import costfunction
from pyro.planning import valueiteration
from pyro.control  import controller

sys  = pendulum.SinglePendulum()

# Discrete world 
grid_sys = discretizer.GridDynamicSystem( sys )

# Cost Function
qcf = costfunction.QuadraticCostFunction(
    q=np.ones(sys.n),
    r=np.ones(sys.m),
    v=np.zeros(sys.p)
)

qcf.xbar = np.array([ -3.14 , 0 ]) # target
qcf.INF  = 10000

# VI algo
vi = valueiteration.ValueIteration_2D( grid_sys , qcf )

vi.initialize()
vi.load_data('simple_pendulum_vi')
#vi.compute_steps(200)
#vi.load_data()
vi.assign_interpol_controller()
vi.plot_policy(0)
vi.plot_cost2go()
vi.save_data('simple_pendulum_vi')

#asign controller
cl_sys = controller.ClosedLoopSystem( sys , vi.ctl )

# Simulation and animation
x0   = [0,0]
tf   = 10
sim = cl_sys.compute_trajectory(x0, tf, costfunc=qcf)
cl_sys.plot_trajectory(sim, 'xuj')
cl_sys.get_animator().animate_simulation(sim)