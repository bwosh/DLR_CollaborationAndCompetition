import numpy as np
import time

from tqdm import tqdm
from unityagents import UnityEnvironment

from ddpg.agent import Agent
from opts import Opts
from utils.plot import save_plot_results

# Parameters
opts = Opts()

# Create environment
env = UnityEnvironment(file_name=opts.executable)
brain_name = env.brain_names[0]
brain = env.brains[brain_name]

# Gather environment properties
env_info = env.reset(train_mode=True)[brain_name]
states = env_info.vector_observations
num_agents = len(env_info.agents)
action_size = brain.vector_action_space_size
state_size = states.shape[1]

agent = Agent(opts.num_agents, state_size, action_size, opts)

def play(brain_name, agent, env, pbar, warmup):
    # Reset environment and variables
    env_info = env.reset(train_mode=True)[brain_name]      
    states = env_info.vector_observations             
    scores = np.zeros(num_agents)
    move=0                          

    while True:
        # Act & get results
        actions = agent.act(states, warmup)
        env_info = env.step(actions)[brain_name] 

        # Gather data
        rewards = env_info.rewards                        
        dones = env_info.local_done                        
        scores += env_info.rewards                        
        next_states = env_info.vector_observations

        # Make agent step
        agent.step(states, actions, rewards, next_states, dones, warmup)
        states = next_states 

        pbar.update()
        move+=1

        if np.any(dones):
            break

    return scores, move

# Try to solve environment
episode_scores = []
pbar = tqdm(total=opts.episodes*opts.moves_per_episode)
for episode in range(opts.episodes):
    # Display data
    e_start = time.time()

    # Play
    scores, moves = play(brain_name, agent, env, pbar, episode<opts.warm_up_episodes)

    # Save scores
    avg_score = np.mean(scores)
    max_score = np.max(scores)
    episode_scores.append(max_score)

    # Solve rule
    mean_target_score = np.mean(episode_scores[-opts.target_score_episodes:])
    if len(episode_scores) >= opts.target_score_episodes and mean_target_score>=opts.target_avg_score:
        print(f"Environment solved after : {episode+1} episodes.")
        print(f"Mean score: {mean_target_score:.3f} over last {opts.target_score_episodes} episodes.")
        break

    agent.save()

    # Display
    e_stop = time.time()
    seconds = e_stop-e_start
    mean_10_score = np.mean(episode_scores[-10:])
    pbar.set_description(f"E{episode+1}/{opts.episodes} M{opts.target_score_episodes}:{mean_target_score:.4f} M10:{mean_10_score:.4f} LOSS:{agent.aloss:.3f}/{agent.closs:.3f}")

# Finish
env.close()

# Save training plot
save_plot_results(opts.approach_title, episode_scores, opts.target_score_episodes, opts.target_avg_score)