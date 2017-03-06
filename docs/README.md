# NuDB
> A database and search engine.

# Setup
```bash
pip install nudb

# or
git clone https://github.com/WuSzHs/nudb.git

```

# Usage
```python
from nudb import NuDB
nudb = NuDB()
```

## Connect to NuDB
```python
nudb.connect('host', 'db')
```

## Put record
```python

# json format
result = nudb.rput(data, 'json')

# text format
result = nudb.rput(data, 'text', recBeg)

```

## Put record by file
**DON'T USE, UNFINISHED**  
```python

# json format
result = nudb.fput(filePath, 'json')

# text format
result = nudb.fput(filePath, 'text', recBeg)

```

## Delete record by rid
```python
result = nudb.rdel(rid)
```

## Search
```python
result = nudb.search(query)
```

# Undo
+ Error handler
