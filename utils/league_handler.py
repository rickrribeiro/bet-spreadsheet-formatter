import json
class LeagueHandler:

  def next_letter(self, letter, number):
    if len(letter) == 1:
        num = ord(letter) - ord('A') + number
        quotient, remainder = divmod(num, 26)
        return 'A' * quotient + chr(ord('A') + remainder)
    else:
        last_char = letter[-1]
        if last_char == 'Z':
            return next_letter(letter[:-1], number) + 'A'
        else:
            return letter[:-1] + next_letter(last_char, number)

  def groupResultsByLeague(self, tables, data):
    leagues = {}
    for table in tables:
      column = table['column']
      for line in range(table['firstLine']-2, table['lastLine']-1):
        leagueName = data[column][line]
        if leagueName not in leagues:
          leagues[leagueName] = []
        leagues[leagueName].append({
          'units': data[self.next_letter(column,1)][line],
          'green': data[self.next_letter(column,2)][line],
          'reds': data[self.next_letter(column,3)][line],
          'tips': data[self.next_letter(column,4)][line]
        })
    return leagues
