import numpy as np

class MctsNode:
    def __init__(self, opts):
        self.opts = opts
        self.N = 0
        self.subnodes = {} 
        self.V = 0 
        self.U = 0 
        self.state = None
        self.terminal = False

    def update_U(self, N_total):
        self.U =  self.V + np.sqrt(N_total)/(1+self.N)

    def generate_subnodes(self, env, action_shape):
        for i in range(action_shape):
            env_copy = env.copy()
            valid, reward, done, _ = env.step(i)
            if valid:
                node = MctsNode(self.opts)
                self.subnodes[i] = node
                node.V = reward
                node.terminal = done

    def play_random_game(self, env, action_shape):
        score = 0
        done = False

        first_action = None

        while not done:
            # Get valid moves
            valid_moves = []
            for i in range(action_shape):
                env_copy = env.copy()
                valid, _, _, _ = env_copy.step(i)
                if valid:
                    valid_moves.append(i)

            # perform random action
            env = env.copy()
            print("Score", score)
            print("state", env.get_state())
            action = valid_moves[np.random.randint(0, len(valid_moves))]
            print("action", action)
            if first_action is None:
                first_action = action
            valid, reward, done, _  = env.step(action)
            score += reward

            if done:
                return first_action, score

    def search(self, env, player_val, action_shape, policy, visits, parent_node = None, indent=0):
        indent_text = "".join(" "*indent)
        if self.state is None:
            self.state = env.get_state()
            self.generate_subnodes(env.copy(), action_shape)

        while self.N < visits:
            if self.N == 0:
                print(f"{indent_text}{self.state} - *Explore")
                action, self.V = self.play_random_game(env.copy(), action_shape)
                print(f"{indent_text}{self.state} - Explore value={self.V}")
                self.N += 1
                # Update U values
                for sn in self.subnodes:
                    self.subnodes[sn].update_U(self.N)
            else:
                # Select the most promising node
                u_max = -np.inf
                u_max_key = None
                for sn in self.subnodes:
                    if self.subnodes[sn].U > u_max:
                        u_max = self.subnodes[sn].U 
                        u_max_key = sn
                print(f"{indent_text}{self.state} - Entering subnode: {u_max_key}")

                if u_max_key is None:
                    pass
                    # TODO no more moves
                    print(f"{indent_text}{self.state} - NO MOVES!")
                    exit(0)
                else:
                    # There are moves
                    best_action = u_max_key
                    best_node = self.subnodes[u_max_key]
                    best_node_target_N = best_node.N + 1

                    env_copy = env.copy()
                    valid, reward, done, _ = env_copy.step(best_action)

                    print(f"{indent_text}{self.state} - *Subnode action:{best_action}")
                    best_node.search(env_copy, player_val, action_shape, policy, best_node_target_N, self, indent=indent+1)

                    sub_sum = 0
                    sub_n = 0
                    
                    for sn in self.subnodes:
                        sub_sum += self.subnodes[sn].V
                        sub_n += self.subnodes[sn].N
                    self.N += 1

                    self.V = self.opts.second_actor_reward_factor * sub_sum / sub_n
                    
        if parent_node is None:
            print("N",self.N)
            print("V",self.V)
            print("U",self.U)

            for sn in self.subnodes:
                n = self.subnodes[sn]
                print(f"{sn}: N:{n.N} V:{n.V} U:{n.U}")
            exit(0)




                

        # TODO
        action = None
        new_node = self
        return self.state, action, new_node
