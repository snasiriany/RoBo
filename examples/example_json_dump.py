'''
Created on June 5th, 2016

@author: Numair Mansur (numair.mansur@gmail.com)
'''

import george

from robo.maximizers.direct import Direct
from robo.models.gaussian_process import GaussianProcess
from robo.task.synthetic_functions.levy import Levy
from robo.acquisition.ei import EI
from robo.solver.bayesian_optimization import BayesianOptimization


task = Levy()
kernel = george.kernels.Matern52Kernel([1.0], ndim=1)


model = GaussianProcess(kernel)

ei = EI(model, task.X_lower, task.X_upper)

maximizer = Direct(ei, task.X_lower, task.X_upper)

bo = BayesianOptimization(acquisition_func=ei,
                          model=model,
                          maximize_func=maximizer,
                          task=task
                          ,save_dir='../JsonDumps/'
                          )

print bo.run(20)