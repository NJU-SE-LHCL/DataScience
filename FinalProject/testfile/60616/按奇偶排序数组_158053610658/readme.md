### 题目描述

给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

### 输入描述

```
一个非负整数数组。
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
```
### 输出描述

```
排序后的数组
```

### 测试样例
#### 样例1: 输入-输出-解释
```
[4,2,5,7]
```
```
[4,5,2,7]
```
```
[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
```