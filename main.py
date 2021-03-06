# Import Libraris File PySide2 App
from interface import *
from configparser import ConfigParser
import os, sys
import gspread
import sqlite3

from Custom_Widgets.Widgets import *

##############################################################################################
##################################### BUILDING DATABASE ######################################
##############################################################################################
# Open Database File
conn = sqlite3.connect('listGames.db')
c = conn.cursor()

# Create Table
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

# Close Database
conn.commit()
conn.close()

temporary_player_list = []

##############################################################################################

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		loadJsonStyle(self, self.ui)

		##############################################################################################
		###################################### OPEN FILE *.INI #######################################
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

		# Add Board Game
		self.saveGameBtn = self.findChild(QPushButton, 'saveGame')

		# Settings Game Table
		self.gameTablet = self.findChild(QTableWidget, 'gameTablet')
		##############################################################################################
		################################### BUILDING LIST COMBOBOX ###################################
		##############################################################################################
		# Combobox Type Game
		typeGameList = ["Podstawka", "Dodatek"]
		self.typeGame.addItems(typeGameList)

		# Combobox Types of Results
		resultsList = ["Wygrana", "Przegrana", "Zmywanie"]
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

		for x in range(1, len(records)):
			self.insertNewGameTableRow(records[x][1:7])

		# Show List Player Winners From Database
		c.execute("SELECT * FROM list_winners")
		records = c.fetchall()

		for record in records[3:]:
			self.insertNewWinnerTableRow(record)

		# Show List Players Lossers From Database
		c.execute("SELECT * FROM list_gold_plate")
		records = c.fetchall()

		for record in records[3:]:
			self.insertNewGoldPlateTableRow(record)

		# Close Database
		conn.commit()
		conn.close()

		##############################################################################################
		#################################### SETTINGS GAMES TABLE ####################################
		##############################################################################################
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

			# qtablewidgetitem = self.ui.winnerTable.item(rowPosition, x)
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
			self.ui.goldPlateTable.setItem(rowPosition, x, qtablewidgetitem)

			# qtablewidgetitem = self.ui.goldPlateTable.item(rowPosition, x)
			qtablewidgetitem.setText(str(items[x]))

	# Table All Games All Players
	def insertNewGameTableRow(self, items):
		# Create New row
		rowPosition = self.ui.gameTablet.rowCount()
		self.ui.gameTablet.insertRow(rowPosition)

		# Insert row values
		for x in range(len(items)):
			# Create Widget
			qtablewidgetitem = QTableWidgetItem()
			self.ui.gameTablet.setItem(rowPosition, x, qtablewidgetitem)
			# Add item
			# qtablewidgetitem = self.ui.gameTablet.item(rowPosition, x) # mo??liwe, ??e nie musze tego robi??
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

		worksheet_game = self.openSheet(self.sheet_all_boardgames, self.sheet_file_boardgames)

		newGame = []
		newGame.append(int(len(worksheet_game.get_all_values())))
		newGame.append(self.nameGame.text())
		newGame.append(typeG)
		newGame.append(int(self.minPlayer.text()))
		newGame.append(int(self.maxPlayer.text()))
		newGame.append(int(self.timeGame.text()))
		newGame.append(self.owner.text())

		worksheet_game.append_row(newGame)
		self.infoNotification.setText(f'Gra "{self.nameGame.text()}" zosta??a zapisana!')

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
		c.execute("DELETE FROM list_games_id")

		# Saving data to list_games in a database
		for record in records_games:
			# print(record)
			# print(res[r][0:7])
			c.execute("INSERT INTO list_games VALUES (:lp, :name_game, :type, :min_players, :max_players, :time_game, :owner)",
				{
					'lp': record[0],
					'name_game': record[1],
					'type': record[2],
					'min_players': record[3],
					'max_players': record[4],
					'time_game': record[5],
					'owner': record[6],
				})

		# Saving data to list_winners in a database
		for record in records_table_winners:
			c.execute("INSERT INTO list_winners VALUES(:position, :name_player, :points)",
				{
					'position': record[1],
					'name_player': record[2],
					'points': record[3]
				})
			c.execute("INSERT INTO list_gold_plate VALUES(:position, :name_player, :percentage_of_losers)",
				{
					'position': record[5],
					'name_player': record[6],
					'percentage_of_losers': record[7]
				})
		
		# Saving data to list_players in a database
		for record in records_players_list:
			c.execute("INSERT INTO list_players VALUES(:name_player, :id)",
				{
					'name_player': record[0],
					'id': record[2]
				})
		# Saving data to list_games_id in a database
		for record in records_games_list:
			c.execute("INSERT INTO list_games_id VALUES(:name_game, :id)",
				{
					'name_game': record[0],
					'id': record[1]
				})

		# c.execute("SELECT * FROM list_players")
		# self.records = c.fetchall()

		# Close Database
		conn.commit()
		conn.close()

		# for record in records:
		# 	print(record)

		self.infoNotification.setText('Zaaktualizowano baz?? danych')

	##############################################################################################
	# 
	##############################################################################################
	def addPlayers(self):
		self.addResults = []
		self.sumPlayer = 0
		self.position.setText("1")


		self.nameGameAdd.setDisabled(True)
		self.dateEdit.setDisabled(True)
		self.numberGame.setDisabled(True)
		self.valuePlayer.setDisabled(True)

	##############################################################################################
	# 
	##############################################################################################
	def nextPlayers(self):
		if self.sumPlayer == int(self.valuePlayer.text()):
			worksheet = self.openSheet(self.sheet_results, self.sheet_file_results)
			records = worksheet.get_all_values()

			for record in records:
				if record[0] == '':
					worksheet.update(f'A{records.index(record)+1}:K{(records.index(record)+len(self.addResults))+1}', self.addResults)
					# print(records.index(record))
					# print(len(self.addResults))
					break
				# print(record)

			# for record in self.addResults:
			# 	# worksheet.append_row(record)
			# 	print(record)
			# print(self.addResults)
			# print(self.sumPlayer)
			# print(self.namePlayer.currentText())
			self.namePlayer.addItems(temporary_player_list)

			self.nameGameAdd.setDisabled(False)
			self.dateEdit.setDisabled(False)
			self.numberGame.setDisabled(False)
			self.valuePlayer.setDisabled(False)
			self.position.setDisabled(False)
			self.points.setDisabled(False)
			self.namePlayer.setDisabled(False)
			self.results.setDisabled(False)

			self.ui.rightMenuContainer.collapseMenu()

		temporary = []



		###
		# ----------------------
		if self.results.currentText() == "Wygrana": #, "Przegrana", "Zmywanie"
			pointLoser = '-1'
			text = 'Wygrana'
		elif self.results.currentText() == "Przegrana":
			pointLoser = '0'
			text = 'Przegrana'
		elif self.results.currentText() == "Zmywanie":
			pointLoser = '1'
			text = 'Przegrana'
		else:
			print("b????d - zmienna warto??ci zmywania")

		# ----------------------
		pointResult = int(self.valuePlayer.text()) - int(self.position.text()) + 1



		# Open Database
		conn = sqlite3.connect('listGames.db')
		c = conn.cursor()

		# ----------------------
		c.execute('SELECT * FROM list_players WHERE name_player=?', (self.namePlayer.currentText(),))
		records = c.fetchall()
		id_player = records[0][1]

		# ----------------------
		c.execute('SELECT * FROM list_games_id WHERE name_game=?', (self.nameGameAdd.currentText(),))
		records = c.fetchall()
		id_game = records[0][1]

		conn.commit()
		conn.close()

		###
		temporary = [int(f'{self.numberGame.text()}'), 
						int(f'{id_game}'), # ID Gry
						f'{self.nameGameAdd.currentText()}', 
						int(f'{id_player}'),  # ID Gracza
						int(f'{self.position.text()}'), 
						f'{self.namePlayer.currentText()}', 
						int(f'{self.points.text()}'), 
						int(f'{pointResult}'), # rywalizacja
						int(f'{pointLoser}'), # zmywanie
						text,#f'{self.results.currentText()}',
						f'{self.dateEdit.text()}']

		self.addResults.append(temporary)
		self.sumPlayer += 1

		# self.namePlayer.removeItem(self.namePlayer.currentIndex())
		
		if self.sumPlayer < int(self.valuePlayer.text()):
			self.position.setText(str(int(self.position.text()) + 1))
			self.points.setText("")

		if self.sumPlayer <= int(self.valuePlayer.text()):
			#####
			temporary_player_list.append(self.namePlayer.currentText())
			# print(temporary_player_list)
			self.namePlayer.removeItem(self.namePlayer.currentIndex())
			#####



		if int(self.sumPlayer) == int(self.valuePlayer.text()) - 1:
			self.nextPlayerBtn.setText('Ostatni')
		elif self.sumPlayer == int(self.valuePlayer.text()):

			# self.position.setText("")
			# self.points.setText(" ")
			# self.namePlayer.setCurrentText("")
			# self.results.setCurrentText("")

			self.position.setDisabled(True)
			self.points.setDisabled(True)
			self.namePlayer.setDisabled(True)
			self.results.setDisabled(True)
			self.nextPlayerBtn.setText('Zako??cz')	



	##############################################################################################

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
