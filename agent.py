from game import TicTacToe, PLAYER_X, PLAYER_O, EMPTY


class RandomAgent:
    def __init__(self, player=None):
        self.player = player
    
    def get_move(self,game):
        import random
        return random.choice(game.get_available_moves())

class HeuristicAgent:
    def __init__(self, player=None):
        self.player = player
        self.opponent_mark = PLAYER_O if self.player == PLAYER_X else PLAYER_X

    def get_move(self,game):
        for move in game.get_available_moves():
            game.make_move(move)
            won = (game.check_winner()==self.player)
            game.undo_move(move)
            if won:
                return move
        for move in game.get_available_moves():
                game.board[move] = self.opponent_mark
                won = (game.check_winner()==self.opponent_mark)
                if won:
                    game.board[move] = EMPTY
                    return move

class MinimaxAgent:
    def __init__(self, player=PLAYER_O,use_alpha_beta=True):
        self.player = player
        self.opponent_mark = PLAYER_O if self.player == PLAYER_X else PLAYER_X
        self.alpha_beta = use_alpha_beta

    def get_move(self,game):
        best_score = float('-inf')
        best_move = None
        for move in game.get_available_moves():
            game.make_move(move)
            score = self.minimax(game, 0, False)
            game.undo_move(move)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def minimax(self, game, depth, maximizing):
        winner = game.check_winner()
        if winner == self.player:
            return 10 - depth
        elif winner == self.opponent_mark:
            return depth - 10
        elif not game.get_available_moves():
            return 0

        if maximizing:
            best_score = float('-inf')
            for move in game.get_available_moves():
                game.make_move(move)
                score = self.minimax(game, depth + 1, False)
                game.undo_move(move)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for move in game.get_available_moves():
                game.make_move(move)
                score = self.minimax(game, depth + 1, True)
                game.undo_move(move)
                best_score = min(best_score, score)
            return best_score

def simulate_match(agent1,agent2, num_games=50):
    results = {'agent1_wins': 0, 'agent2_wins': 0, 'draws': 0}
    for _ in range(num_games):
        game = TicTacToe()
        current_agent = agent1 if game.current_player == agent1.player else agent2
        while True:
            move = current_agent.get_move(game)
            game.make_move(move)
            winner = game.check_winner()
            if winner==agent1.player:
                results['agent1_wins'] += 1
                break
            elif winner==agent2.player:
                results['agent2_wins'] += 1
                break    
            elif not game.get_available_moves():
                results['draws'] += 1
                break
            current_agent = agent1 if current_agent == agent2 else agent2
    return results

