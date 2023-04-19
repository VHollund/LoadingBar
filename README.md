# LoadingBar.Py
### The simplest loadingbar i could think of.
By Vetle Hollund

## Usage
```python
from loadingbar import LoadingBar

k=LoadingBar() # fill material and width are optional arguments
k.LoadingBar(x) # x is the current percentage
```

## Example
```python
from loadingbar import LoadingBar

if __name__ == '__main__':
    k=LoadingBar(20, "█")
    for x in range(0, 101):
        k.LoadingBar(x)
        time.sleep(0.1)
```


