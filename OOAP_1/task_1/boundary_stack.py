class BoundedStack<T>

  // скрытые поля
  private List<T> stack; // основное хранилище стека
  private int peek_status; // статус запроса peek()
  private int pop_status; // статус команды pop()
  private int boundary_limit; // ограничение размера стека

  // интерфейс класса, реализующий АТД Stack
  public const int POP_NIL = 0;
  public const int POP_OK = 1;
  public const int POP_ERR = 2;
  public const int PEEK_NIL = 0;
  public const int PEEK_OK = 1;
  public const int PEEK_ERR = 2;

  // конструктор
  // постусловие - создается пустой стек с заданным размером, если размер не задан размер по умолчанию 32
  public BoundedStack(int max_size)

  // команды
  // предусловие - размер текущего стека меньше ограничительного размера
  // постусловие - в стек добавлен новый элемент
  public void push(T value)

  // предусловие - размер текущего стека больше нуля
  // постусловие - размер стека уменьшился на 1
  public void pop()

  // постусловие - из стека удалятся все значения
  public void clear()
    stack = [ ] // пустой список/стек

    // начальные статусы для предусловий peek() и pop()
    peek_status = PEEK_NIL
    pop_status = POP_NIL

  public T peek()


  public int size()


  // запросы статусов
  public int get_pop_status()

  public int get_peek_status()

