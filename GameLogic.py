__all__ = ["Block", "BlockState", "Board", "BoardState", "WiningPossibilities", "Player", "blocks_display_for_a_winning_method"]
from enum import Enum, auto
class CustomEnum(Enum):
    def __str__(self):
        return self.name
class BlockState(CustomEnum):
    Neutral = auto()
    X = auto()
    O = auto()
    XDiagonalR = auto()
    XDiagonalL = auto()
    ODiagonalR = auto()
    ODiagonalL = auto()
    XHorizontal = auto()
    XVertical = auto()
    OHorizontal = auto()
    OVertical = auto()
class BoardState(CustomEnum):
    Ongoing = auto()
    XWon = auto()
    OWon = auto()
class Player(CustomEnum):
    PlayerX = auto()
    PlayerO = auto()
class WiningPossibilities(CustomEnum):
    DiagonalLeft = auto()
    DiagonalRight = auto()
    TopRow = auto()
    MiddleRow = auto()
    BottomRow = auto()
    LeftColumn = auto()
    MiddleColumn = auto()
    RightColumn = auto()
class Block:
    def __init__(self):
        self.state = BlockState.Neutral

class Board:
    def __init__(self):
        self.state = BoardState.Ongoing
        self.wining_method = None
        self.block1 = Block()
        self.block2 = Block()
        self.block3 = Block()
        self.block4 = Block()
        self.block5 = Block()
        self.block6 = Block()
        self.block7 = Block()
        self.block8 = Block()
        self.block9 = Block()
        self.wining_possibilities = {
            WiningPossibilities.DiagonalLeft: [self.block1, self.block5, self.block9],
            WiningPossibilities.DiagonalRight: [self.block3, self.block5, self.block7],
            WiningPossibilities.LeftColumn: [self.block1, self.block4, self.block7],
            WiningPossibilities.MiddleColumn: [self.block2, self.block5, self.block8],
            WiningPossibilities.RightColumn: [self.block3, self.block6, self.block9],
            WiningPossibilities.TopRow: [self.block1, self.block2, self.block3],
            WiningPossibilities.MiddleRow: [self.block4, self.block5, self.block6],
            WiningPossibilities.BottomRow: [self.block7, self.block8, self.block9]
        }
    def reset_board(self):
        self.state = BoardState.Ongoing
        self.wining_method = None
        self.reset_blocks()
    def reset_blocks(self):
        self.block1.state = BlockState.Neutral
        self.block2.state = BlockState.Neutral
        self.block3.state = BlockState.Neutral
        self.block4.state = BlockState.Neutral
        self.block5.state = BlockState.Neutral
        self.block6.state = BlockState.Neutral
        self.block7.state = BlockState.Neutral
        self.block8.state = BlockState.Neutral
        self.block9.state = BlockState.Neutral
    def click_if_allowed(self, block_number:int, player):
        player_to_block = {
            Player.PlayerX: BlockState.X,
            Player.PlayerO: BlockState.O
        }
        reference_number_to_attribute = {
            1: "block1",
            2: "block2",
            3: "block3",
            4: "block4",
            5: "block5",
            6: "block6",
            7: "block7",
            8: "block8",
            9: "block9"
        }
        if self.check_state == BoardState.Ongoing:
            block_name = reference_number_to_attribute[block_number]
            block_state = getattr(getattr(self, block_name), "state")
            if block_state == BlockState.Neutral:
                state_to_set = player_to_block[player]
                setattr(getattr(self, block_name),"state",state_to_set)
                return True
        return False
    @property
    def winner_and_winning_method(self):
        if self.state == BoardState.Ongoing:
            winner = None
            wining_method = None
            block_to_player = {
                BlockState.X: Player.PlayerX,
                BlockState.O: Player.PlayerO
            }
            for block_state in [BlockState.X, BlockState.O]:
                for wining_method_name, wining_method_blocks in self.wining_possibilities.items():
                    if all(block.state == block_state for block in wining_method_blocks):
                        wining_method = wining_method_name
                        winner = block_to_player[block_state]
            return winner, wining_method
        else:
            state_to_player = {
                BoardState.XWon: Player.PlayerX,
                BoardState.OWon: Player.PlayerO
            }
            if self.state == BoardState.Ongoing:
                return None, None
            else:
                return state_to_player[self.state], self.wining_method
    @property
    def winner(self):
        winner, _ = self.winner_and_winning_method
        return winner

    @property
    def check_state(self):
        player_to_state = {
            Player.PlayerX: BoardState.XWon,
            Player.PlayerO: BoardState.OWon
        }
        if self.winner:
            return player_to_state[self.winner]
        else:
            return BoardState.Ongoing

    @property
    def the_winning_method(self):
        _, the_winning_method = self.winner_and_winning_method
        return the_winning_method

def blocks_display_for_a_winning_method(winning_method:WiningPossibilities, player):
    wining_display = {
        WiningPossibilities.DiagonalLeft: {
            1: f"{player}DiagonalL",
            5: f"{player}DiagonalL",
            9: f"{player}DiagonalL",
        },
        WiningPossibilities.DiagonalRight: {
            3: f"{player}DiagonalR",
            5: f"{player}DiagonalR",
            7: f"{player}DiagonalR",
        },
        WiningPossibilities.LeftColumn: {
            1: f"{player}Vertical",
            4: f"{player}Vertical",
            7: f"{player}Vertical",
        },
        WiningPossibilities.MiddleColumn: {
            2: f"{player}Vertical",
            5: f"{player}Vertical",
            8: f"{player}Vertical",
        },
        WiningPossibilities.RightColumn: {
            3: f"{player}Vertical",
            6: f"{player}Vertical",
            9: f"{player}Vertical",
        },
        WiningPossibilities.TopRow: {
            1: f"{player}Horizontal",
            2: f"{player}Horizontal",
            3: f"{player}Horizontal",
        },
        WiningPossibilities.MiddleRow: {
            4: f"{player}Horizontal",
            5: f"{player}Horizontal",
            6: f"{player}Horizontal",
        },
        WiningPossibilities.BottomRow: {
            7: f"{player}Horizontal",
            8: f"{player}Horizontal",
            9: f"{player}Horizontal",
        },
    }
    return wining_display[winning_method]

if __name__ == '__main__':
    board = Board()
    print(board.click_if_allowed(1, Player.PlayerX))
    print(board.click_if_allowed(2, Player.PlayerX))
    print(board.click_if_allowed(3, Player.PlayerX))

    print(board.check_state)
    # some_blocks = [board.block1, board.block2, board.block3]
    # if all(block.state == BlockState.X for block in some_blocks):
    #     print("test")