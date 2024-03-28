import json
import utils.column_helper as ch
class LeagueHandler:

  def formatUnitTofloat(self, unit):
    floatUnit = float(unit.replace(',', '.')[3:])
    if unit[0] == '-':
      floatUnit = floatUnit * -1
    return floatUnit

  def groupResultsByLeague(self, tables, data):
    leagues = {}
    for table in tables:
      column = table['column']
      for line in range(table['firstLine']-2, table['lastLine']-1):
        leagueName = data[column][line]
        if leagueName not in leagues:
          leagues[leagueName] = []
        floatUnit = self.formatUnitTofloat(data[ch.next_letter(column,1)][line])
        print(data[column][1])
        leagues[leagueName].append({
          'date': str(data[column][1]),
          'units': floatUnit,
          'green': data[ch.next_letter(column,2)][line],
          'reds': data[ch.next_letter(column,3)][line],
          'tips': data[ch.next_letter(column,4)][line]
        })
    for key in leagues.keys():
      sumUnits = 0
      leagues[key] = sorted(leagues[key], key=lambda x: x['units'], reverse=True)
      for i in range(len(leagues[key])):
        sumUnits += leagues[key][i]['units']
      leagues[key].append({
          'units': sumUnits,
          'green': '-',
          'reds': '-',
          'tips': '-'
        })
       
    return leagues
