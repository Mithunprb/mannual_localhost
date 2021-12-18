# mannual_localhost
Thia program uses SimpleHTTPServer, BaseHTTPServer moduels to assign HTTP protocol on given port

# Requirements:
* Python 2.7x

[localhost.py](./localhost.py)

```python
    protocol = "HTTP/1.0"
    host = ''
    port = 8000
```
Assign port number to the variable ```port```

* Python3 or above

[manual_localhost.py](./manual_localhost.py)
* Default ```port``` <br>
```python
python -m manual_localhost
```
* For manual ```port``` <br>
```python
python  -m manual_localhost -p 8080
```
