import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="경영 DNA 테스트",
    page_icon="📊",
    layout="centered"
)

# -----------------------------
# 질문 데이터
# -----------------------------
questions = [

    {
        "question": "Q1. 새로운 아이디어가 떠오르면?",
        "a": "일단 실행부터 해본다",
        "b": "현실성과 데이터를 먼저 본다",
        "type": "CA"
    },

    {
        "question": "Q2. 팀플에서 나는 보통?",
        "a": "리더 역할을 맡는다",
        "b": "조율자 역할을 맡는다",
        "type": "LT"
    },

    {
        "question": "Q3. 사업 아이템을 고른다면?",
        "a": "위험해도 혁신적인 것",
        "b": "안정적으로 오래 갈 것",
        "type": "CS"
    },

    {
        "question": "Q4. 회의 분위기가 답답하면?",
        "a": "방향을 바꾸자고 한다",
        "b": "모두 의견을 듣는다",
        "type": "LT"
    },

    {
        "question": "Q5. 내가 더 중요하게 생각하는 건?",
        "a": "창의성과 가능성",
        "b": "효율성과 결과",
        "type": "CA"
    },

    {
        "question": "Q6. 친구들이 나를 보는 느낌은?",
        "a": "추진력 있다",
        "b": "배려심 있다",
        "type": "LT"
    },

    {
        "question": "Q7. 기업 운영에서 가장 중요한 건?",
        "a": "시장 혁신",
        "b": "지속 가능한 성장",
        "type": "CS"
    },

    {
        "question": "Q8. 발표를 맡게 되면?",
        "a": "즉흥적으로 분위기를 이끈다",
        "b": "준비한 흐름대로 진행한다",
        "type": "LT"
    },

    {
        "question": "Q9. 실패를 겪으면?",
        "a": "다시 더 크게 도전한다",
        "b": "원인을 분석한다",
        "type": "CA"
    },

    {
        "question": "Q10. 조직 분위기는?",
        "a": "빠르고 자유로운 게 좋다",
        "b": "안정적이고 체계적인 게 좋다",
        "type": "CS"
    },

    {
        "question": "Q11. 새 기술이 나오면?",
        "a": "바로 써본다",
        "b": "검증된 후 사용한다",
        "type": "CA"
    },

    {
        "question": "Q12. 내 미래 목표는?",
        "a": "세상을 바꾸는 것",
        "b": "오래 살아남는 것",
        "type": "CS"
    }
]

# -----------------------------
# 결과 데이터
# -----------------------------
results = {

    "CLC": {
        "title": "혁신가형",
        "person": "Steve Jobs",
        "image": "images/jobs.jpg",

        "desc": """
당신은 새로운 아이디어와 창의성을 중요하게 생각하는 혁신가형입니다.

기존 방식에 얽매이기보다 새로운 흐름을 만들고,
사람들에게 강한 인상을 남기는 능력이 있습니다.
""",

        "famous": """
애플(Apple)의 공동 창업자.

아이폰·아이패드·맥북 등 혁신적인 제품을 통해
전 세계 IT 시장과 디자인 트렌드를 바꾼 인물입니다.
""",

        "strength": [
            "창의적 아이디어",
            "강한 비전 제시",
            "브랜드 감각",
            "트렌드 선도"
        ],

        "job": [
            "마케팅",
            "브랜딩",
            "스타트업",
            "디자인경영"
        ],

        "quote": "Innovation distinguishes between a leader and a follower."
    },

    "CLS": {
        "title": "비전리더형",
        "person": "Howard Schultz",
        "image": "images/schultz.jpg",

        "desc": """
당신은 사람 중심의 리더십을 가진 비전리더형입니다.
""",

        "famous": """
스타벅스(Starbucks)를 세계적인 브랜드로 성장시킨 경영자.
""",

        "strength": [
            "공감 능력",
            "조직 관리",
            "소통 능력"
        ],

        "job": [
            "인사관리",
            "브랜드경영",
            "서비스경영"
        ],

        "quote": "Success is best when it’s shared."
    },

    "CTC": {
        "title": "소통혁신형",
        "person": "Elon Musk",
        "image": "images/musk.jpg",

        "desc": """
당신은 도전과 혁신을 즐기는 타입입니다.
""",

        "famous": """
테슬라(Tesla), 스페이스X(SpaceX)의 CEO.
""",

        "strength": [
            "실행력",
            "도전 정신",
            "미래지향적 사고"
        ],

        "job": [
            "창업",
            "IT비즈니스",
            "전략기획"
        ],

        "quote": "When something is important enough, you do it."
    },

    "CTS": {
        "title": "공감리더형",
        "person": "Oprah Winfrey",
        "image": "images/oprah.jpg",

        "desc": """
당신은 뛰어난 공감 능력과 소통 능력을 가진 타입입니다.
""",

        "famous": """
세계적인 방송인 겸 미디어 사업가.
""",

        "strength": [
            "공감 능력",
            "영향력",
            "커뮤니케이션"
        ],

        "job": [
            "광고홍보",
            "마케팅",
            "미디어경영"
        ],

        "quote": "Turn your wounds into wisdom."
    },

    "ALC": {
        "title": "전략가형",
        "person": "Jeff Bezos",
        "image": "images/bezos.jpg",

        "desc": """
당신은 효율과 전략을 중요하게 생각하는 타입입니다.
""",

        "famous": """
아마존(Amazon)의 창업자.
""",

        "strength": [
            "전략적 사고",
            "효율성",
            "데이터 분석"
        ],

        "job": [
            "SCM",
            "생산관리",
            "경영전략"
        ],

        "quote": "Your margin is my opportunity."
    },

    "ALS": {
        "title": "투자분석형",
        "person": "Warren Buffett",
        "image": "images/buffett.jpg",

        "desc": """
당신은 신중하고 안정적인 성향의 분석형입니다.
""",

        "famous": """
세계적인 투자자이자 버크셔 해서웨이의 회장.
""",

        "strength": [
            "분석력",
            "안정성",
            "리스크 관리"
        ],

        "job": [
            "재무관리",
            "회계",
            "금융"
        ],

        "quote": "Risk comes from not knowing what you're doing."
    },

    "ATC": {
        "title": "디지털개척형",
        "person": "Mark Zuckerberg",
        "image": "images/zuck.jpg",

        "desc": """
당신은 기술과 디지털 환경에 강한 타입입니다.
""",

        "famous": """
메타(Meta)의 창업자.
""",

        "strength": [
            "디지털 감각",
            "빠른 실행",
            "성장 중심 사고"
        ],

        "job": [
            "IT창업",
            "서비스기획",
            "플랫폼비즈니스"
        ],

        "quote": "The biggest risk is not taking any risk."
    },

    "ATS": {
        "title": "협상전문가형",
        "person": "Jack Ma",
        "image": "images/jackma.jpg",

        "desc": """
당신은 뛰어난 설득력과 소통 능력을 가진 타입입니다.
""",

        "famous": """
알리바바(Alibaba)의 창업자.
""",

        "strength": [
            "협상 능력",
            "영업 능력",
            "관계 형성"
        ],

        "job": [
            "국제경영",
            "영업관리",
            "무역"
        ],

        "quote": "Never give up."
    }
}

