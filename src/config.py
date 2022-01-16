# Algorithm configuration
ALPHA = 2e-1
GAMMA = 0.9
EPS = 3e-1
EPISODES = 1000

# Environment configuration
N_SLOTS = 10
N_ARRAYS = 4
MAX_ARRAY_SIZE = 100

# Environment internal settings
INVALID_ACTION_REWARD = -10
STEP_REWARD = -0.1
MEMORY_TO_ARRAY_REWARD = -1e-4
END_EPISODE_REWARD = 10