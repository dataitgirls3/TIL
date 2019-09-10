### 파이썬 설치
1. homebrew(mac)/chocolaty(win): 패키지 매니저 
2. pyenv: 파이썬 버전 왔다갔다 할 수 있게 하는 프로그램
    - brew update && brew upgrade pyenv
3. pyenv 통해서 파이썬 설치
4. pycharm: IDE

<br>

### 상태 변경 state transition
age = 13
<br>age += 1
<br>age -= 1
<br>age /= 2

factorial = 1  # 초기값 할당
<br>factorial *= 2
<br>factorial *= 3
<br>...
<br>factorial *= n  # 누산(accumulation)

```Python
for x in range(1:n+1):
    factorial *= x 
```
```Python
for x in [1,2,3]:
    factorial *= x
```
```Python
for x in range(1, n+1):
    y = x
    factorial *= y
```
