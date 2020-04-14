from agent import Agent
from env import TicTacToe
from opts import Opts
from play import play_episodes
from plot import save_plot_results

opts = Opts()
env = TicTacToe(opts)
agent = Agent(opts, env.get_state_shape(), env.get_action_shape())

scores = play_episodes(opts, env, agent)

if opts.make_plot:
    save_plot_results("temp", scores, 
        opts.target_episodes, opts.target_mean_score)