import numpy as np

from search import MctsNode

class Agent:
    def __init__(self, opts, state_shape, action_shape):
        self.opts = opts 
        self.state_shape = state_shape
        self.action_shape = action_shape
        self.mcts_node = MctsNode(opts)

    def step(self, state, action, reward, next_state, done):
        # TODO
        pass

    def policy(self, action):
        # TODO
        return np.random.choice(np.arange(0, self.action_shape) )

    def act(self, env, agent_index):
        player_val = (agent_index-0.5)*2.
        state, action, new_node = self.mcts_node.search( 
            env, player_val, self.action_shape, self.policy, 
            self.opts.mcts_visits)
        
        self.mcts_node = new_node
        return state, action
 
class AgentWrapper:
    def __init__(self, agent, factor):
        self.agent = agent
        self.factor = factor

    def step(self, state, action, reward, next_state, done):
        if reward>=-1 and reward<=1:
            reward = self.factor * reward
        self.agent.step(state, action, reward, next_state, done)

    def act(self, state):
        return self.agent.act(state)