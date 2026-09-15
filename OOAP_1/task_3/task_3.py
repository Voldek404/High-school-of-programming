class ParentList<T>

// статусы

    HEAD_NIL = 0;
    HEAD_OK = 1;
    HEAD_ERR = 2;

    TAIL_NIL = 0;
    TAIL_OK = 1;
    TAIL_ERR = 2;

    RIGHT_NIL = 0;
    RIGHT_OK = 1;
    RIGHT_ERR = 2;

    LEFT_NIL = 0;
    LEFT_OK = 1;
    LEFT_ERR = 2;

    PUT_LEFT_NIL = 0;
    PUT_LEFT_OK = 1;
    PUT_LEFT_ERR = 2;

    PUT_RIGHT_NIL = 0;
    PUT_RIGHT_OK = 1;
    PUT_RIGHT_ERR = 2;

    REMOVE_NIL = 0;
    REMOVE_OK = 1;
    REMOVE_ERR = 2;

    REPLACE_NIL = 0;
    REPLACE_OK = 1;
    REPLACE_ERR = 2;

    FIND_NIL = 0;
    FIND_OK = 1;
    FIND_ERR = 2;

    ADD_TO_EMPTY_NIL = 0;
    ADD_TO_EMPTY_OK = 1;
    ADD_TO_EMPTY_ERR = 2;

    GET_NIL = 0;
    GET_OK = 1;
    GET_ERR = 2;


// конструктор

// постусловие: создан новый пустой список
    ParentList<T>()


// команды

// предусловие: список непустой
// постусловие: курсор установлен на первый узел списка
    def head();

// предусловие: список непустой
// постусловие: курсор установлен на последний узел списка
    def tail();

// предусловие: правее курсора есть элемент
// постусловие: курсор сдвинут на один узел вправо
    def right();

// предусловие: левее курсора есть элемент
// постусловие: курсор сдвинут на один узел влево
    def left();

// предусловие: список непустой
// постусловие: перед текущим узлом добавлен новый узел
// с заданным значением
    def put_left(value);

// предусловие: список непустой
// постусловие: после текущего узла добавлен новый узел
// с заданным значением
    def put_right(value);

// предусловие: список непустой
// постусловие: текущий узел удалён;
// курсор смещён к правому соседу, если он есть,
// иначе к левому соседу, если он есть
    def remove();

// постусловие: список очищен от всех элементов
    def clear();

// предусловие: список пустой
// постусловие: в списке один узел со значением value
    def add_to_empty(value);

// постусловие: новый узел добавлен в хвост списка
    def add_tail(value);

// предусловие: список непустой
// постусловие: значение текущего узла заменено на value
    def replace(value);

// предусловие: список непустой
// постусловие: курсор установлен на следующий узел
// с искомым значением, если такой узел найден
    def find(value);


// запросы

// предусловие: список непустой
    def get();

// возвращает true, если курсор находится на первом узле
    def is_head() -> bool;

// возвращает true, если курсор находится на последнем узле
    def is_tail() -> bool;

// возвращает true, если курсор установлен на узле
    def is_value() -> bool;

    def size() -> int;


// дополнительные запросы

    def get_head_status() -> int;
    def get_tail_status() -> int;
    def get_right_status() -> int;
    def get_left_status() -> int;
    def get_put_right_status() -> int;
    def get_put_left_status() -> int;
    def get_remove_status() -> int;
    def get_replace_status() -> int;
    def get_find_status() -> int;
    def get_add_to_empty_status() -> int;
    def get_get_status() -> int;


// --------------------------------------------------
// LinkedList
// --------------------------------------------------

class LinkedList<T> extends ParentList<T>

// Дополнительной логики не требуется.
// Интерфейс LinkedList не предоставляет left() пользователю.
// Вся реализация операций находится в ParentList.


// --------------------------------------------------
// TwoWayList
// --------------------------------------------------

class TwoWayList<T> extends ParentList<T>

// предусловие: левее курсора есть элемент
// постусловие: курсор сдвинут на один узел влево
    def left();

