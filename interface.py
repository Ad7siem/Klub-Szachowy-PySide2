# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1034, 573)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"	background-color: #252525;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 21px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer{\n"
"	background-color: #353535;\n"
"}\n"
"#rightMenuSubContainer{\n"
"	background-color: #4f4f4f;\n"
"	border-radius: 10px\n"
"}\n"
"#frame_4, #frame_8, #popupNotificationSubContainer{\n"
"	background-color: #0d0d0d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer, #footContainer{\n"
"	background-color: #353535;\n"
"}\n"
"\n"
"#maxPlayer,#minPlayer, #nameGame, #timeGame, #typeGame, #owner{\n"
"	background-color: rgb(94, 94, 94);\n"
"	border: 20px;\n"
"	border-radius:2px;\n"
"}\n"
"\n"
"#listAllGames, #listGames, #playersSheet, #resultsDay, #t"
                        "ableWinners, #urlBordGamesSheet, #urlStatisticSheet, #search, #dateEdit, #nameGameAdd, #numberGame, #valuePlayer, #namePlayer, #points, #position, #results{\n"
"	background-color:#303030;\n"
"	border: 1px;\n"
"	border-radius: 2px;\n"
"	border-color: #969696;\n"
"	border-style: outset;\n"
"}\n"
"\n"
"#saveGame, #saveSettings, #searchItem, #addPlayer, #nextPlayer{\n"
"	background-color: rgb(94, 94, 94);\n"
"\n"
"	border-radius: 5px;\n"
"	border-width: 1px;\n"
"	border-color: #969696;\n"
"	border-style: outset;\n"
"}\n"
"\n"
"#titleListGames, #titleResults, #titleAddResults, #frame_11, #frame_12, #frame_13{\n"
"	background-color: #969696;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.leftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 14, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/rolling-dices.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/podium-winner.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.reportsBtn = QPushButton(self.frame_2)
        self.reportsBtn.setObjectName(u"reportsBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/add-results.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reportsBtn.setIcon(icon3)
        self.reportsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.reportsBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingBtn = QPushButton(self.frame_3)
        self.settingBtn.setObjectName(u"settingBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon4)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingBtn)

        self.informationBtn = QPushButton(self.frame_3)
        self.informationBtn.setObjectName(u"informationBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.informationBtn.setIcon(icon5)
        self.informationBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.informationBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(400, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon7)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_22 = QVBoxLayout(self.widget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_2, 0, Qt.AlignTop)

        self.frame_17 = QFrame(self.widget)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_17)
        self.verticalLayout_23.setSpacing(8)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 10, 0, 0)
        self.label_23 = QLabel(self.frame_17)
        self.label_23.setObjectName(u"label_23")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_23.setFont(font1)

        self.verticalLayout_23.addWidget(self.label_23, 0, Qt.AlignTop)

        self.urlStatisticSheet = QLineEdit(self.frame_17)
        self.urlStatisticSheet.setObjectName(u"urlStatisticSheet")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.urlStatisticSheet.sizePolicy().hasHeightForWidth())
        self.urlStatisticSheet.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(10)
        self.urlStatisticSheet.setFont(font2)

        self.verticalLayout_23.addWidget(self.urlStatisticSheet, 0, Qt.AlignTop)

        self.label_24 = QLabel(self.frame_17)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.verticalLayout_23.addWidget(self.label_24, 0, Qt.AlignTop)

        self.urlBordGamesSheet = QLineEdit(self.frame_17)
        self.urlBordGamesSheet.setObjectName(u"urlBordGamesSheet")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.urlBordGamesSheet.sizePolicy().hasHeightForWidth())
        self.urlBordGamesSheet.setSizePolicy(sizePolicy3)
        self.urlBordGamesSheet.setFont(font2)

        self.verticalLayout_23.addWidget(self.urlBordGamesSheet, 0, Qt.AlignTop)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.label_25 = QLabel(self.frame_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_25)

        self.playersSheet = QLineEdit(self.frame_17)
        self.playersSheet.setObjectName(u"playersSheet")
        self.playersSheet.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.playersSheet)

        self.label_26 = QLabel(self.frame_17)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_26)

        self.listAllGames = QLineEdit(self.frame_17)
        self.listAllGames.setObjectName(u"listAllGames")
        self.listAllGames.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.listAllGames)

        self.label_27 = QLabel(self.frame_17)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_27)

        self.resultsDay = QLineEdit(self.frame_17)
        self.resultsDay.setObjectName(u"resultsDay")
        self.resultsDay.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.resultsDay)

        self.label_28 = QLabel(self.frame_17)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_28)

        self.listGames = QLineEdit(self.frame_17)
        self.listGames.setObjectName(u"listGames")
        self.listGames.setFont(font2)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.listGames)

        self.label_29 = QLabel(self.frame_17)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_29)

        self.tableWinners = QLineEdit(self.frame_17)
        self.tableWinners.setObjectName(u"tableWinners")
        self.tableWinners.setFont(font2)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.tableWinners)


        self.verticalLayout_23.addLayout(self.formLayout_2)


        self.verticalLayout_22.addWidget(self.frame_17)

        self.saveSettings = QPushButton(self.widget)
        self.saveSettings.setObjectName(u"saveSettings")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.saveSettings.setFont(font3)

        self.verticalLayout_22.addWidget(self.saveSettings)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_2)


        self.verticalLayout_7.addWidget(self.widget)

        self.centerMenuPages.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setPointSize(13)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy4)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777212))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 30))
        self.label_5.setPixmap(QPixmap(u":/images/Logo klub.ico"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_6.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon8)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon9)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileManuBtn = QPushButton(self.frame_6)
        self.profileManuBtn.setObjectName(u"profileManuBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/add-game.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileManuBtn.setIcon(icon10)
        self.profileManuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileManuBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.mainBodyContent.setMinimumSize(QSize(584, 397))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_14 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.horizontalLayout_16 = QHBoxLayout(self.page_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_16 = QFrame(self.page_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 0))
        self.label_22.setMaximumSize(QSize(500, 150))
        self.label_22.setPixmap(QPixmap(u":/images/Logo klub.png"))
        self.label_22.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_22)


        self.horizontalLayout_16.addWidget(self.frame_16)

        self.mainPages.addWidget(self.page_9)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_15 = QVBoxLayout(self.page_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.titleListGames = QFrame(self.page_6)
        self.titleListGames.setObjectName(u"titleListGames")
        self.titleListGames.setFrameShape(QFrame.StyledPanel)
        self.titleListGames.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.titleListGames)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_10 = QLabel(self.titleListGames)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_10)

        self.searchBtn = QPushButton(self.titleListGames)
        self.searchBtn.setObjectName(u"searchBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon14)
        self.searchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.searchBtn, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.titleListGames)

        self.frame_12 = QFrame(self.page_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_12)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gameTablet = QTableWidget(self.frame_12)
        if (self.gameTablet.columnCount() < 6):
            self.gameTablet.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.gameTablet.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.gameTablet.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.gameTablet.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.gameTablet.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.gameTablet.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.gameTablet.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.gameTablet.setObjectName(u"gameTablet")
        self.gameTablet.setMinimumSize(QSize(725, 0))
        self.gameTablet.setMaximumSize(QSize(725, 16777215))
        self.gameTablet.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.gameTablet.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.gameTablet.setAlternatingRowColors(True)
        self.gameTablet.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.gameTablet.setRowCount(0)

        self.verticalLayout_20.addWidget(self.gameTablet, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_12)

        self.mainPages.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setMinimumSize(QSize(0, 0))
        self.page_7.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.page_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.titleResults = QLabel(self.page_7)
        self.titleResults.setObjectName(u"titleResults")
        self.titleResults.setMinimumSize(QSize(700, 0))
        self.titleResults.setFont(font)
        self.titleResults.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.titleResults, 0, Qt.AlignTop)

        self.frame_11 = QFrame(self.page_7)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setMinimumSize(QSize(700, 0))
        self.frame_11.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.winnerTable = QTableWidget(self.frame_11)
        if (self.winnerTable.columnCount() < 3):
            self.winnerTable.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.winnerTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.winnerTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.winnerTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.winnerTable.setObjectName(u"winnerTable")
        self.winnerTable.setMinimumSize(QSize(340, 0))
        self.winnerTable.setMaximumSize(QSize(340, 16777215))
        self.winnerTable.setAlternatingRowColors(True)
        self.winnerTable.setRowCount(0)

        self.horizontalLayout_14.addWidget(self.winnerTable, 0, Qt.AlignRight)

        self.goldPlateTable = QTableWidget(self.frame_11)
        if (self.goldPlateTable.columnCount() < 3):
            self.goldPlateTable.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.goldPlateTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.goldPlateTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.goldPlateTable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        self.goldPlateTable.setObjectName(u"goldPlateTable")
        self.goldPlateTable.setMinimumSize(QSize(340, 0))
        self.goldPlateTable.setMaximumSize(QSize(340, 16777215))
        self.goldPlateTable.setAlternatingRowColors(True)
        self.goldPlateTable.setRowCount(0)

        self.horizontalLayout_14.addWidget(self.goldPlateTable, 0, Qt.AlignLeft)


        self.verticalLayout_16.addWidget(self.frame_11)

        self.mainPages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_17 = QVBoxLayout(self.page_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.titleAddResults = QLabel(self.page_8)
        self.titleAddResults.setObjectName(u"titleAddResults")
        self.titleAddResults.setFont(font)
        self.titleAddResults.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.titleAddResults, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.page_8)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_13)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 10)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(6)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_33 = QLabel(self.frame_13)
        self.label_33.setObjectName(u"label_33")
        font6 = QFont()
        font6.setPointSize(14)
        self.label_33.setFont(font6)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_33)

        self.dateEdit = QDateEdit(self.frame_13)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font6)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.dateEdit)

        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font6)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_30)

        self.valuePlayer = QLineEdit(self.frame_13)
        self.valuePlayer.setObjectName(u"valuePlayer")
        self.valuePlayer.setFont(font6)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.valuePlayer)

        self.label_32 = QLabel(self.frame_13)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font6)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_32)

        self.nameGameAdd = QComboBox(self.frame_13)
        self.nameGameAdd.setObjectName(u"nameGameAdd")
        self.nameGameAdd.setFont(font6)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.nameGameAdd)

        self.label_31 = QLabel(self.frame_13)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font6)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_31)

        self.numberGame = QLineEdit(self.frame_13)
        self.numberGame.setObjectName(u"numberGame")
        self.numberGame.setFont(font6)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.numberGame)


        self.verticalLayout_28.addLayout(self.formLayout_3)

        self.addPlayer = QPushButton(self.frame_13)
        self.addPlayer.setObjectName(u"addPlayer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.addPlayer.sizePolicy().hasHeightForWidth())
        self.addPlayer.setSizePolicy(sizePolicy5)
        self.addPlayer.setMinimumSize(QSize(200, 0))
        self.addPlayer.setFont(font3)

        self.verticalLayout_28.addWidget(self.addPlayer, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_4)


        self.verticalLayout_17.addWidget(self.frame_13)

        self.mainPages.addWidget(self.page_8)

        self.verticalLayout_14.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(200, 379))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 10)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightBtn = QPushButton(self.frame_8)
        self.closeRightBtn.setObjectName(u"closeRightBtn")
        self.closeRightBtn.setIcon(icon7)
        self.closeRightBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_26 = QVBoxLayout(self.page_11)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_18 = QFrame(self.page_11)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_18)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 10)
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.position = QLineEdit(self.frame_18)
        self.position.setObjectName(u"position")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.position)

        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.namePlayer = QComboBox(self.frame_18)
        self.namePlayer.setObjectName(u"namePlayer")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.namePlayer)

        self.label_34 = QLabel(self.frame_18)
        self.label_34.setObjectName(u"label_34")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_34)

        self.points = QLineEdit(self.frame_18)
        self.points.setObjectName(u"points")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.points)

        self.label_35 = QLabel(self.frame_18)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_35)

        self.results = QComboBox(self.frame_18)
        self.results.setObjectName(u"results")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.results)


        self.verticalLayout_27.addLayout(self.formLayout_4)

        self.nextPlayer = QPushButton(self.frame_18)
        self.nextPlayer.setObjectName(u"nextPlayer")
        self.nextPlayer.setFont(font3)

        self.verticalLayout_27.addWidget(self.nextPlayer)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_5)


        self.verticalLayout_26.addWidget(self.frame_18)

        self.rightMenuPages.addWidget(self.page_11)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.horizontalLayout_19 = QHBoxLayout(self.page_10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_19 = QFrame(self.page_10)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_19)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_13 = QLabel(self.frame_19)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_13, 0, Qt.AlignTop)

        self.search = QLineEdit(self.frame_19)
        self.search.setObjectName(u"search")

        self.verticalLayout_24.addWidget(self.search)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_20)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.radioButton = QRadioButton(self.frame_20)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_25.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_20)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_25.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.frame_20)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_25.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.frame_20)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_25.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.frame_20)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_25.addWidget(self.radioButton_5)


        self.verticalLayout_24.addWidget(self.frame_20, 0, Qt.AlignHCenter)

        self.searchItem = QPushButton(self.frame_19)
        self.searchItem.setObjectName(u"searchItem")
        self.searchItem.setFont(font6)

        self.verticalLayout_24.addWidget(self.searchItem)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_3)


        self.horizontalLayout_19.addWidget(self.frame_19)

        self.rightMenuPages.addWidget(self.page_10)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_21 = QVBoxLayout(self.page_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_8)

        self.frame_14 = QFrame(self.page_4)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setMaximumSize(QSize(16777215, 170))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(-1, 10, -1, 0)
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.nameGame = QLineEdit(self.frame_14)
        self.nameGame.setObjectName(u"nameGame")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameGame)

        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_18)

        self.minPlayer = QLineEdit(self.frame_14)
        self.minPlayer.setObjectName(u"minPlayer")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.minPlayer)

        self.label_19 = QLabel(self.frame_14)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_19)

        self.maxPlayer = QLineEdit(self.frame_14)
        self.maxPlayer.setObjectName(u"maxPlayer")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.maxPlayer)

        self.label_20 = QLabel(self.frame_14)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_20)

        self.timeGame = QLineEdit(self.frame_14)
        self.timeGame.setObjectName(u"timeGame")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.timeGame)

        self.label_21 = QLabel(self.frame_14)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_21)

        self.owner = QLineEdit(self.frame_14)
        self.owner.setObjectName(u"owner")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.owner)

        self.typeGame = QComboBox(self.frame_14)
        self.typeGame.setObjectName(u"typeGame")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.typeGame)


        self.horizontalLayout_10.addLayout(self.formLayout)


        self.verticalLayout_21.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.page_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.saveGame = QPushButton(self.frame_15)
        self.saveGame.setObjectName(u"saveGame")
        self.saveGame.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.saveGame.sizePolicy().hasHeightForWidth())
        self.saveGame.setSizePolicy(sizePolicy2)
        self.saveGame.setMinimumSize(QSize(80, 0))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(94, 94, 94, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.saveGame.setPalette(palette)
        self.saveGame.setFont(font3)

        self.horizontalLayout_15.addWidget(self.saveGame, 0, Qt.AlignTop)


        self.verticalLayout_21.addWidget(self.frame_15)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_13 = QVBoxLayout(self.page_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_9)

        self.rightMenuPages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_18 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_14 = QLabel(self.popupNotificationSubContainer)
        self.label_14.setObjectName(u"label_14")
        font7 = QFont()
        font7.setBold(True)
        font7.setWeight(75)
        self.label_14.setFont(font7)

        self.verticalLayout_19.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.infoNotification = QLabel(self.frame_9)
        self.infoNotification.setObjectName(u"infoNotification")
        sizePolicy4.setHeightForWidth(self.infoNotification.sizePolicy().hasHeightForWidth())
        self.infoNotification.setSizePolicy(sizePolicy4)
        self.infoNotification.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.infoNotification)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon15)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_9)


        self.verticalLayout_18.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)

        self.footContainer = QWidget(self.mainBodyContainer)
        self.footContainer.setObjectName(u"footContainer")
        self.horizontalLayout_12 = QHBoxLayout(self.footContainer)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)


        self.horizontalLayout_12.addWidget(self.frame_10)

        self.sizeGrip = QPushButton(self.footContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        sizePolicy.setHeightForWidth(self.sizeGrip.sizePolicy().hasHeightForWidth())
        self.sizeGrip.setSizePolicy(sizePolicy)
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/arrow-down-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sizeGrip.setIcon(icon16)

        self.horizontalLayout_12.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.footContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Plansz\u00f3wki", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u" Plansz\u00f3wki", None))
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Wyniki", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u" Wyniki", None))
#if QT_CONFIG(tooltip)
        self.reportsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Dodaj Wynik", None))
#endif // QT_CONFIG(tooltip)
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"  Dodaj Wynik", None))
#if QT_CONFIG(tooltip)
        self.settingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u" Ustawienia", None))
