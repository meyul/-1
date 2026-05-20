import streamlit as st
import time

# 1. 웹페이지 기본 설정 (브라우저 탭에 보일 아이콘과 제목)
st.set_page_config(
    page_title="💸 개발자 지갑 심폐소생술", 
    page_icon="🩸", 
    layout="centered"
)

# 2. 아주 크고 어그로 가득한 타이틀과 서브타이틀
st.title('🚨 [긴급] 개발자의 통장을 살려주세요...!')
st.subheader('💰 우리에게 후원하다!!! (본격 영혼 탈탈 프로젝트)')

# 3. 상황 설명 (과장법과 감성 자극)
st.markdown("---")
st.write("📢 **안내 말씀**")
st.write(
    "당신의 소중한 후원은 개발자의 **삼각김밥 속 참치마요 함량**을 결정합니다. "
    "지나가던 길고양이도 눈물 흘릴 이 눈물겨운 프로젝트에 제발 동참해 주세요!"
)

# 4. 후원 금액 선택 (selectbox를 활용한 병맛 옵션들)
donation_option = st.selectbox(
    '💸 후원 금액을 선택해 주세요 (신중하게 결정하세요):',
    (
        '선택 안 함 (개발자 굶기기)',
        '500원 (컵라면 국물 한 입 기부)',
        '1,000원 (삼각김밥 김 코팅 기부)',
        '10,000원 (치킨 조각 한 개 기부)',
        '100,000,000원 (개발자를 소유하기)'
    )
)

# 5. 선택한 금액에 따른 개발자의 눈물겨운 반응 (조건문 분기)
st.markdown("### 🗣️ 개발자의 한마디")
if donation_option == '선택 안 함 (개발자 굶기기)':
    st.warning('⚠️ 뒤에서 개발자의 아주 슬프고 따가운 눈빛이 느껴집니다...')
elif donation_option == '500원 (컵라면 국물 한 입 기부)':
    st.info('🍜 국물만 먹으면 짜지만... 감사합니다! 짭조름한 제 눈물과 섞어 마실게요.')
elif donation_option == '1,000원 (삼각김밥 김 코팅 기부)':
    st.success('🍙 밥알이 흩어지지 않게 꽉 잡아주는 아주 소중한 김을 얹었습니다!')
elif donation_option == '10,000원 (치킨 조각 한 개 기부)':
    st.write('🍗 **대박!** 오늘 밤은 닭 냄새라도 맡을 수 있겠군요! 압도적 감사!')
elif donation_option == '100,000,000원 (개발자를 소유하기)':
    st.error('👑 회장님 모시겠습니다! 이제부터 이 개발자는 평생 회장님 노예입니다. (환불 불가)')

# 6. 한 줄 평 입력 받기
comment = st.text_input("✍️ 개발자에게 한마디 남기기 (팩트 폭행 환영):", placeholder="예: 코딩 똑바로 하세요")

# 7. 기부 완료 버튼 (로딩 바 + 풍선 + 눈 효과)
if st.button('💸 전재산 기부하고 천국 가기 💸'):
    if donation_option == '선택 안 함 (개발자 굶기기)':
        st.error("앗! 후원 금액을 먼저 선택하고 기부 버튼을 눌러주세요! 개발자가 현기증 난단 말이에요 😭")
    else:
        # 영혼이 털리는 기분을 표현하는 로딩 바
        progress_bar = st.progress(0)
        status_text = st.empty()

        for percent_complete in range(100):
            time.sleep(0.01)  # 로딩 속도 조절
            progress_bar.progress(percent_complete + 1)
            status_text.text(f"통장 잔고 털어내는 중... {percent_complete + 1}% 완료")

        # 완료 메시지 및 화려한 파티 타임
        st.success(f'🎉 기부 완료! "{comment}"라는 따뜻한 말씀과 함께 영혼이 성공적으로 탈탈 털렸습니다!')
        
        # Streamlit의 꿀잼 치트키 기능 두 가지 동시 소환!
        st.balloons()  # 화면 아래에서 풍선이 올라옴
        st.snow()      # 하늘에서 눈이 내림
