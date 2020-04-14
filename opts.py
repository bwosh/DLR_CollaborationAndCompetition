class Opts:
    def __init__(self):
        self.target_episodes = 100
        self.target_mean_score = 0.5
        
        # Solving env params
        self.n_episodes = 100
        self.safe_max_moves = 15 # TicTacToe

        self.make_plot = False
