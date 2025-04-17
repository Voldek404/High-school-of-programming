# 5.3  Оцените, насколько поиск узла в дереве, представленном в виде массива, эффективнее (или неэффективнее) поиска узла в классическом дереве с указателями.
# В случае поиска по бинарному дереву поиска с указателями и поиску по дереву в виде списка мы получим O(log n)
# Однако же, если иметь отсортированный массив, то нужное нам значение можно отыскать бинарным поиском, который будет проивзодительнее
# перехода по индексам в неотсортированном масииве и обычном BST с указателями


# 5.5 По части картинки я бы ответил, что бинарное дерево поиска уже само по себе отсортировано определенным путем, а именно расположением
# элементов в правом и левом поддереве. Выполнить же in-order обход за О(1) невозможно само себе.


# 5.4 Реализуйте метод удаления узла из двоичного дерева, заданного в виде массива.
# Несмотря на отсутствие пустых мест, метод должен корректно перестраивать дерево, сохраняя балансировку.
# Здесь мы по сути повторяем метод из второго задания, но вместо указателей детей и родителей используем индексы
# С помощью них и производим балансировку

def deleteNodeByIndex(node_value, bst_list):
    # Если узла нет в дереве
    if node_value not in bst_list:
        return None


    current_index = bst_list.index(node_value)
    parent_index = (current_index - 1) // 2

    left_index  = 2 * current_index + 1
    right_index = 2 * current_index + 2

    has_left = False
    if left_index < len(bst_list) and bst_list[left_index] is not None:
        has_left = True
    has_right = False
    if right_index < len(bst_list) and bst_list[right_index] is not None:
        has_right = True

    if not has_left and not has_right:
        if current_index == 0:
            bst_list[0] = None
        else:
            parent_left  = 2 * parent_index + 1
            parent_right = 2 * parent_index + 2
            if bst_list[parent_left] == node_value:
                bst_list[parent_left] = None
            else:
                bst_list[parent_right] = None
    elif has_left and not has_right:
        child_index = left_index

        if current_index == 0:
            bst_list[0] = bst_list[child_index]
        else:
            parent_left  = 2 * parent_index + 1
            parent_right = 2 * parent_index + 2
            if bst_list[parent_left] == node_value:
                bst_list[parent_left] = bst_list[child_index]
            else:
                bst_list[parent_right] = bst_list[child_index]

        bst_list[child_index] = None

    elif has_right and not has_left:
        child_index = right_index

        if current_index == 0:
            bst_list[0] = bst_list[child_index]
        else:
            parent_left  = 2 * parent_index + 1
            parent_right = 2 * parent_index + 2
            if bst_list[parent_left] == node_value:
                bst_list[parent_left] = bst_list[child_index]
            else:
                bst_list[parent_right] = bst_list[child_index]

        bst_list[child_index] = None

    else:
        succ_parent = current_index
        succ_index  = right_index
        while True:
            left_succ = 2 * succ_index + 1
            if left_succ < len(bst_list) and bst_list[left_succ] is not None:
                succ_parent = succ_index
                succ_index  = left_succ
            else:
                break

        bst_list[current_index] = bst_list[succ_index]

        succ_right = 2 * succ_index + 2
        if succ_right < len(bst_list) and bst_list[succ_right] is not None:
            bst_list[succ_index] = bst_list[succ_right]
            bst_list[succ_right] = None
        else:
            bst_list[succ_index] = None

    return bst_list





