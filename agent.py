import numpy as np

class Agent:
    def __init__(self, opts, state_shape, action_shape):
        self.opts = opts 
        self.state_shape = state_shape
        self.action_shape = action_shape

    def step(self, state, action, reward, next_state, done):
        # TODO
        pass

    def act(self, state):
        # TODO
        return np.random.choice(np.arange(0,self.action_shape) )

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