import unittest

#não veio com enunciado
def verbing(s):
    #SEU CODIGO AQUI
    pass


# Dado um astring, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
  not_index = s.find('not')
  bad_index = s.find('bad')
  if not_index < bad_index:
    switch = s[not_index : (bad_index + 3)]
    return s.replace(switch, "good")
  return s

# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frete (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a aprte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):
  alen = len(a)
  blen = len(b)
  if alen % 2 == 1:
    afront = a[:int((alen + 1) / 2)]
    aback = a[int((alen + 1) / 2):]
  else:
    afront = a[:int(alen / 2)]
    aback = a[int(alen / 2):]

  if blen % 2 == 1:
    bfront = b[:int((blen + 1) / 2)]
    bback = b[int((blen + 1) / 2):]
  else:
    bfront = b[:int(blen / 2)]
    bback = b[int(blen / 2):]
  return afront + bfront + aback + bback

class MyTest(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(verbing('hail'), 'hailing')
    self.assertEqual(verbing('swiming'), 'swimingly')
    self.assertEqual(verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

  def test_front_back(self):
    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()