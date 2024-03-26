def next_letter(letter, number):
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


def num_to_col_name(n):
  name = ''
  while n > 0:
      n, rem = divmod(n - 1, 26)
      name = chr(65 + rem) + name
  return name