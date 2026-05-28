'''
1. 创建一个包含类别特征的 DataFrame：

```python
import pandas as pd
data = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'blue', 'red', 'green', 'red', 'blue'],
    'size': ['S', 'M', 'L', 'M', 'S', 'L', 'M', 'S'],
    'price': [10, 20, 30, 25, 12, 28, 15, 22]
})
```

2. 对 `color` 和 `size` 列做 One-Hot 编码（使用 `pd.get_dummies` 或 `OneHotEncoder`）
3. 打印编码后的 DataFrame
4. 说明编码后有多少列，哪些列是新增的

'''

import pandas as pd
data = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'blue', 'red', 'green', 'red', 'blue'],
    'size': ['S', 'M', 'L', 'M', 'S', 'L', 'M', 'S'],
    'price': [10, 20, 30, 25, 12, 28, 15, 22]
})

print(data)

data_encoded = pd.get_dummies(
    data,
    columns=["color", "size"]
)

print(data_encoded)

# 编码后有7列（不包含索引），除了price都是新增的