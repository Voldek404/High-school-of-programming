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

  public void Stack(size)// конструктор
    boundary_limit = size if size else 32
    clear()

  public void push(T value)
    assert size < boundary limit
    stack.Append(value)

  public void pop()
    if size() > 0
      stack.RemoveAt(-1)
      pop_status = POP_OK
    else
      pop_status = POP_ERR

  public void clear()
    stack = [ ] // пустой список/стек

    // начальные статусы для предусловий peek() и pop()
    peek_status = PEEK_NIL
    pop_status = POP_NIL

  public T peek()
    if size() > 0
      result = stack[-1]
      peek_status = PEEK_OK
    else
      result = 0
      peek_status = PEEK_ERR
    return result

  public int size()
    return stack.Length()

  // запросы статусов
  public int get_pop_status()
    return pop_status

  public int get_peek_status()
    return peek_status
