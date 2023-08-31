# MasterThesis

This repository contains the code used to develop my Master thesis. 

## Structure
There are two folders in the repo: 
- Code: contains the code used for training and evaluation. It also includes the policies and the tensorboard outputs.
  Regarding the policies:
  - Standing Balance with no perturbation: policies_best_model/2023_05_17_18_05_04
  - Standing Balance with AP perturbation: policies_best_model/2023_05_25_17_25_29
  - Standing Balance with ML perturbation: policies_best_model/2023_06_21_21_18_35
- Plotting: contains the scripts used for plotting the results of the evaluation of the policies, as well as the script used to obtain the figures shown in the report
- 
## Getting started
The following things are required: 
- Python 3.7.1  ```pip install python```
- MyoSuite```pip install -U myosuite```
- Mujoco ```pip install mujoco```
- Gym ```pip install gym```
- mj_envs ``` $ git clone --recursive https://github.com/vikashplus/mj_envs.git ``` and then ``` $ pip install -e . ```
- stable_baselines3 ```pip install stable-baselines3 ```


