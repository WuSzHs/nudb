# NuDB
> A database and search engine.

# Setup
```bash
pip install nudb
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
```python
**UNFINISHED**
# json format
result = nudb.fput(filePath, 'json')

# text format
result = nudb.fput(filePath, 'text', recBeg)

```

## Get record by rid
```python
result = nudb.rget(rid)
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
