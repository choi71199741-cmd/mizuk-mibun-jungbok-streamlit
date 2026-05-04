import streamlit as st
import random

st.set_page_config(page_title="미적분 퀴즈", page_icon="📘")

st.title("📘 미적분 퀴즈 앱")
st.write("다양한 함수의 도함수를 맞춰보세요!")

# ------------------------
# 문제 생성
# ------------------------
def generate_problem():
    t = random.choice(["exp", "log", "trig", "quotient", "power", "composite"])

    if t == "exp":
        a = random.randint(1, 3)
        question = f"e^({a}x)"
        answer = f"{a}e^({a}x)"

    elif t == "log":
        a = random.randint(1, 5)
        question = f"ln({a}x)"
        answer = f"{a}/({a}x)"

    elif t == "trig":
        func = random.choice(["sin", "cos"])
        a = random.randint(1, 3)

        if func == "sin":
            question = f"sin({a}x)"
            answer = f"{a}cos({a}x)"
        else:
            question = f"cos({a}x)"
            answer = f"-{a}sin({a}x)"

    elif t == "quotient":
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        question = f"(x^{a})/(x^{b})"
        answer = f"({a-b})x^{a-b-1}"

    elif t == "power":
        r = random.choice([0.5, 1.5, 2.5])
        question = f"x^{r}"
        answer = f"{r}x^{r-1}"

    else:
        a = random.randint(1, 3)
        question = f"sin(x^{a})"
        answer = f"{a}x^{a-1}cos(x^{a})"

    return question, answer


# ------------------------
# 선택지 생성
# ------------------------
def generate_choices(correct):
    wrongs = set()

    while len(wrongs) < 3:
        fake = f"{random.randint(1,5)}x^{random.randint(0,3)}"
        if fake != correct:
            wrongs.add(fake)

    choices = list(wrongs) + [correct]
    random.shuffle(choices)
    return choices


# ------------------------
# 힌트
# ------------------------
def give_hint(attempt):
    hints = [
        "💡 기본 미분 공식을 떠올려보세요",
        "💡 체인룰 또는 몫의 미분을 사용하세요",
        "💡 바깥함수 미분 × 안쪽함수 미분",
        "💡 계산을 다시 확인해보세요"
    ]
    return hints[min(attempt-1, len(hints)-1)]


# ------------------------
# 세션 상태
# ------------------------
if "problem" not in st.session_state:
    q, ans = generate_problem()
    st.session_state.problem = q
    st.session_state.answer = ans
    st.session_state.choices = generate_choices(ans)
    st.session_state.attempt = 0


# ------------------------
# 문제 출력 (예쁘게)
# ------------------------
st.latex(f"f(x) = {st.session_state.problem}")

choice = st.radio("정답을 선택하세요:", st.session_state.choices)

if st.button("제출"):
    st.session_state.attempt += 1

    if choice == st.session_state.answer:
        st.success(f"🎉 정답! → {st.session_state.answer}")
    else:
        st.error("❌ 틀렸습니다")
        st.info(give_hint(st.session_state.attempt))


if st.button("다음 문제"):
    q, ans = generate_problem()
    st.session_state.problem = q
    st.session_state.answer = ans
    st.session_state.choices = generate_choices(ans)
    st.session_state.attempt = 0
