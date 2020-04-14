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

    def is_action_valid(self, action):
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

    def is_action_valid(self, action):
        return self.state[action] == 0

    def get_reward(self, player):

        win_positions = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]

        for p in win_positions:
            sample = self.state[p[0]]
            all_equal = True
            for idx in p:
                if self.state[idx]!=sample:
                    all_equal = False
            if all_equal:
                if sample == player:
                    return 1.0
                else:
                    return -1.0
        return 0.0



    def step(self, action):
        if not self.is_action_valid(action):
            if self.opts.throw_on_ivalid_action:
                raise Exception("Invalid move")
            else:
                return False, self.opts.invalid_action_score, 0, self.get_state()

        # Player 1 or -1
        player_to_move = (np.sum(self.state==0))%2
        player_to_move = (1 - player_to_move-0.5)*2

        self.state[action] = player_to_move
        reward = self.get_reward(player_to_move)
        done = self.is_done()
        next_state = self.get_state()

        return True, reward, done, next_state