# -----------------------------
# 세션 상태
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

# -----------------------------
# 메인 화면
# -----------------------------
st.title("📊 경영 DNA 테스트")
st.subheader("나와 가장 닮은 기업가는 누구일까?")

progress = st.session_state.page / len(questions)
st.progress(progress)

# -----------------------------
# 질문 화면
# -----------------------------
if st.session_state.page < len(questions):

    q = questions[st.session_state.page]

    st.write(f"## {q['question']}")

    answer = st.radio(
        "답변 선택",
        [q["a"], q["b"]],
        key=st.session_state.page
    )

    if st.button("다음 ➡️"):

        st.session_state.answers.append({
            "answer": answer,
            "type": q["type"],
            "a": q["a"]
        })

        st.session_state.page += 1
        st.rerun()

# -----------------------------
# 결과 계산
# -----------------------------
else:

    creative = 0
    analytic = 0

    leader = 0
    teamwork = 0

    challenge = 0
    stable = 0

    for item in st.session_state.answers:

        if item["type"] == "CA":

            if item["answer"] == item["a"]:
                creative += 1
            else:
                analytic += 1

        elif item["type"] == "LT":

            if item["answer"] == item["a"]:
                leader += 1
            else:
                teamwork += 1

        elif item["type"] == "CS":

            if item["answer"] == item["a"]:
                challenge += 1
            else:
                stable += 1

    result = ""

    if creative >= analytic:
        result += "C"
    else:
        result += "A"

    if leader >= teamwork:
        result += "L"
    else:
        result += "T"

    if challenge >= stable:
        result += "C"
    else:
        result += "S"

    final = results[result]

    # -----------------------------
    # 결과 출력
    # -----------------------------
    st.balloons()

    st.success(f"당신의 유형은 '{final['title']}' 입니다!")

    st.image(final["image"], width=320)

    st.header(final["title"])
    st.subheader(final["person"])

    st.write("## 👤 대표 기업가 소개")
    st.write(final["famous"])

    st.write("---")

    st.write("## 📊 당신의 성향 분석")
    st.write(final["desc"])

    st.write("---")

    st.write("## 💡 당신의 강점")

    for s in final["strength"]:
        st.write(f"✔ {s}")

    st.write("---")

    st.write("## 🎯 추천 분야")

    for j in final["job"]:
        st.write(f"📌 {j}")

    st.write("---")

    st.write("## 🗣 대표 명언")
    st.info(final["quote"])

    st.write("---")

    st.write("## 📈 성향 점수")

    st.write(f"창의성: {creative}")
    st.write(f"분석력: {analytic}")

    st.write(f"리더십: {leader}")
    st.write(f"협업성: {teamwork}")

    st.write(f"도전성: {challenge}")
    st.write(f"안정성: {stable}")

    st.write("---")

    st.write(f"### 🔍 결과 코드: {result}")

    # 다시하기
    if st.button("🔄 다시 테스트하기"):

        st.session_state.page = 0
        st.session_state.answers = []

        st.rerun()

        