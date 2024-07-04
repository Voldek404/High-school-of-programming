from list_sort.my_sort import list_sort
from list_sort.my_sort import generate_list
import pytest


class TestRepeat:

    @pytest.mark.repeat(6)
    def test_function(self):
        test_list = generate_list(10)
        assert list_sort(test_list) == sorted(test_list)


if __name__ == '__main__':
    pytest.main()
