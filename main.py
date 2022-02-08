from interface import *
from configparser import ConfigParser
import os, sys
import gspread

from Custom_Widgets.Widgets import *


class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		loadJsonStyle(self, self.ui)

		##############################################################################################
		###################################### OPEN FILE *.INI ######################################
		##############################################################################################
		parser = ConfigParser()
		parser.read('main.ini')
		self.sheet_file_results = parser.get('sheet', 'sheet_file_results')
		self.sheet_file_boardgames = parser.get('sheet', 'sheet_file_boardgames')
		self.sheet_all_boardgames = parser.get('sheet', 'sheet_all_boardgames')
		self.sheet_players = parser.get('sheet', 'sheet_players')
		self.sheet_boardgames = parser.get('sheet', 'sheet_boardgames')
		self.sheet_results = parser.get('sheet', 'sheet_results')
		self.sheet_table_winners = parser.get('sheet', 'sheet_table_winners')

		##############################################################################################
		###################################### SHOW APP ##############################################
		##############################################################################################
		self.show()

		##############################################################################################
		# EXPAND CENTER MENU WIDGET SIZE
		self.ui.settingBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
		self.ui.informationBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
		self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

		# CLOSE CENTER MENU WIDGET
		self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

		# EXPAND RIGHT MENU WIDGET SIZE
		self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
		self.ui.profileManuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
		self.ui.searchBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

		# CLOSE RIGHT MENU WIDGET 
		self.ui.closeRightBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

		# CLOSE NOTIFICATION MENU WIDGET 
		self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
		##############################################################################################

		##############################################################################################
		###################################### INITIALIZATION WIDGET #################################
		##############################################################################################
		# Widget Add Board Game
		self.nameGame = self.findChild(QLineEdit, 'nameGame')
		# self.typeGame = self.findChild(QLineEdit, 'typeGame')
		self.typeGame = self.findChild(QComboBox, 'typeGame')
		self.maxPlayer = self.findChild(QLineEdit, 'maxPlayer')
		self.minPlayer = self.findChild(QLineEdit, 'minPlayer')
		self.timeGame = self.findChild(QLineEdit, 'timeGame')
		self.owner = self.findChild(QLineEdit, 'owner')

		typeGameList = ["Podstawka", "Dodatek"]
		self.typeGame.addItems(typeGameList)

		# Widget Notification
		self.notificationBtn = self.findChild(QPushButton, 'notificationBtn')
		self.infoNotification = self.findChild(QLabel, 'infoNotification')

		# Widget Settings
		self.saveSettingsBtn = self.findChild(QPushButton, 'saveSettings')
		self.listAllGames = self.findChild(QLineEdit, 'listAllGames')
		self.listGames = self.findChild(QLineEdit, 'listGames')
		self.playersSheet = self.findChild(QLineEdit, 'playersSheet')
		self.resultsDay = self.findChild(QLineEdit, 'resultsDay')
		self.tableWinners = self.findChild(QLineEdit, 'tableWinners')
		self.urlBordGamesSheet = self.findChild(QLineEdit, 'urlBordGamesSheet')
		self.urlStatisticSheet = self.findChild(QLineEdit, 'urlStatisticSheet')		

		##############################################################################################
		###################################### SHOW LABEL SETTINGS ###################################
		##############################################################################################
		self.listAllGames.setText(self.sheet_all_boardgames)
		self.listGames.setText(self.sheet_boardgames)
		self.playersSheet.setText(self.sheet_players)
		self.resultsDay.setText(self.sheet_results)
		self.tableWinners.setText(self.sheet_table_winners)
		self.urlBordGamesSheet.setText(self.sheet_file_boardgames)
		self.urlStatisticSheet.setText(self.sheet_file_results)

		##############################################################################################
		###################################### SAVE SETTINGS #########################################
		##############################################################################################
		self.saveSettingsBtn.clicked.connect(self.saveSettings)

		##############################################################################################
		###################################### ADD BOARD GAMES #######################################
		##############################################################################################
		self.saveGameBtn = self.findChild(QPushButton, 'saveGame')
		# self.NotificationBtn = self.findChild(QPushButton, 'NotificationBtn')
		self.saveGameBtn.clicked.connect(self.saveGame)
		# self.saveGameBtn.clicked.connect(self.NotificationBtn)

		##############################################################################################
		######################################### DATA UPDATE ########################################
		##############################################################################################
		self.notificationBtn.clicked.connect(self.dataUpdate)

		##############################################################################################
		###################################### CONNECT TO GOOGLE #####################################
		##############################################################################################
		# Retrieve data
		self.worksheet_game = self.openSheet("Gry", self.sheet_file_boardgames)
		res = self.worksheet_game.get_all_values()
		print(res)

		# Extract row values from the object
		for x in range(len(res)):
			# print(res[x])
			if x > 0:
				# print(res[x][1:7])
				self.insertNewGameTableRow(res[x][1:7])

		self.worksheet_results = self.openSheet("Wyniki", self.sheet_file_results)
		res = self.worksheet_results.get_all_values()

		for x in range(len(res)):
			if x > 2:
				# print(res[x][1:4])
				self.insertNewWinnerTableRow(res[x][1:4])

		for x in range(len(res)):
			if x > 2:
				# print(res[x][5:8])
				self.insertNewGoldPlateTableRow(res[x][5:8])


		##############################################################################################
		##################################### SETTINGS GAME TABLET ###################################
		##############################################################################################
		self.gameTablet = self.findChild(QTableWidget, 'gameTablet')
		self.gameTablet.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.gameTablet.resizeColumnsToContents()

		##############################################################################################

	# A FUNCTION TO INSERT NEW TABLE ROWS
	def insertNewWinnerTableRow(self, items):
		# Create New row
		rowPosition = self.ui.winnerTable.rowCount()
		self.ui.winnerTable.insertRow(rowPosition)

		for x in range(len(items)):
			if items[1] == '':
				break
			qtablewidgetitem = QTableWidgetItem()
			self.ui.winnerTable.setItem(rowPosition, x, qtablewidgetitem)

			qtablewidgetitem = self.ui.winnerTable.item(rowPosition, x)
			# print(qtablewidgetitem)
			qtablewidgetitem.setText(str(items[x]))


	def insertNewGoldPlateTableRow(self, items):
		# Create New row
		rowPosition = self.ui.goldPlateTable.rowCount()
		self.ui.goldPlateTable.insertRow(rowPosition)

		for x in range(len(items)):
			if items[1] == '':
				break
			qtablewidgetitem = QTableWidgetItem()
			# print(rowPosition, x, items[1])
			self.ui.goldPlateTable.setItem(rowPosition, x, qtablewidgetitem)

			qtablewidgetitem = self.ui.goldPlateTable.item(rowPosition, x)
			# print(qtablewidgetitem)
			qtablewidgetitem.setText(str(items[x]))


	def insertNewGameTableRow(self, items):
		# Create New row
		rowPosition = self.ui.gameTablet.rowCount()
		self.ui.gameTablet.insertRow(rowPosition)

		# Insert row values
		for x in range(len(items)):
			# print(str(items[x]))
			# Create Widget
			qtablewidgetitem = QTableWidgetItem()
			# print(qtablewidgetitem.setText(str(x)))
			# print(rowPosition, x)
			self.ui.gameTablet.setItem(rowPosition, x, qtablewidgetitem)
			# Add item
			qtablewidgetitem = self.ui.gameTablet.item(rowPosition, x)
			# print(qtablewidgetitem)
			qtablewidgetitem.setText(str(items[x]))


	# A FUNCTION OPEN SHEET
	def openSheet(self, name_sheet, url_sheet):
		# Json File Key
		gc = gspread.service_account(filename='credentials.json')
		# Url Google Sheets
		sh = gc.open_by_url(url_sheet)
		# Select Sheet
		worksheet = sh.worksheet(name_sheet)
		return worksheet


	# A FUNCTION SAVE GAME IN GOOGLE SHEET
	def saveGame(self):
		if self.typeGame.currentText() == "Podstawka":
			typeG = 'P'
		elif self.typeGame.currentText() == "Dodatek":
			typeG = 'D'

		newGame = []
		newGame.append(int(len(self.worksheet_game.get_all_values())))
		newGame.append(self.nameGame.text())
		newGame.append(typeG)
		newGame.append(int(self.minPlayer.text()))
		newGame.append(int(self.maxPlayer.text()))
		newGame.append(int(self.timeGame.text()))
		newGame.append(self.owner.text())
		# newGame2 = [f'{self.nameGame.text()}', f'{self.typeGame.text()}', f'{self.minPlayer.text()}', f'{self.maxPlayer.text()}', f'{self.timeGame.text()}', f'{self.owner.text()}']
		# print(newGame)
		# print(newGame2)

		self.worksheet_game.append_row(newGame)
		self.infoNotification.setText(f'Gra "{self.nameGame.text()}" została zapisana!')


	# A FUNCTION SAVE SATTINGS APP
	def saveSettings(self):
		parser = ConfigParser()
		parser.read('main.ini')

		parser.set('sheet', 'sheet_file_results', self.urlStatisticSheet.text())
		parser.set('sheet', 'sheet_file_boardgames', self.urlBordGamesSheet.text())
		parser.set('sheet', 'sheet_all_boardgames', self.listAllGames.text())
		parser.set('sheet', 'sheet_players', self.playersSheet.text())
		parser.set('sheet', 'sheet_boardgames', self.listGames.text())
		parser.set('sheet', 'sheet_results', self.resultsDay.text())
		parser.set('sheet', 'sheet_table_winners', self.tableWinners.text())

		with open('main.ini', 'w') as configfile:
			parser.write(configfile)

		self.infoNotification.setText('Zapisano ustawienia!')


	def dataUpdate(self):
		self.infoNotification.setText('Zaaktualizowano bazę danych')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
