from simulator import Simulator, Map, Agent
from devices import Device
import numpy as np


env = Simulator()
map = Map()
map.get_map_from_geom2d(env, radius=100, n_pts=180)

robot = Agent(env, radius=3, color=(1, 0, 0, 0.5), v_max=1.5)
robot.reset(init_state=np.array([0, 40, 0]))
device = Device(env, parent=robot, kp=np.array([[-10, 0], [10, 0]]), color=[0, 1, 0, 0.1])
while True:
    env._render()
    robot.update(v=np.array([1, 0]))