import gym
from gym import spaces
from tqdm import tqdm
import mujoco_py
import mj_envs
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import EvalCallback
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
from tensorboard.backend.event_processing.reservoir import Reservoir
import matplotlib.pyplot as plt
import skvideo.io
import os
import random
from plottingStuff import storeData
import pickle
nb_seed = 1

# Making automatic True will run the code for the last policy that was generated
# If automatic is false, it will loop through all files in the policy_best_model folder. 
auto = 1

env_name = 'myoLegReachFixed-v1'
pkl_path = '/home/carlota/Documents/output/PKL/' + env_name + '/'

all_dirs = os.listdir(pkl_path)
if auto == 1: 
    sorted_dirs = sorted(all_dirs, key=lambda d: os.path.getctime(os.path.join(pkl_path, d)), reverse=True)
    latest_dir_name = sorted_dirs[0]
    last_file = "{}".format(latest_dir_name)
    fileName = [last_file]
elif auto == 0: 
    fileName = ['2023_03_23_08_36_38', '2023_03_23_08_37_42', '2023_03_23_08_38_59']
else: fileName = all_dirs 
print(fileName)

name = fileName[0].split('.')[0]
file_name = name
policy_path = './policy_best_model/' + env_name + '/' + file_name + '/best_model.zip'

model = PPO.load(policy_path)
env = gym.make(env_name)
env.reset()
random.seed() 
steps = 1000

dataStore = storeData(env, model, env_name, file_name, steps, True)


frames_front = dataStore['videoInfo']['framesFront']
frames_side = dataStore['videoInfo']['framesSide']
dataStore['videoInfo'] = {}

os.makedirs(pkl_path, exist_ok=True)
with open(pkl_path + name + '.pkl', 'wb') as fp:
    pickle.dump(dataStore, fp)
    print('dictionary saved successfully to file')

print('Making movie')
video_path = '/home/carlota/Documents/output/videos/' + env_name + '/'
os.makedirs( video_path, exist_ok=True)

# make a local copy 
skvideo.io.vwrite(video_path + file_name + '_side' + '.mp4', np.asarray(frames_side), outputdict={"-pix_fmt": "yuv420p"})
skvideo.io.vwrite(video_path + file_name +  '_front' + '.mp4', np.asarray(frames_front), outputdict={"-pix_fmt": "yuv420p"})
print('Movie saved successfully to file')

