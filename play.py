import numpy as np
from tqdm import tqdm

def play_episodes(opts, env, agents):
    scores = []
    mean_score = ""
    progress = tqdm(range(opts.n_episodes))
    for episode in progress:
        progress.set_description(f"{episode+1}/{opts.n_episodes} {mean_score}")
        score = play_episode(opts, env, agents)
        scores.append(score)
        mean_score=f"{np.mean(scores):.3f}"
    return scores

def play_episode(opts, env, agents):
    env.reset()
    move = 0
    scores = np.zeros((len(agents)), dtype='float')
    agent_index = 0
    while not env.is_done():
        agent = agents[agent_index]
        state, action = agent.act(env, agent_index)
        valid, reward, done, next_state = env.step(action)

        agent.step(state, action, reward, next_state, done)
        scores[agent_index] += reward

        if valid:
            move+= 1
            agent_index =  move % len(agents)
            if move> opts.safe_max_moves:
                break

    return scores