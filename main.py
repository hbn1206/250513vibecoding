import streamlit as st

# 🌈 페이지 설정
st.set_page_config(
    page_title="✨ MBTI 진로 추천 ✨",
    page_icon="🧠",
    layout="wide"
)

# ❄️ 앱 시작 시 눈 내리는 효과
st.snow()

# 🎉 상단 배너
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4; font-size: 60px;'>🌟 나의 MBTI로 찾는 미래 직업 🌟</h1>
    <p style='text-align: center; font-size: 24px;'>당신의 성격 유형에 맞는 멋진 직업을 지금 바로 찾아보세요! 🧑‍🚀👩‍⚕️👨‍🏫👩‍💻</p>
""", unsafe_allow_html=True)

# 💡 MBTI 진로 데이터
mbti_jobs = {
    "INTJ": ["전략 컨설턴트 🧠", "AI 엔지니어 🤖", "연구 과학자 🔬"],
    "INTP": ["데이터 과학자 📊", "철학자 📚", "게임 개발자 🎮"],
    "ENTJ": ["CEO 💼", "프로젝트 매니저 📈", "변호사 ⚖️"],
    "ENTP": ["벤처 창업가 🚀", "발명가 🛠️", "유튜버 📹"],
    "INFJ": ["상담심리사 🧘", "교사 👩‍🏫", "작가 ✍️"],
    "INFP": ["시인 📝", "예술가 🎨", "사회복지사 🤝"],
    "ENFJ": ["리더십 트레이너 🧑‍🏫", "홍보 전문가 📣", "정치가 🏛️"],
    "ENFP": ["마케터 📈", "공연예술가 🎭", "여행 작가 ✈️"],
    "ISTJ": ["공무원 🏛️", "회계사 📒", "군인 🪖"],
    "ISFJ": ["간호사 💉", "보건 교사 🏥", "도서관 사서 📚"],
    "ESTJ": ["경영 관리자 🏢", "판사 ⚖️", "군 간부 🎖️"],
    "ESFJ": ["유치원 교사 🧒", "행사 기획자 🎪", "영업 매니저 📞"],
    "ISTP": ["기계 엔지니어 🛠️", "파일럿 ✈️", "응급 구조사 🚑"],
    "ISFP": ["플로리스트 🌸", "패션 디자이너 👗", "사진작가 📷"],
    "ESTP": ["기업 컨설턴트 🧑‍💼", "프로 운동선수 ⚽", "이벤트 플래너 🎉"],
    "ESFP": ["연예인 🎤", "메이크업 아티스트 💄", "여행 가이드 🌍"]
}

# 🎯 사용자 선택
st.subheader("🔍 당신의 MBTI를 선택하세요:")
selected_mbti = st.selectbox("MBTI 유형", list(mbti_jobs.keys()), index=0)

# 📢 추천 결과 출력
if selected_mbti:
    # 🎈 추천 결과 축하 효과
    st.balloons()

    st.markdown(f"""
        <div style='background-color: #ffe4e1; padding: 30px; border-radius: 15px;'>
            <h2 style='color: #c71585;'>🌟 {selected_mbti} 유형에게 어울리는 직업은?</h2>
            <ul style='font-size: 22px;'>
                {''.join(f"<li>{job}</li>" for job in mbti_jobs[selected_mbti])}
            </ul>
            <p style='color: #808080;'>💡 MBTI는 당신의 가능성을 탐색하는 도구입니다. 마음에 드는 길을 용기 있게 걸어가세요! 💖</p>
        </div>
    """, unsafe_allow_html=True)

# 🎨 푸터
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 18px;'>Made with ❤️ by <b>MBTI Career Explorer</b> · 버전 1.0</p>
""", unsafe_allow_html=True)
