#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Wed Oct 12 20:13:17 2022@author: alex"""import numpy as npimport matplotlib.pyplot as pltfrom scipy.interpolate import RectBivariateSpline as interpol2Dfrom scipy.interpolate import RegularGridInterpolator as rgifrom pyro.control  import controllerfrom pyro.planning import valueiteration################################################################################## RL controllers###############################################################################class greedy_controller(controller.StaticController):    ############################    def __init__(self, k, m, p):        """ """        super().__init__(k, m, p)                # Label        self.name = 'Greedy Controller'                #############################    def greedy_action_selection( self , x ):        """  select the optimal u given actual cost map """                # Place holder function                return np.zeros(self.m) # State derivative vector        #############################    def c( self , y , r , t = 0 ):        """  State feedback (y=x) - no reference - time independent """        x = y        u = self.greedy_action_selection( x )                return u        ##################################################################class epsilon_greedy_controller( greedy_controller ):        ############################    def __init__(self, k, m, p, actions_input):        """ """        super().__init__(k, m, p)                self.name = 'Epsilon Greedy Controller'                self.epsilon = 0.7                self.actions_input = actions_input # Discrete list of possible u input                    #############################    def c( self , y , r , t = 0 ):        """  State feedback (y=x) - no reference - time independent """        x = y                if np.random.uniform(0,1) < self.gamma:                # greedy behavior            u = self.greedy_action_selection( x )            else:                    # Random exploration            random_index = int(np.random.uniform( 0 , self.actions_input.size ))            u = self.actions_input[ random_index ]                 return u    ################################################################################## RL algo###############################################################################class Q_Learning_2D( valueiteration.ValueIteration_2D ):        ############################    def __init__(self, grid_sys , cost_function ):                # Dynamic system        self.grid_sys  = grid_sys         # Discretized Dynamic system class        self.sys       = grid_sys.sys     # Base Dynamic system class                # Cost function        self.cf  = cost_function                # Q Learning Parameters        self.alpha = 0.8        self.nabla = 0.8                    ##############################    def initialize(self):        """ initialize cost-to-go and policy """                J_dim = self.grid_sys.xgriddim        Q_dim = ( J_dim[0], J_dim[1] , self.grid_sys.actions_n )                self.Q             = np.zeros( Q_dim , dtype = float )        self.J             = np.zeros( J_dim , dtype = float )        self.action_policy = np.zeros( J_dim , dtype = int   )        self.Jnew          = self.J.copy()        self.Jplot         = self.J.copy()                # Set initial value              for node in range( self.grid_sys.nodes_n ):                              x = self.grid_sys.nodes_state[ node , : ]                                i = self.grid_sys.nodes_index[ node , 0 ]                j = self.grid_sys.nodes_index[ node , 1 ]                                # Final Cost                final_cost = self.cf.h( x )                                # Initial J value                self.J[i,j] = final_cost                                # Initial Q-values                for action in range( self.grid_sys.actions_n ):                                        k = self.grid_sys.actions_index[action,0]                                        self.Q[i,j,k] = final_cost                                             ##############################    def Q2J(self):        """ update the J table from Q values """                for node in range( self.grid_sys.nodes_n ):                              i = self.grid_sys.nodes_index[ node , 0 ]                j = self.grid_sys.nodes_index[ node , 1 ]                                self.J[i,j] = self.Q[i,j,:].min()                                    ##############################    def Q_update_from_index(self, s1 , a , s2 ):        """         s1: index of initial node        k:  index of taken action        s2: index of resulting node        """        # Get value of initial state        x = self.grid_sys.nodes_state[ s1 , : ]        i = self.grid_sys.nodes_index[ s1 , 0 ]        j = self.grid_sys.nodes_index[ s1 , 1 ]                # Get value of taken action        u = self.grid_sys.actions_input[ a , : ]        k = self.grid_sys.actions_index[ a , 0 ]                # Get value of next state        x_next = self.grid_sys.nodes_state[ s2 , : ]        i_next = self.grid_sys.nodes_index[ s2 , 0 ]        j_next = self.grid_sys.nodes_index[ s2 , 1 ]                # Compute optimal cost-to-go of next state minimize over all u_next actions        self.J[i_next,j_next] = self.Q[i_next,j_next,:].min()                        if self.sys.isavalidstate(x_next):                        J_next = self.J[i_next,j_next]                        # No need to interpolate since this function is based on x_next index                        # Get interpolation of current cost space            #J_interpol = interpol2D( self.grid_sys.xd[0] , self.grid_sys.xd[1] , self.J , bbox=[None, None, None, None], kx=1, ky=1,)            #J_next = J_interpol( x_next[0] , x_next[1] )                        y = self.sys.h(x, u, 0)                        Q_sample = self.cf.g(x, u, y, 0) * self.grid_sys.dt + self.alpha * J_next                    else:                        Q_sample = self.cf.INF                            # Q update        error          = Q_sample      - self.Q[i,j,k]        self.Q[i,j,k]  = self.Q[i,j,k] + self.nabla * error                # Action policy update        self.action_policy[i,j] = self.Q[i,j,:].argmin()                                        