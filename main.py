import streamlit as st
from PIL import Image

# 🌈 스타일 설정
st.set_page_config(
    page_title="✨ MBTI 진로 추천 ✨",
    page_icon="🧠",
    layout="wide"
)

# 🎉 상단 배너
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4; font-size: 60px;'>🌟 나의 MBTI로 찾는 미래 직업 🌟</h1>
    <p style='text-align: center; font-size: 24px;'>당신의 성격 유형에 맞는 멋진 직업을 지금 바로 찾아보세요! 🧑‍🚀👩‍⚕️👨‍🏫👩‍💻</p>
""", unsafe_allow_html=True)

# 📷 이미지 (최신 버전 반영)
st.image("https://i.imgur.com/JWtF1A5.png", use_container_width=True)

# 🎯 MBTI 목록 및 추천 직업
mbti_jobs = {
    "INTJ": ["전략 컨설턴트 🧠", "AI 엔지니어 🤖", "연구 과학자 🔬"],
    "INFP": ["작가 ✍️", "상담사 🧘‍♀️", "아티스트 🎨"],
    "ENFP": ["마케터 📣", "창업가 🚀", "강연가 🎤"],
    "ESTJ": ["경영 관리자 🏢", "군인 🎖️", "판사 ⚖️"],
    "ISFJ": ["간호사 💉", "초등교사 👩‍🏫", "사서 📚"],
    "ENTP": ["벤처 CEO 💼", "투자자 💰", "크리에이터 📺"],
}

# 🌟 사용자 입력
st.subheader("🔍 당신의 MBTI를 선택하세요:")
selected_mbti = st.selectbox("MBTI 유형을 골라주세요!", list(mbti_jobs.keys()))

# 🎁 추천 결과
if selected_mbti:
    st.markdown(f"""
        <div style='background-color: #ffe4e1; padding: 30px; border-radius: 15px;'>
            <h2 style='color: #c71585;'>🌈 {selected_mbti} 유형에게 어울리는 직업은?</h2>
            <ul style='font-size: 22px;'>
                {''.join(f"<li>{job}</li>" for job in mbti_jobs[selected_mbti])}
            </ul>
            <p style='color: #808080;'>💡 MBTI는 참고용 도구일 뿐, 여러분의 진로는 언제든지 바꿀 수 있어요!</p>
        </div>
    """, unsafe_allow_html=True)

# 🎨 하단 안내 문구
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 18px;'>Made with ❤️ by YourCareerGPT · MBTI 진로 웹앱 v1.0</p>
""", unsafe_allow_html=True)
