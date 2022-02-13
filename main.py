from interface import *
from configparser import ConfigParser
import os, sys
import gspread
import sqlite3

from Custom_Widgets.Widgets import *

conn = sqlite3.connect('listGames.db')
c = conn.cursor()

c.execute("""CREATE TABLE if not exists list_games(
	lp text,
	name_game text,
	type text,
	min_players text,
	max_players text,
	time_game text,
	owner text)
	""")

c.execute("""CREATE TABLE if not exists list_winners(
	position text,
	name_player text,
	points text)
	""")
c.execute("""CREATE TABLE if not exists list_gold_plate(
	position text,
	name_player text,
	percentage_of_losers text)
	""")
c.execute("""CREATE TABLE if not exists list_players(
	name_player text,
	id int)
	""")
c.execute("""CREATE TABLE if not exists list_games_id(
	name_game text,
	id int)
	""")

conn.commit()
conn.close()

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
		self.ui.addPlayer.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

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

		# Add Results	
		self.addPlayerBtn = self.findChild(QPushButton, 'addPlayer')
		self.nextPlayerBtn = self.findChild(QPushButton, 'nextPlayer')
		self.nameGameAdd = self.findChild(QComboBox, 'nameGameAdd')
		self.numberGame = self.findChild(QLineEdit, 'numberGame')
		self.valuePlayer = self.findChild(QLineEdit, 'valuePlayer')
		self.dateEdit = self.findChild(QDateEdit, 'dateEdit')
		self.namePlayer = self.findChild(QComboBox, 'namePlayer')
		self.results = self.findChild(QComboBox, 'results')
		self.points = self.findChild(QLineEdit, 'points')
		self.position = self.findChild(QLineEdit, 'position')

		##############################################################################################
		################################### BUILDING LIST COMBOBOX ###################################
		##############################################################################################
		# Combobox Type Game
		typeGameList = ["Podstawka", "Dodatek"]
		self.typeGame.addItems(typeGameList)

		# Combobox Types of Results
		resultsList = ["Zwyciężca", "Przegrany", "Zmywacz"]
		self.results.addItems(resultsList)

		# Open Database and bulding records from list players and list games
		conn = sqlite3.connect('listGames.db')
		c = conn.cursor()

		c.execute("SELECT * FROM list_players")
		records_players_list_db = c.fetchall()

		c.execute("SELECT * FROM list_games_id")
		records_games_list_db = c.fetchall()

		conn.commit()
		conn.close()

		# Combobox List Games
		nameGameAddList = []
		for record in records_games_list_db[1:]:
			# print(record[0])
			nameGameAddList.append(record[0])
		self.nameGameAdd.addItems(nameGameAddList)

		# Combobox List Players
		namePlayerList = []
		for record in records_players_list_db[1:]:
			# print(record[0])
			namePlayerList.append(record[0])
		self.namePlayer.addItems(namePlayerList)

		##############################################################################################
		########################################## ADD RESULTS #######################################
		##############################################################################################
		self.addPlayerBtn.clicked.connect(self.addPlayers)
		self.nextPlayerBtn.clicked.connect(self.nextPlayers)


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
		self.saveGameBtn.clicked.connect(self.saveGame)

		##############################################################################################
		######################################### DATA UPDATE ########################################
		##############################################################################################
		self.notificationBtn.clicked.connect(self.dataUpdate)

		##############################################################################################
		###################################### CONNECT TO GOOGLE #####################################
		##############################################################################################

		### 					In case of problems loading from the database file  			   ###

		"""
		# Retrieve data
		self.worksheet_game = self.openSheet("Gry", self.sheet_file_boardgames)
		res = self.worksheet_game.get_all_values()
		print(res)

		Extract row values from the object
		
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
		"""
		##############################################################################################
		########################### BUILDING A TABLE FROM A DATABASE FILE ############################
		##############################################################################################
		# Open Database
		conn = sqlite3.connect('listGames.db')
		c = conn.cursor()

		# Show List All Games From Database
		c.execute("SELECT * FROM list_games")
		records = c.fetchall()

		for x in range(len(records)):
			if x > 0:
				# print(records[x])
				self.insertNewGameTableRow(records[x][1:7])

		# Show List Player Winners From Database
		c.execute("SELECT * FROM list_winners")
		records = c.fetchall()

		for record in records[3:]:
			# if x > 2:
				# print(records[x])
			self.insertNewWinnerTableRow(record)

		# Show List Players Lossers From Database
		c.execute("SELECT * FROM list_gold_plate")
		records = c.fetchall()

		for record in records[3:]:
			if x > 2:
				self.insertNewGoldPlateTableRow(record)

		# Close Database
		conn.commit()
		conn.close()

		##############################################################################################
		#################################### SETTINGS GAMES TABLET ###################################
		##############################################################################################
		self.gameTablet = self.findChild(QTableWidget, 'gameTablet')
		self.gameTablet.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.gameTablet.resizeColumnsToContents()

		##############################################################################################

	##############################################################################################
	# A FUNCTION TO INSERT NEW TABLE ROWS
	##############################################################################################
	# Table Winners
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

	# Table Losers
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

	# Table All Games All Players
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
			if qtablewidgetitem == None:
				continue
			qtablewidgetitem.setText(str(items[x]))

	##############################################################################################
	# A FUNCTION OPEN SHEET
	##############################################################################################
	def openSheet(self, name_sheet, url_sheet):
		# Json File Key
		gc = gspread.service_account(filename='credentials.json')
		# Url Google Sheets
		sh = gc.open_by_url(url_sheet)
		# Select Sheet
		worksheet = sh.worksheet(name_sheet)
		return worksheet

	##############################################################################################
	# A FUNCTION SAVE GAME IN GOOGLE SHEET
	##############################################################################################
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

	##############################################################################################
	# A FUNCTION SAVE SATTINGS APP
	##############################################################################################
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

	##############################################################################################
	# FUNCTION UPDATING THE DATABASE FROM GOOGLE SHEET
	##############################################################################################
	def dataUpdate(self):
		self.infoNotification.setText('Zaaktualizowano bazę danych')

		### Downloading data from google sheet ###
		worksheet_game = self.openSheet(self.sheet_all_boardgames, self.sheet_file_boardgames)
		records_games = worksheet_game.get_all_values()
		# print(records_games)

		worksheet_results = self.openSheet(self.sheet_table_winners, self.sheet_file_results)
		records_table_winners = worksheet_results.get_all_values()
		# print(records_table_winners)

		worksheet_players_list = self.openSheet(self.sheet_players , self.sheet_file_results)
		records_players_list = worksheet_players_list.get_all_values()
		# print(records_players_list)

		worksheet_games_id = self.openSheet(self.sheet_boardgames, self.sheet_file_results)
		records_games_list = worksheet_games_id.get_all_values()
		######

		### Open Database ###
		conn = sqlite3.connect('listGames.db')
		c = conn.cursor()

		# Deleting date from the database
		c.execute("DELETE FROM list_games;")
		c.execute("DELETE FROM list_winners;")
		c.execute("DELETE FROM list_gold_plate;")
		c.execute("DELETE FROM list_players;")

		# Saving data to list_games in a database
		for record in records_games:
			# print(record)
			# print(res[r][0:7])
			temporary_lp = record[0]
			temporary_name_game = record[1]
			temporary_type = record[2]
			temporary_min_players = record[3]
			temporary_max_players = record[4]
			temporary_time_game = record[5]
			temporary_owner = record[6]
			c.execute("INSERT INTO list_games VALUES (:lp, :name_game, :type, :min_players, :max_players, :time_game, :owner)",
				{
					'lp': temporary_lp,
					'name_game': temporary_name_game,
					'type': temporary_type,
					'min_players': temporary_min_players,
					'max_players': temporary_max_players,
					'time_game': temporary_time_game,
					'owner': temporary_owner,
				})

		# Saving data to list_winners in a database
		for record in records_table_winners:
			temporary_position_winners = record[1]
			temporary_name_player_winners = record[2]
			temporary_points = record[3]
			temporary_position_plate = record[5]
			temporary_name_player_plate = record[6]
			temporary_losers = record[7]
			c.execute("INSERT INTO list_winners VALUES(:position, :name_player, :points)",
				{
					'position': temporary_position_winners,
					'name_player': temporary_name_player_winners,
					'points': temporary_points
				})
			c.execute("INSERT INTO list_gold_plate VALUES(:position, :name_player, :percentage_of_losers)",
				{
					'position': temporary_position_plate,
					'name_player': temporary_name_player_plate,
					'percentage_of_losers': temporary_losers
				})
		
		# Saving data to list_players in a database
		for record in records_players_list:
			temporary_player = record[0]
			temporary_id = record[2]
			c.execute("INSERT INTO list_players VALUES(:name_player, :id)",
				{
					'name_player': temporary_player,
					'id': temporary_id
				})

		# Saving data to list_games_id in a database
		for record in records_games_list:
			temporary_name_game = record[0]
			temporary_id = record[1]
			c.execute("INSERT INTO list_games_id VALUES(:name_game, :id)",
				{
					'name_game': temporary_name_game,
					'id': temporary_id
				})

		# c.execute("SELECT * FROM list_players")
		# self.records = c.fetchall()

		# Close Database
		conn.commit()
		conn.close()

		# for record in records:
		# 	print(record)


	##############################################################################################
	# 
	##############################################################################################
	def addPlayers(self):
		pass

	##############################################################################################
	# 
	##############################################################################################
	def nextPlayers(self):
		temporary = []

		print(self.dateEdit.text())
		# print(self.nameGameAdd.text())
		print(self.numberGame.text())
		print(self.valuePlayer.text())
		# print(self.namePlayer.text())
		# print(self.results.text())
		print(self.points.text())
		print(self.position.text())
		# self.nameGameAdd 
		# self.numberGame 
		# self.valuePlayer 
		# self.dateEdit 
		# self.namePlayer 
		# self.results
		# self.points 
		# self.position 

	##############################################################################################

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
