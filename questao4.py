import unittest

# Dado um a lista de números, retorna uma lista onde
# todo elemento adjacente e repetido será deletado reduzindo a um único elemento.
# Então, [1, 2, 2, 3] retornará [1, 2, 3]
# Você pode criar uma nova lista ou modificar a lista atual.
def remove_adjacent(nums):
  index = 0
  while True:
    if index >= len(nums) - 1 or len(nums) <= 1:
      return nums
    elif nums[index] == nums[index + 1]:
      nums.pop(index + 1)
    else:
      index += 1

# Dado duas listas ordenadas em ordem crescente, criar e retornar uma
# lista de todos os elementos em ordem algabética.
# Você pode modificar as listas passadas.
# Idealmente, a solução deve trabalhar em tempo "linear", que passa uma única vez em ambas as listas.
def linear_merge(list1, list2):
  list3 = list1 + list2
  list3.sort()
  return list3

class MyTest(unittest.TestCase):
  def test_remove_adjacent(self):
    self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    # Repare que são excluídos apenas os valores repetidos e adjacentes
    self.assertEqual(remove_adjacent([1, 2, 3, 2, 3]), [1, 2, 3, 2, 3])
    self.assertEqual(remove_adjacent([]), [])

  def test_linear_merge(self):
    self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])

if __name__ == '__main__':
  unittest.main()