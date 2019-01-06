# Object Oriented Programming


* **class**
  adding new concept in program. 
  - vector 
  - geometry shapes 
  
```python
def compute_length(vector):
    return (vec['x']**2 + vec['y']**2)**0.5
    
def add_vector(vec1, vec2):
    x = vec1['x'] + vec2['x']
    y = vec1['y'] + vec2['y']
    return {'x': x, 'y': y}
    
    
vec1 = {'x': 10, 'y': 6}
vec2 = {'x': 1, 'y': 2}
print(vec1['x'], vec1['y'])
print(compute_length(vec))
vec3 = add_vector(vec1, vec2)
```
  
  
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def compute_length(self):
        return (self.x**2 + self.y**2)**0.5
        
    def __add__(self, othe):
vec1 = Vector(10, 6)   # instantiation, construction
vec2 = Vector(1, 2)
print(vec1.x)
print(vec1.y)
print(vec1.compute_length())
vec1 + vec2  # vec1.__add__(vec2)      # Vector.__add__(vec1, vec2)
```
  
  
* **instance**:
  `vec1 = Vector()`
  
  ```math
  v = (1, 2)
  ```
* property
* attribute
* method  



## functional approach:
```
f(o)
```

```python
def upper_string(s):
    pass 
    
    
text = "hello"
upper_string(text)
```

## object oriented approach
```
o.f()

```

```python
num = 11
text="hello"
text.upper()
```
