import json
from utils.spreadsheet_service import SpreadsheetService
from utils.league_handler import LeagueHandler

def main():
  f = open('config.json')
  config = json.load(f)
  f.close()

  fileName = './data/'+config['fileName']
  tables = config['tables']
  
  spreadsheetService = SpreadsheetService(fileName)

  data = spreadsheetService.read()

  leagueHandler = LeagueHandler()
  result = leagueHandler.groupResultsByLeague(tables, data)


  spreadsheetService.write(result, 'output.xlsx')
main()
