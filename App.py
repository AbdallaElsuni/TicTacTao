import sys
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QIcon
from TicTacTaoUI import Ui_Game
from GameLogic import *

class TicTacTaoWindow(QWidget, Ui_Game):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.board = Board()
        self.player = Player.PlayerX
        self.pb_1.clicked.connect(lambda :self.button_clicked(1))
        self.pb_2.clicked.connect(lambda :self.button_clicked(2))
        self.pb_3.clicked.connect(lambda :self.button_clicked(3))
        self.pb_4.clicked.connect(lambda :self.button_clicked(4))
        self.pb_5.clicked.connect(lambda :self.button_clicked(5))
        self.pb_6.clicked.connect(lambda :self.button_clicked(6))
        self.pb_7.clicked.connect(lambda :self.button_clicked(7))
        self.pb_8.clicked.connect(lambda :self.button_clicked(8))
        self.pb_9.clicked.connect(lambda :self.button_clicked(9))
        self.pb_Reset.clicked.connect(self.restart_game)
        self.show()
    def restart_game(self):
        self.player = Player.PlayerX
        self.board.reset_blocks()
        self.clear_icons()
        self.lb_Messege.setText("")
    def clear_icons(self):
        self.pb_1.setIcon(QIcon(""))
        self.pb_2.setIcon(QIcon(""))
        self.pb_3.setIcon(QIcon(""))
        self.pb_4.setIcon(QIcon(""))
        self.pb_5.setIcon(QIcon(""))
        self.pb_6.setIcon(QIcon(""))
        self.pb_7.setIcon(QIcon(""))
        self.pb_8.setIcon(QIcon(""))
        self.pb_9.setIcon(QIcon(""))
    def switch_player(self):
        if self.player == Player.PlayerX:
            self.player = Player.PlayerO
        elif self.player == Player.PlayerO:
            self.player = Player.PlayerX
    def button_clicked(self, button_number):
        if self.board.click_if_allowed(button_number, self.player):
            player_to_block = {
                Player.PlayerX: BlockState.X,
                Player.PlayerO: BlockState.O
            }
            self.change_button_icon(button_number, player_to_block[self.player])
            if self.board.check_state == BoardState.Ongoing:
                self.switch_player()
            elif self.board.check_state == BoardState.XWon or self.board.check_state == BoardState.OWon:
                winning_method = self.board.the_winning_method
                if self.board.check_state == BoardState.XWon:
                    blocks_display = blocks_display_for_a_winning_method(winning_method, "X")
                    for block_number, block_display in blocks_display.items():
                        self.change_button_icon(block_number, BlockState[block_display])
                    self.lb_Messege.setText("X Won!")
                elif self.board.check_state == BoardState.OWon:
                    blocks_display = blocks_display_for_a_winning_method(winning_method, "O")
                    for block_number, block_display in blocks_display.items():
                        self.change_button_icon(block_number, BlockState[block_display])
                        self.lb_Messege.setText("O Won!")
    def change_button_icon(self, button_number, change_to):
        block_state_to_png = {
            BlockState.Neutral: "",
            BlockState.X: "GreenX.png",
            BlockState.O: "GreenO.png",
            BlockState.XDiagonalL: "GreenX_Diagonal_L.png",
            BlockState.XDiagonalR: "GreenX_Diagonal_R.png",
            BlockState.ODiagonalL: "GreenO_Diagonal_L.png",
            BlockState.ODiagonalR: "GreenO_Diagonal_R.png",
            BlockState.XVertical: "GreenX_Vertical.png",
            BlockState.XHorizontal: "GreenX_Horizontal.png",
            BlockState.OVertical: "GreenO_Vertical.png",
            BlockState.OHorizontal: "GreenO_Horizontal.png",
        }
        change_to = block_state_to_png[change_to]
        button_name = f"pb_{button_number}"
        button = getattr(self, button_name)
        button.setIcon(QIcon(f":/Buttons/{change_to}"))
application = QApplication(sys.argv)

window = TicTacTaoWindow()

application.exec()