# 표지 지시문 모음 — 산업재해 패널 데이터를 활용한 머신러닝 모델 (재활 서비스 예측 연구실)
표지 7장(목차 1 + 장 6)을 Genspark 등 이미지 생성 도구에 그대로 붙여 넣는 지시문입니다. **목차 표지(00)를 먼저 받아** 그림체를 확인한 뒤, 나머지 요청에 그 그림을 참고 이미지로 함께 올립니다.

| 공통 | 내용 |
|---|---|
| 판 | L (16:9, 가로 1920 이상) → 빌드 1600×900 WebP |
| 저장 이름 | `img/cover_00.webp` ~ `img/cover_06.webp` (페이지가 이 이름을 자동으로 찾아 대체 표지 대신 보여 줌) |
| 참고 이미지 | 네 캐릭터 기본 그림 4장 (GitHub `adminmrobo/fruitfly-lab-expressions`) |
| 금지 | 글자·숫자·물음표·로고, 하얀 둥근 로봇(Money-Robo), 실존 인물·기관 로고, 다친 몸·피·병원 침대 같은 고통 묘사 |
| 배경 | 낮의 연구실 (흰 벽, 큰 창, 자연광) |
| 미공개 X1~X3 · 인턴 | 표지에는 넣지 않음 (본문에서만 등장) |

## 받은 뒤 처리
1. PNG/JPG를 1600×900 WebP(220KB 이하)로 바꿔 `img/cover_NN.webp`로 저장
2. 같은 그림을 3:2로 잘라 `img/thumb_NN.webp`(카탈로그 썸네일), 1200×630으로 잘라 `img/og_NN.webp`(공유 미리보기)
3. `cover_manifest.json`의 해당 항목 `status`를 `ok`로

---

