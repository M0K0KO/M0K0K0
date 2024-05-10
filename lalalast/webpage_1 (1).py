import streamlit as st
import pandas as pd 
import os 
from datetime import date, datetime
from PIL import Image

def save_uploaded_file(directory, file) :

    if not os.path.exists(directory) :
        os.makedirs(directory)

    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())

    return st.success('{} 에 {} 파일이 저장되었습니다.'.format(directory, file.name))


def main():

    st.title('물고기 종류🐟')
    st.markdown("""
    <style>
    h1 {
            color: blue
    }            
    </style>     
                
                
                """,unsafe_allow_html=True)
    menu = ['Image', 'About']

    choice = st.sidebar.selectbox('메뉴', menu )

    if choice == 'Image' :
        st.subheader('물고기 파일 업로드')
        length = st.text_input('생선의 길이를 입력하세요')
        date = st.date_input("생선을 잡은 날짜가 언제인가요?")
        f = open("data.txt", 'w')
        f.write(str(date))
        f.close()
        file = st.file_uploader('물고기 이미지를 업로드하세요', type=['jpg','jpeg','png'])

        if file is not None :
            st.text(file.name)
            st.text(file.size)
            st.text(file.type)

            current_time = datetime.now()
            print(current_time.isoformat().replace(':','_') )
            current_time = current_time.isoformat().replace(':','_')
            print( current_time + '.jpg' )

            file.name = current_time + '.jpg'

            # 바꾼파일명으로, 파일을 서버에 저장한다.
            save_uploaded_file('물고기', file)

            # 파일을 웹 화면에 나오게.
            img = Image.open(file)
            img.save("sample.png")
            st.image(img)

    elif choice == 'About' :
        st.subheader('파일 업로드 프로젝트 입니다.')
        st.text("이 프로그램은 생선의 종류를 맞추고, 금어기를 알려줍니다.")
        st.text("\n")
        st.text("금어기란 연간어획량과 어획물의 크기를 제한하고 자원의 보호와 배양을 목적으로 \n어패류의 산란기나 치어기에 맞추어 설정되는 특정 어패류의 포획을 금지하는 기간입니다.")

if __name__=='__main__' :
    main()