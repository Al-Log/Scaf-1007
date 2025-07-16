## 📘 문제 이름
귤 고르기

- 🧩 난이도: level 2
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/138476)

---

### 🧠 문제 설명
한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 
귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성

---

### 💡 아이디어
- counter 모듈을 이용하면 리스트 내 요소 개수를 쉽게 구함
- tangerine을 Counter() 안에 넣고 많이 등장한 개수 순으로 정리
- 가장 개수가 많이 등장하는 귤 부터 선택해서 한 변수에 더하고 answer에 +1
- k 번 반복했다면 종료하고 answer 반환

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)
count 모듈을 활용하는 법을 배우는 문제였다

리스트에서 특정 원소의 개수를 세야 할 때 그것을 딕셔너리로 만들어주는 counter모듈은 꽤나 많은 문제에서 사용될 듯 하다.

잘못하면 엄청 긴 연속 반복문이 될 뻔한 문제를 간단하게 만들어주었다.

---

### 다른 사람의 풀이
카운터 모듈을 이용하지 않고 직접 딕셔너리에 추가하는 코드를 만든 풀이
numbers={}
for size in tangerine:
    if size not in numbers:
        numbers[size]=0
    numbers[size]+=1
만약 size(tangerine)의 값이 numbers안에 없다면 size를 키값으로한 0value값 생성, 있다면 그 value에 +1
