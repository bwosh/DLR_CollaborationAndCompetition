import numpy as np
from tqdm import tqdm

def play_episodes(opts, env, agent):
    scores = []
    mean_score = ""
    progress = tqdm(range(opts.n_episodes))
    for episode in progress:
        progress.set_description(f"{episode+1}/{opts.n_episodes} {mean_score}")
        score = play_episode(opts, env, agent)
        scores.append(score)
        mean_score=f"{np.mean(scores):.3f}"
    return scores

def play_episode(opts, env, agent):
    env.reset()
    move = 0
    score = 0
    while not env.is_done():
        state = env.get_state()
        action = agent.act(state)

        reward, done, next_state = env.step(action)

        agent.step(state, action, reward, next_state, done)

        score += reward
        move+= 1
        if move> opts.safe_max_moves:
            break

    return score