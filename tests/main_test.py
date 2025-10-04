"""
test src/test_copier_propagation/main.py

run with:
```
uv run pytest tests/main_test.py
```
"""

import pytest

from test_copier_propagation import main


def test_main():
    with pytest.raises(NotImplementedError):
        main.main()