#if QT_CONFIG(tooltip)
        self.informationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Informacje", None))
#endif // QT_CONFIG(tooltip)
        self.informationBtn.setText(QCoreApplication.translate("MainWindow", u" Informacje", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Pomoc", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u" Pomoc", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Link do arkusza statystyk:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Link do arkusza z plansz\u00f3wkami:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Podaj nazw\u0119 arkusza z graczami:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Podaj nazw\u0119 arkusza z list\u0105 wszystkich gier:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Podaj nazw\u0119 arkusza z wynikami dnia:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Podaj nazw\u0119 arkusza z list\u0105 plansz\u00f3wek:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Podaj nazw\u0119 arkusza z wynikiem og\u00f3lnym:", None))
        self.saveSettings.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Klub Szachowy", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileManuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Dodaj Gr\u0119", None))
#endif // QT_CONFIG(tooltip)
        self.profileManuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_22.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"          Lista Gier Planszowych", None))
        self.searchBtn.setText("")
        ___qtablewidgetitem = self.gameTablet.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nazwa Gry", None));
        ___qtablewidgetitem1 = self.gameTablet.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Typ Gry", None));
        ___qtablewidgetitem2 = self.gameTablet.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Min. ilo\u015b\u0107 graczy", None));
        ___qtablewidgetitem3 = self.gameTablet.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Max. ilo\u015b\u0107 graczy", None));
        ___qtablewidgetitem4 = self.gameTablet.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Czas Gry", None));
        ___qtablewidgetitem5 = self.gameTablet.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"W\u0142a\u015bciciel", None));
        self.titleResults.setText(QCoreApplication.translate("MainWindow", u"Wyniki", None))
        ___qtablewidgetitem6 = self.winnerTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Pozycja", None));
        ___qtablewidgetitem7 = self.winnerTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Osoba", None));
        ___qtablewidgetitem8 = self.winnerTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Punkty", None));
        ___qtablewidgetitem9 = self.goldPlateTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Pozycja", None));
        ___qtablewidgetitem10 = self.goldPlateTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Osoba", None));
        ___qtablewidgetitem11 = self.goldPlateTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Zmywanie", None));
        self.titleAddResults.setText(QCoreApplication.translate("MainWindow", u"Dodaj Wynik", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Data rozgrywki[d/m/r]:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 graczy:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Nazwa Gry", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Numer rozgrywki", None))
        self.addPlayer.setText(QCoreApplication.translate("MainWindow", u"Dodaj Gracza", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightBtn.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Miejsce:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nazwa Gracza", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Punkty", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Rezultat", None))
        self.nextPlayer.setText(QCoreApplication.translate("MainWindow", u"Nast\u0119pny Gracz", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Wyszukiwanie", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Nazwa Gry", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"W\u0142a\u015bciciel", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Czas Gry", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Min. Graczy", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Max. Graczy", None))
        self.searchItem.setText(QCoreApplication.translate("MainWindow", u"Szukaj", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dodaj Gr\u0119", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nazwa Gry:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Typ Gry:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Min. graczy:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Max. graczy:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Czas gry:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"W\u0142a\u015bciciel:", None))
        self.saveGame.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.infoNotification.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright ...", None))
        self.sizeGrip.setText("")
    # retranslateUi

