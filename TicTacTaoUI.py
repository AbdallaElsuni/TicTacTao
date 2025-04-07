# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TicTacTaoUI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QWidget)
import Icons.TicTacTao_Icons_rc

class Ui_Game(object):
    def setupUi(self, Game):
        if not Game.objectName():
            Game.setObjectName(u"Game")
        Game.resize(350, 390)
        self.gridLayout = QGridLayout(Game)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_Messege = QLabel(Game)
        self.lb_Messege.setObjectName(u"lb_Messege")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lb_Messege.setFont(font)

        self.gridLayout.addWidget(self.lb_Messege, 1, 0, 1, 1)

        self.pb_Reset = QPushButton(Game)
        self.pb_Reset.setObjectName(u"pb_Reset")
        self.pb_Reset.setFont(font)

        self.gridLayout.addWidget(self.pb_Reset, 1, 1, 1, 1)

        self.groupBox = QGroupBox(Game)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_4 = QPushButton(self.groupBox)
        self.pb_4.setObjectName(u"pb_4")
        self.pb_4.setMinimumSize(QSize(100, 100))
        self.pb_4.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.pb_4, 1, 0, 1, 1)

        self.pb_6 = QPushButton(self.groupBox)
        self.pb_6.setObjectName(u"pb_6")
        self.pb_6.setMinimumSize(QSize(100, 100))
        self.pb_6.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.pb_6, 1, 2, 1, 1)

        self.pb_2 = QPushButton(self.groupBox)
        self.pb_2.setObjectName(u"pb_2")
        self.pb_2.setMinimumSize(QSize(100, 100))
        self.pb_2.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.pb_2, 0, 1, 1, 1)

        self.pb_3 = QPushButton(self.groupBox)
        self.pb_3.setObjectName(u"pb_3")
        self.pb_3.setMinimumSize(QSize(100, 100))
        self.pb_3.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.pb_3, 0, 2, 1, 1)

        self.pb_5 = QPushButton(self.groupBox)
        self.pb_5.setObjectName(u"pb_5")
        self.pb_5.setMinimumSize(QSize(100, 100))
        self.pb_5.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.pb_5, 1, 1, 1, 1)

        self.pb_1 = QPushButton(self.groupBox)
        self.pb_1.setObjectName(u"pb_1")
        self.pb_1.setMinimumSize(QSize(100, 100))
        self.pb_1.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.pb_1, 0, 0, 1, 1)

        self.pb_7 = QPushButton(self.groupBox)
        self.pb_7.setObjectName(u"pb_7")
        self.pb_7.setMinimumSize(QSize(100, 100))
        self.pb_7.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.pb_7, 2, 0, 1, 1)

        self.pb_8 = QPushButton(self.groupBox)
        self.pb_8.setObjectName(u"pb_8")
        self.pb_8.setMinimumSize(QSize(100, 100))
        self.pb_8.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.pb_8, 2, 1, 1, 1)

        self.pb_9 = QPushButton(self.groupBox)
        self.pb_9.setObjectName(u"pb_9")
        self.pb_9.setMinimumSize(QSize(100, 100))
        self.pb_9.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.pb_9, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)


        self.retranslateUi(Game)

        QMetaObject.connectSlotsByName(Game)
    # setupUi

    def retranslateUi(self, Game):
        Game.setWindowTitle(QCoreApplication.translate("Game", u"TicTacTao", None))
        self.lb_Messege.setText("")
        self.pb_Reset.setText(QCoreApplication.translate("Game", u"Reset", None))
        self.groupBox.setTitle("")
        self.pb_4.setText("")
        self.pb_6.setText("")
        self.pb_2.setText("")
        self.pb_3.setText("")
        self.pb_5.setText("")
        self.pb_1.setText("")
        self.pb_7.setText("")
        self.pb_8.setText("")
        self.pb_9.setText("")
    # retranslateUi

