## 📘 문제 이름


- 🧩 난이도: level 2
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/42747)

---

### 🧠 문제 설명
발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성

---

### 💡 아이디어
- 우선 인용을 적게 한 순서 대로 정렬
- 이단 반복문을 엮어서 i가 j보다 작거나 같을 때 조건 만족을 하니 cnt 변수에 1추가
- 반복을 끝내고 cnt와 i 둘중 작은 것과 answer를 비교해 더 큰것을 answer로 설정
- 내부,외부 반복문을 모두 끝내면 최종 answer 반환

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)
이중 반복문을 통한 간단한 구조이다

가장 많이 인용된 횟수를 찾는 것이기에 min,max를 이용한 구조가 명확하고 간단히 느껴졌다

---

### 다른 사람의 풀이
enumerate를 이용한 묶음 풀이
enumerate(citations, start=1)을 통해 순번과 인용 횟수를 묶어서 튜플로 정리한 뒤 map을 통해 min 연산을 한번에 작동 max로 다시 정하여 답 도출
