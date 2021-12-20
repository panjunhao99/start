
```python
for path, file_dir, files in os.walk(path):

for files in os.listdir(path):

if not device.startswith('G'):

if f.endswith('.json'):

region_list.append(region)

json.load()   
    def load_json(path):   
    import json
    lines = []     #  第一步：定义一个列表， 打开文件
    with open(path) as f:  
        for row in f.readlines(): # 第二步：读取文件内容 
            if row.strip().startswith("//"):   # 第三步：对每一行进行过滤 
                continue
            lines.append(row)                   # 第四步：将过滤后的行添加到列表中.
    return json.loads("\n".join(lines))       #将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！

print('json.loads 将整数类型的字符串转为int类型: type(json.loads("123456"))) --> {}'.format(type(json.loads("123456"))))
print('json.loads 将浮点类型的字符串转为float类型: type(json.loads("123.456")) --> {}'.format(type(json.loads("123.456"))))
print('json.loads 将boolean类型的字符串转为bool类型: type(json.loads("true")) --> {}'.format((type(json.loads("true")))))
print('json.loads 将列表类型的字符串转为列表: type(json.loads(\'["a", "b", "c"]\')) --> {}'.format(type(json.loads('["a", "b", "c"]'))))
print('json.loads 将字典类型的字符串转为字典: type(json.loads(\'{"a": 1, "b": 1.2, "c": true, "d": "ddd"}\')) --> %s' % str(type(json.loads('{"a": 1, "b": 1.2, "c": true, "d": "ddd"}'))))

```