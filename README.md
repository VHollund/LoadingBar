# LoadingBar.Py
### The simplest loadingbar i could think of.
By Vetle Hollund

## Usage


```python
pip install LoadingBar_Py_Diggs
```

## Example
```python
from loadingbar import LoadingBar

if __name__ == '__main__':
    k=LoadingBar(20, "█")
    for x in range(0, 101):
        k.update(x)
        time.sleep(0.1)
```


