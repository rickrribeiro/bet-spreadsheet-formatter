import json
import utils.column_helper as ch
class LeagueHandler:

  def groupResultsByLeague(self, tables, data):
    leagues = {}
    for table in tables:
      column = table['column']
      for line in range(table['firstLine']-2, table['lastLine']-1):
        leagueName = data[column][line]
        if leagueName not in leagues:
          leagues[leagueName] = []
        leagues[leagueName].append({
          'units': data[ch.next_letter(column,1)][line],
          'green': data[ch.next_letter(column,2)][line],
          'reds': data[ch.next_letter(column,3)][line],
          'tips': data[ch.next_letter(column,4)][line]
        })
    return leagues
