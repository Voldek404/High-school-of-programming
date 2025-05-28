import unittest

from task_7 import Heap

class TestHeapMethods(unittest.TestCase):
    def test_add_and_get_max(self):
        # Создаем экземпляр кучи
        heap = Heap()

        # Добавляем элементы в кучу
        heap.Add(10)
        heap.Add(20)
        heap.Add(5)

        # Проверяем, что максимальный элемент после добавления равен 20
        self.assertEqual(heap.GetMax(), 20)

        # Добавляем еще один элемент и проверяем максимальный элемент
        heap.Add(25)
        self.assertEqual(heap.GetMax(), 25)

    def test_get_max(self):
        heap = Heap()

        # Добавляем элементы
        heap.Add(10)
        heap.Add(20)
        heap.Add(5)

        # Проверяем извлечение максимального элемента
        self.assertEqual(heap.GetMax(), 20)
        self.assertEqual(heap.GetMax(), 10)
        self.assertEqual(heap.GetMax(), 5)

        # Проверяем, что куча пуста
        self.assertEqual(heap.GetMax(), -1)

    def test_make_heap(self):
        heap = Heap()

        # Строим кучу из списка
        heap.MakeHeap([15, 10, 20, 5, 30], 3)

        # Проверяем максимальный элемент
        self.assertEqual(heap.GetMax(), 30)

        # Убираем максимальный элемент
        heap.GetMax()

        # Проверяем, что максимальный элемент после удаления равен 20
        self.assertEqual(heap.GetMax(), 20)


if __name__ == "__main__":
    unittest.main()