## cover_00 · 목차 · 산업재해 패널 데이터를 활용한 머신러닝 모델

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_00 · L (16:9) |
| 장소 | 연구실 큰 탁자 위에 펼친 설문지 묶음과 세 갈래 길 표지판 |
| 주제 은유 | 설문지 묶음에서 빛나는 작은 카드 몇 장(소수의 이용자)이 떠올라 세 개의 문(재활·직업·사회)으로 향함 |
| 네 캐릭터 포즈 | 박사 standing at the back center, one hand presenting the glowing cards / 조수 beside the table, holding a clipboard, smiling / 초파리 on the left facing right, holding a magnifying glass over a pile of papers / 주판봇 on the right facing left, abacus raised, excited by a tall bar chart |
| 대체 글 (alt) | 네 캐릭터가 설문지 더미에서 떠오른 빛나는 카드 몇 장과 그 뒤의 세 문을 바라보는 낮의 연구실 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a bright daytime lab. A long lab table covered with neat stacks of blank survey sheets; a few small glowing blank cards float up from the stack toward three plain doorways in the background (three kinds of rehabilitation services).
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center, one hand presenting the glowing cards;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, beside the table, holding a clipboard, smiling;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, holding a magnifying glass over a pile of papers;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, abacus raised, excited by a tall bar chart.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple.
Mood: curious, warm, friendly rivalry. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no injuries, no blood, no hospital beds, no real brands or real products.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_01 · 1장 · 왜 재활 서비스 이용을 예측하나

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_01 · L (16:9) |
| 장소 | 두 개의 작업대: 왼쪽은 규칙 카드, 오른쪽은 예시 카드 더미 |
| 주제 은유 | 왼쪽 작업대에는 손으로 쓴 규칙 카드 한 장, 오른쪽 작업대에는 예시 카드가 쌓이고 저울이 스스로 기울어짐 (규칙 vs 학습) |
| 네 캐릭터 포즈 | 박사 standing between the two workbenches, arms open as if presenting two choices / 조수 at the right workbench, sorting example cards into two trays / 초파리 on the left facing right, tapping the single rule card thoughtfully / 주판봇 on the right facing left, pointing the abacus at the self-tilting scale |
| 대체 글 (alt) | 규칙 카드 한 장과 예시 카드 더미가 놓인 두 작업대 사이의 네 캐릭터 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a bright daytime lab. Two workbenches side by side: the left one holds a single blank handwritten-style rule card on a stand; the right one holds a big stack of blank example cards and a small balance scale tilting by itself.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing between the two workbenches, arms open as if presenting two choices;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the right workbench, sorting example cards into two trays;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, tapping the single rule card thoughtfully;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, pointing the abacus at the self-tilting scale.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple.
Mood: curious, warm, friendly rivalry. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no injuries, no blood, no hospital beds, no real brands or real products.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_02 · 2장 · 데이터 읽기

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_02 · L (16:9) |
| 장소 | 벽 가득한 칸막이 서랍장 (데이터 열) |
| 주제 은유 | 서랍장의 서랍 몇 개가 열려 있고, 그중 하나에 빈 칸이 많은 서랍(결측값), 두 개의 큰 물방울 모양 막대(이용률이 다른 두 무리) |
| 네 캐릭터 포즈 | 박사 at the center, pulling out one drawer to show / 조수 kneeling, counting small tokens into two bowls of very different sizes / 초파리 on the left facing right, peering into a nearly empty drawer with a magnifying glass / 주판봇 on the right facing left, abacus raised, reading numbers off the drawers |
| 대체 글 (alt) | 많은 서랍이 달린 벽장 앞에서 서랍을 열어 보고 토큰을 두 그릇에 세는 네 캐릭터 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a bright daytime lab. A tall wall cabinet of many small labeled-less drawers; several drawers are open, one is almost empty. On the floor two bowls of tokens, one big and full, one small.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the center, pulling out one drawer to show;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, kneeling, counting small tokens into two bowls of very different sizes;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, peering into a nearly empty drawer with a magnifying glass;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, abacus raised, reading numbers off the drawers.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple.
Mood: curious, warm, friendly rivalry. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no injuries, no blood, no hospital beds, no real brands or real products.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_03 · 3장 · 세 가지 분류 모델

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_03 · L (16:9) |
| 장소 | 세 개의 실험 구역: 점 무리와 원, S자 곡선 미끄럼틀, 갈림길 나무 모형 |
| 주제 은유 | 왼쪽 바닥의 색 점과 점선 원(이웃), 가운데 S자 미끄럼틀(시그모이드), 오른쪽 예/아니오 갈림길이 있는 작은 나무 모형 |
| 네 캐릭터 포즈 | 박사 at the center behind the S-shaped slide, presenting all three stations / 조수 at the tree model, moving a small token down a branch / 초파리 on the left facing right, standing inside the dotted circle among colored dots / 주판봇 on the right facing left, sliding a bead down the S-shaped slide |
| 대체 글 (alt) | 점 무리·S자 미끄럼틀·갈림길 나무 모형의 세 실험 구역에 흩어진 네 캐릭터 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a bright daytime lab. Three small stations in one lab: on the left colored dots on the floor with a dashed circle around a black dot; in the middle a playground-like S-shaped slide; on the right a tabletop decision-tree model with branching wooden paths and small boxes at the ends.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the center behind the S-shaped slide, presenting all three stations;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the tree model, moving a small token down a branch;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, standing inside the dotted circle among colored dots;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, sliding a bead down the S-shaped slide.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple.
Mood: curious, warm, friendly rivalry. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no injuries, no blood, no hospital beds, no real brands or real products.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_04 · 4장 · 성적표 읽기

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_04 · L (16:9) |
| 장소 | 2×2 칸의 커다란 성적표 보드 |
| 주제 은유 | 칸 넷 중 한 칸만 크게 빛나고, 다른 칸(놓침)은 빨간 테두리로 비어 있음; 큰 숫자 대신 막대 두 개(정확도는 높고 찾은 비율은 낮음) |
| 네 캐릭터 포즈 | 박사 in front of the board, pointing at the red-edged cell / 조수 holding a clipboard, comparing two bars / 초파리 on the left facing right, frowning at the shining cell with a magnifying glass / 주판봇 on the right facing left, cheering at the tall bar with the abacus |
| 대체 글 (alt) | 네 칸 성적표 보드와 높이가 다른 두 막대 앞의 네 캐릭터 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a bright daytime lab. A large wall board divided into four equal cells (two green, one amber, one red-edged and empty); next to it two vertical bars, one very tall and one very short.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, in front of the board, pointing at the red-edged cell;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, holding a clipboard, comparing two bars;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, frowning at the shining cell with a magnifying glass;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, cheering at the tall bar with the abacus.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple.
Mood: curious, warm, friendly rivalry. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no injuries, no blood, no hospital beds, no real brands or real products.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_05 · 5장 · 불균형 데이터와 보완

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_05 · L (16:9) |
| 장소 | 기울어진 커다란 시소 저울 |
| 주제 은유 | 한쪽에 회색 공이 수북하고 반대쪽에 초록 공 두세 개; 초록 쪽에 추를 올리거나 점선 공을 더해 균형을 맞추려 함 |
| 네 캐릭터 포즈 | 박사 at the pivot, steadying the seesaw with one hand / 조수 placing a small weight on the green side / 초파리 on the left facing right, adding dotted outline balls between green balls / 주판봇 on the right facing left, trying to copy-paste identical green balls with the abacus |
| 대체 글 (alt) | 회색 공이 수북한 쪽과 초록 공 몇 개뿐인 쪽으로 기운 시소를 맞추려는 네 캐릭터 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a bright daytime lab. A big seesaw scale: one side piled high with gray balls, the other side with only two or three green balls; dashed-outline balls appear between the green ones.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the pivot, steadying the seesaw with one hand;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, placing a small weight on the green side;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, adding dotted outline balls between green balls;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, trying to copy-paste identical green balls with the abacus.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple.
Mood: curious, warm, friendly rivalry. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no injuries, no blood, no hospital beds, no real brands or real products.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_06 · 6장 · 직접 해 보기 · 현장에 옮기기

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_06 · L (16:9) |
| 장소 | 노트북 화면과 상담 창구 책상 |
| 주제 은유 | 노트북 화면에 빈 코드 줄(글자 없는 색 막대), 옆 상담 책상에 순서대로 놓인 빈 명함 카드와 전화기 |
| 네 캐릭터 포즈 | 박사 at the counter, handing over an ordered stack of blank cards / 조수 typing on the laptop, smiling / 초파리 on the left facing right, checking the laptop screen closely / 주판봇 on the right facing left, calculating with the abacus next to the phone |
| 대체 글 (alt) | 노트북과 상담 창구 책상 사이에서 순서대로 놓인 카드를 건네는 네 캐릭터 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a bright daytime lab. A laptop showing colored blank code lines (no characters) next to a friendly counseling desk with a phone and a neat ordered row of blank name cards.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the counter, handing over an ordered stack of blank cards;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, typing on the laptop, smiling;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, checking the laptop screen closely;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, calculating with the abacus next to the phone.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple.
Mood: curious, warm, friendly rivalry. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no injuries, no blood, no hospital beds, no real brands or real products.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`
