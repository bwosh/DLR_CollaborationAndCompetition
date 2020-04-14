import numpy as np

class BaseEnvironment:
    def __init__(self, opts):
        self.opts = opts

    def reset(self):
        raise Exception("Not impmented")

    def is_done(self):
        raise Exception("Not impmented")

    def get_state(self):
        raise Exception("Not impmented")

    def get_state_shape(self):
        raise Exception("Not impmented")

    def get_action_shape(self):
        raise Exception("Not impmented")

    def step(self, action):
        raise Exception("Not impmented")

class TicTacToe(BaseEnvironment):
    def __init__(self, opts):
        super().__init__(opts)
        self.reset()  

    def reset(self):
        self.state = np.zeros((9), dtype='float')

    def get_state_shape(self):
        return 9

    def get_action_shape(self):
        return 9

    def is_done(self):
        return np.sum(self.state==0)==0

    def get_state(self):
        return self.state.copy()

    def step(self, action):
        # TODO
        reward = 0.0
        done = 0
        next_state = self.state

        return reward, done, next_state