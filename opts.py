class Opts:
    def __init__(self):
        # Environment solving params
        self.target_episodes = 100
        self.target_mean_score = 0.5
        self.n_episodes = 100
        
        # Solving env params - TictacToe
        self.safe_max_moves = 15 
        self.safe_max_move_attempts = 100
        self.throw_on_ivalid_action = False
        self.invalid_action_score = -10
        self.second_actor_reward_factor = -1

        # Summary
        self.make_plot = False
