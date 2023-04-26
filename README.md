# LoadingBar.Py
### The simplest loadingbar i could think of.
By Vetle Hollund

## Usage


```python
pip install LoadingBar_Py_Diggs
```

## Example 1
```python
from loadingbar import LoadingBar

if __name__ == '__main__':
    k=LoadingBar(20, "█")
    for x in range(0, 101):
        k.update(x)
        time.sleep(0.1)
```

## Example 2
```python
from loadingbar import LoadingBar
bar = LoadingBar(width=20, fill="=", color="yellow", emptycolor="grey", start="Processing: |", end="| Done!")
bar.update(50)
```
output:
<div style="background-color:#000000; ">
<pre style="font-family: Courier; background-color:#33475b;">Processing: |<span style="color:green;">========<span>          | Done! 50% </pre>
<div>
