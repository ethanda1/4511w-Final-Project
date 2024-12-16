from tkinter import Frame, Label, CENTER
import random
import logic
import constants as c
from expectimax import ExpectimaxValue, expectimax, Node, MAX_NODE
from heuristics import highest_score_heuristic, fewest_filled_tiles, moveTilesDown, numberOfTilesInSameLocation, highTilesAlongSingleEdge

def gen():
    return random.randint(0, c.GRID_LEN - 1)

class GameGrid(Frame):
    def __init__(self, heuristic=None, depth_limit=2, time_between_moves=0):
        Frame.__init__(self)

        # For expectimax
        self.heuristic = heuristic
        self.depth_limit = depth_limit
        
        self.grid()
        self.master.title('2048')
        
        # Needed for user input if we want it back
        # self.master.bind("<Key>", self.key_down)
        self.game_score = 0
        self.commands = {
            c.KEY_UP: logic.up,
            c.KEY_DOWN: logic.down,
            c.KEY_LEFT: logic.left,
            c.KEY_RIGHT: logic.right,
            c.KEY_UP_ALT1: logic.up,
            c.KEY_DOWN_ALT1: logic.down,
            c.KEY_LEFT_ALT1: logic.left,
            c.KEY_RIGHT_ALT1: logic.right,
            c.KEY_UP_ALT2: logic.up,
            c.KEY_DOWN_ALT2: logic.down,
            c.KEY_LEFT_ALT2: logic.left,
            c.KEY_RIGHT_ALT2: logic.right,
        }

        self.time_between_moves = time_between_moves        # measured in ms
        self.grid_cells = []
        self.init_grid()
        self.matrix = logic.new_game(c.GRID_LEN)
        self.history_matrices = [self.matrix]
        self.update_grid_cells()

        self.auto_play()
        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(
                    background,
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    width=c.SIZE / c.GRID_LEN,
                    height=c.SIZE / c.GRID_LEN
                )
                cell.grid(
                    row=i,
                    column=j,
                    padx=c.GRID_PADDING,
                    pady=c.GRID_PADDING
                )
                t = Label(
                    master=cell,
                    text="",
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=c.FONT,
                    width=5,
                    height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number]
                    )
        self.update_idletasks()


    def get_heuristic_move(self):
        root_node: Node = Node(value=0, children=[], state_matrix=self.matrix, action_history=[], action=None, state_history_matrices=self.history_matrices)
        ret_val: ExpectimaxValue = expectimax(root_node, MAX_NODE, self.heuristic, 1, self.depth_limit)
        
        if (ret_val.action_history):
            return ret_val.action_history[-1]
        return None
    
    def make_heuristic_move(self):
        """Make a heuristic move and update the grid."""
        move_key = self.get_heuristic_move()
        if (not(move_key)):
            print("move key is None")
        # print(f'ACTUAL move taken: {move_key}')
        self.matrix, done = self.commands[move_key](self.matrix)
        if done:
            self.matrix = logic.add_two(self.matrix)
            # Record the last move
            self.history_matrices.append(self.matrix)
            self.update_grid_cells()
            if logic.game_state(self.matrix) == 'win':
                self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            if logic.game_state(self.matrix) == 'lose':
                self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            return logic.game_state(self.matrix)
    
    def get_random_move(self):
            """Return a random valid move from the available commands."""
            valid_moves = list(self.commands.keys())
            return random.choice(valid_moves)

    def make_random_move(self):
        """Make a random move and update the grid."""
        move_key = self.get_random_move()
        self.matrix, done = self.commands[move_key](self.matrix)
        if done:
            self.matrix = logic.add_two(self.matrix)
            # Record the last move
            self.history_matrices.append(self.matrix)
            self.update_grid_cells()
            if logic.game_state(self.matrix) == 'win':
                self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

            if logic.game_state(self.matrix) == 'lose':
                self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def close_game(self):
        # print("Closing game.")
        self.master.quit()
        self.master.destroy()

    def auto_play(self):
        """Automatically make a move every 1 second."""
        if (not(self.make_heuristic_move() == "not over")):
            self.game_score = logic.calc_game_score(self.matrix)
            self.close_game()
            return
        self.after(self.time_between_moves, self.auto_play)  
        
    # User input can be added back if needed
    def key_down(self, event):
        key = event.keysym
        print(event)
        if key == c.KEY_QUIT: exit()
        if key == c.KEY_BACK and len(self.history_matrices) > 1:
            self.matrix = self.history_matrices.pop()
            self.update_grid_cells()
            print('back on step total step:', len(self.history_matrices))
        elif key in self.commands:
            self.matrix, done = self.commands[key](self.matrix)
            if done:
                self.matrix = logic.add_two(self.matrix)
                # record last move
                self.history_matrices.append(self.matrix)
                self.update_grid_cells()
                if logic.game_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.game_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def generate_next(self):
        index = (gen(), gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (gen(), gen())
        self.matrix[index[0]][index[1]] = 2



if __name__ == "__main__":
    game_grid = GameGrid(highTilesAlongSingleEdge, time_between_moves=0)
    print(game_grid.game_score)
