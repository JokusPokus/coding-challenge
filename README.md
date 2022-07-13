## Pyfold

The pyfold package implements a common [fold](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) function
in pure Python. Both left and right folding are available (see below).


### Usage

The package can be installed by navigating to the parent
directory of `src` and running:

```sh
python -m pip install .
```

Now, the `fold` function is available via:

```python
from pyfold import fold

# Usage examples
fold([1, 2, 3], 0, lambda x, y: x + y)  # 6
fold(['y', 'e'], 'h', lambda x, y: x + y, right=True)  # 'hey'
```

### Tests

To run tests, install and run the `pytest` package:
    
```sh
python -m pip install pytest
pytest
```

### Build

For distribution purposes, the `pyfold` package can be conveniently built into 
a source archive and python wheel using the `build` package:

```sh
python -m pip install build
python -m build
```
