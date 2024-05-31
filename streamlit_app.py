import streamlit as st
import time

class LoveAdviceApp:
    def __init__(self):
        self.user_info = {}
        self.options = {
            "age": ["20대", "30대", "40대 이상"],
            "interest": ["영화", "책", "운동"]
        }

    def set_user_info(self, info_type, option):
        self.user_info[info_type] = option

    def show_advice(self):
        age = self.user_info.get("age", "미정")
        interest = self.user_info.get("interest", "미정")
        advice = f"당신은 {age}이고, 관심사는 {interest}입니다. 사랑은 언제나 가까이에 있습니다."
        st.info(advice)

    def run(self):
        if "advice_requested" not in st.session_state:
            st.session_state.advice_requested = False
        if "dialogue_shown" not in st.session_state:
            st.session_state.dialogue_shown = False
        if "current_question" not in st.session_state:
            st.session_state.current_question = 0

        if st.session_state.dialogue_shown == False:
            st.markdown('<div style="text-align: center;">나: "하...연애하고 싶다...ㅠㅠ"</div>', unsafe_allow_html=True)
            time.sleep(3)
            st.markdown('<div style="text-align: center;">나: "누가 연애 조언 안해주나...?"</div>', unsafe_allow_html=True)
            time.sleep(3)
            st.markdown('<div style="text-align: center;">슝슝이: "안녕? 난 슝슝이야!"</div>', unsafe_allow_html=True)
            time.sleep(3)
            st.markdown('<div style="text-align: center;">슝슝이: "내가 너의 모솔 탈출을 도와줄게!"</div>', unsafe_allow_html=True)
            time.sleep(3)
            st.markdown('<div style="text-align: center;">슝슝이: "일단 내가 만든 질문에 답을 해봐!"</div>', unsafe_allow_html=True)
            time.sleep(3)
            st.session_state.dialogue_shown = True

        if st.session_state.dialogue_shown and not st.session_state.advice_requested:
            if st.button("연애 조언 받기"):
                st.session_state.advice_requested = True
                st.experimental_rerun()

        if st.session_state.advice_requested:
            if st.session_state.current_question < len(self.options):
                info_type = list(self.options.keys())[st.session_state.current_question]
                options = self.options[info_type]
                choice = st.radio(f"당신의 {info_type}을 선택하세요:", options)
                if st.button("다음"):
                    self.set_user_info(info_type, choice)
                    st.session_state.current_question += 1
                    st.experimental_rerun()
            else:
                self.show_advice()

            if st.button("초기화"):
                self.user_info = {}
                st.session_state.advice_requested = False
                st.session_state.dialogue_shown = False
                st.session_state.current_question = 0
                st.experimental_rerun()

def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.banggooso.com/assets/images/uploadImg/1596642366(M).jpg");
            background-size: 50%;
            background-position: center top;
            background-repeat: no-repeat;
            background-color: white;
        }}
        .center {{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    # Add background image
    add_bg_from_local()

    # Set the app title
    st.markdown('<h1 style="text-align: center;">사랑을 찾아 슝슝~♥</h1>', unsafe_allow_html=True)

    # Run the love advice app
    app = LoveAdviceApp()
    app.run()

if __name__ == "__main__":
    main()
