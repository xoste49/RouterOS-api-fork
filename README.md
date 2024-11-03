# RouterOS-api

Python API to RouterBoard devices produced by [MikroTik](https://mikrotik.com/) written by [Social WiFi](https://socialwifi.com).

## Usage

### Connection

```python
#!/usr/bin/python

import routeros_api_fork

connection = routeros_api_fork.RouterOsApiPool('IP', username='admin', password='')
api = connection.get_api()
```

#### Connect Options

```python
routeros_api_fork.RouterOsApiPool(
    host,
    username='admin',
    password='',
    port=8728,
    use_ssl=False,
    ssl_verify=True,
    ssl_verify_hostname=True,
    ssl_context=None,
)
```

Parameters:

* `host` - String - Hostname or IP of device

Optional Parameters:

* `username` - String - Login username - Default 'admin'
* `password` - String - Login password - Default empty string
* `port` - Integer - TCP Port for API - Default 8728 or 8729 when using SSL
* `plaintext_login` - Boolean - Try plaintext login (for RouterOS 6.43 onwards) - Default **False**
* `use_ssl` - Boolean - Use SSL or not? - Default **False**
* `ssl_verify` - Boolean - Verify the SSL certificate? - Default **True**
* `ssl_verify_hostname` - Boolean - Verify the SSL certificate hostname matches? - Default **True**
* `ssl_context` - Object - Pass in a custom SSL context object. Overrides other options. - Default **None**

#### Using SSL

If we want to use SSL, we can simply specify `use_ssl` as `True`:

```python
connection = routeros_api_fork.RouterOsApiPool('<IP>', username='admin', password='', use_ssl=True)
```

This will automatically verify SSL certificate and hostname. 
The most flexible way to modify SSL parameters is to provide an SSL Context object using the 
`ssl_context` parameter, but for typical use-cases with self-signed certificates, the shorthand options of
 `ssl_verify` and `ssl_verify_hostname` are provided.

e.g. if using a self-signed certificate, you can (but probably shouldn't) use:

```python
connection = routeros_api_fork.RouterOsApiPool(
    '<IP>',
    username='admin',
    password='',
    use_ssl=True,
    ssl_verify=False,
    ssl_verify_hostname=False,
)
```

#### Login for RouterOS v6.43 onwards

RouterOS Versions v6.43 onwards now use a different login method. 
The disadvantage is that it passes the password in plain text. 
For security we only attempt the plaintext login if requested using the `plaintext_login` parameter. 
It is highly recommended only to use this option with SSL enabled.

```python
routeros_api_fork.RouterOsApiPool(host, username='admin', password='', plaintext_login=True)
```

### Execute Commands

Call this with a resource and parameters as name/value pairs.

```python
api.get_binary_resource('/').call('<resource>',{ <dict of params> })
```

#### Examples

```python
api.get_binary_resource('/').call('tool/fetch',{ 'url': "https://dummy.url" })
api.get_binary_resource('/').call('ping', { 'address': '192.168.56.1', 'count': '4' })
```

### Fetch List/Resource

```python
list = api.get_resource('/command')
```

#### Example

```python
list_queues = api.get_resource('/queue/simple')
```

#### Show all elements

```python
list_queues.get()
```

### Add rules

```python
list.add(attribute="vale", attribute_n="value")
```

**NOTE**: Atributes with `-`, like `max-limit` use underscore `_`: `max_limit`

#### Example:

```python
list_queues.add(name="001", max_limit="512k/4M", target="192.168.10.1/32")
```

### Update Values

```python
list.set(id, attributes)
```

#### Example:

```python
list_queues.set(id="*2", name="jhon")
```

### Get element:

```python
list.get(attribute=value)
```

#### Example:

```python
list_queues.get(name="jhon")
```

### Remove element:

```python
list.remove(id)
```

#### Example:

```python
list_queues.remove(id="*2")
```

### Close conection:

```python
connection.disconnect()
```

### Run script and get output

The example script only prints "hello". Here's a simplifed example of how to run it and get the output:

```
>>> api.get_resource("/system/script").get()[0]['source']
'/put "hello"'
>>> async_response = api.get_binary_resource('/').call('system/script/run', {"number": '0'.encode('utf-8')})
>>> async_response.__dict__
{'command': <routeros_api_fork.sentence.CommandSentence object at 0x73a0f2b3eba0>, 'done_message': {'ret': b'hello'}, 'done': True, 'error': None}
>>> async_response.done_message['ret']
b'hello'
```

### Other Example:

```python
list_address =  api.get_resource('/ip/firewall/address-list')
list_address.add(address="192.168.0.1",comment="P1",list="10M")

list_address.get(comment="P1")

list_address.remove(id="*7")
```
