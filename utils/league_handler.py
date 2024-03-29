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
          leagues[leagueName] = {
            'sumUnits': 0,
            'results': []
          }
        floatUnit = self.formatUnitTofloat(data[ch.next_letter(column,1)][line])
        print(data[column][1])
        leagues[leagueName]['results'].append({
          'date': str(data[column][1]),
          'units': floatUnit,
          'green': data[ch.next_letter(column,2)][line],
          'reds': data[ch.next_letter(column,3)][line],
          'tips': data[ch.next_letter(column,4)][line]
        })
    for key in leagues.keys():
      sumUnits = 0
      for i in range(len(leagues[key]['results'])):
        sumUnits += leagues[key]['results'][i]['units']
      leagues[key]['sumUnits'] = sumUnits
    sortedLeagues = sorted(leagues.items(), key=lambda x: x[1]['sumUnits'], reverse=True)
    return sortedLeagues
