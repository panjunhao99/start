### vecter用法

```cpp
vector<vector<int> > res(m, vector<int>(n, 0));     // 注意大尖括号最后最好要空一格
```

定义了一个vector容器，元素类型为```vector<int>```，初始化为包含m个```vector<int>```对象，每个对象都是一个新创立的```vector<int>```对象的拷贝，而这个新创立的```vector<int>```对象被初始化为包含n个0。即(m * n)的矩阵，初始元素都为0.




