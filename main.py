from agent import Agent, AgentWrapper
from env import TicTacToe
from opts import Opts
from play import play_episodes
from plot import save_plot_results

opts = Opts()
env = TicTacToe(opts)

agent = Agent(opts, env.get_state_shape(), env.get_action_shape())
agent_neg = AgentWrapper(agent, opts.second_actor_reward_factor)
agents = [agent, agent_neg] 

print("=========================")
scores = play_episodes(opts, env, agents)

if opts.make_plot:
    for agent_idx in range(len(agents)):
        save_plot_results(f"temp{agent_idx}", scores[agent_idx], 
            opts.target_episodes, opts.target_mean_score)
