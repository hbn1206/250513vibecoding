import streamlit as st
import pandas as pd
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Initialize session state for student data
if 'student_data' not in st.session_state:
    st.session_state.student_data = [
        {"name": "지민", "interest": "국민연금의 구조"},
        {"name": "서연", "interest": "연금 수령 시기와 총액 비교"},
        {"name": "현우", "interest": "연금 투자 포트폴리오"},
        {"name": "하늘", "interest": "세금과 연금 수령 시 이점"},
        {"name": "민준", "interest": "국민연금의 지속 가능성"},
        {"name": "수빈", "interest": "국민연금 개혁 방안"},
        {"name": "윤서", "interest": "연금 수령 시기 전략"},
        {"name": "도윤", "interest": "연금 투자 수익률 분석"},
        {"name": "채원", "interest": "세계 연금제도 비교"},
        {"name": "정우", "interest": "연금 소득 과세 방식"}
    ]

# 제목
st.title("💸✨ 연금기반 경제수학 수업 🌟 모둠 구성기 🎓🧠")
st.markdown("""
#### 💁‍♀️ 학생의 관심 주제를 바탕으로 찰떡궁합 팀을 추천해줘요! ✨
""")

# 입력창
name = st.text_input("👤 이름을 입력해주세요:")
interest = st.text_input("💡 연금 관련 관심 주제 키워드를 적어주세요 (예: 국민연금, 수령 시기, 투자전략 등):")

# 발표 주제 추천 리스트 (예시)
topic_recommendations = {
    "국민연금": ["국민연금의 구조 분석", "국민연금의 지속 가능성 평가"],
    "수령 시기": ["수령 시기에 따른 연금 총액 비교", "연금 수령 전략 최적화"],
    "투자전략": ["연금 투자 포트폴리오 설계", "리스크 최소화 투자전략"],
    "세금": ["연금 소득에 대한 과세 분석", "세제 혜택을 극대화하는 연금 운용"],
    "연금제도 비교": ["세계 각국의 연금제도 비교", "한국 연금제도의 특성과 문제점"]
}

# 유사도 분석 함수
def assign_groups(student_data):
    names = [x['name'] for x in student_data]
    keywords = [x['interest'] for x in student_data]

    tfidf = TfidfVectorizer().fit_transform(keywords)
    sim_matrix = cosine_similarity(tfidf)

    assigned = set()
    groups = []

    for i in range(len(names)):
        if i in assigned:
            continue
        group = [i]
        assigned.add(i)
        sims = list(enumerate(sim_matrix[i]))
        sims = sorted(sims, key=lambda x: x[1], reverse=True)
        for j, score in sims:
            if j != i and j not in assigned and len(group) < 5:
                group.append(j)
                assigned.add(j)
        groups.append(group)
    return groups

# 주제 통합 요약 함수
def summarize_topics(topics):
    if not topics:
        return "(요약 없음)"
    keywords = [word for t in topics for word in t.split() if len(word) > 1]
    freq = pd.Series(keywords).value_counts().head(3).index.tolist()
    return " / ".join(freq) + " 관련 주제"

# 제출 처리
if st.button("✨ 입력하고 팀 구성 보기!"):
    if name and interest:
        updated = False
        for student in st.session_state.student_data:
            if student['name'] == name:
                student['interest'] = interest
                updated = True
                st.info(f"🔁 '{name}'님의 관심 주제가 업데이트되었어요!")
                break
        if not updated:
            st.session_state.student_data.append({"name": name, "interest": interest})
            st.success("✅ 입력 완료! 멋진 팀 구성을 준비 중이에요...")
            st.balloons()

        # 발표 주제 추천
        st.markdown("---")
        st.subheader("📚 추천 발표 주제")
        for key in topic_recommendations:
            if key in interest:
                for topic in topic_recommendations[key]:
                    st.markdown(f"🎤 **{topic}**")

        # 모둠 구성
        groups = assign_groups(st.session_state.student_data)
        st.markdown("---")
        st.subheader("👥 현재까지의 모둠 구성")

        # 모둠표 만들기
        group_dict = {}
        for idx, group in enumerate(groups, 1):
            group_name = f"모둠 {idx}"
            summary = summarize_topics([st.session_state.student_data[i]['interest'] for i in group])
            group_dict[group_name + f" ({summary})"] = [f"{st.session_state.student_data[i]['name']} - {st.session_state.student_data[i]['interest']}" for i in group]

        max_len = max(len(members) for members in group_dict.values())
        for key in group_dict:
            while len(group_dict[key]) < max_len:
                group_dict[key].append("")

        df = pd.DataFrame(group_dict)
        st.dataframe(df)
        st.snow()
    else:
        st.error("⚠️ 이름과 관심 주제를 모두 입력해주세요!")

# 저장된 정보 보기
if st.checkbox("📄 누적된 입력 데이터 보기"):
    st.dataframe(pd.DataFrame(st.session_state.student_data))
