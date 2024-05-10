import streamlit as st
import pandas as pd 
import os 
from datetime import date, datetime
from PIL import Image

f = open("data.txt", 'r')
name = f.readline()
dates = f.readline()
leng = f.readline()
f.close()

def save_uploaded_file(directory, file) :

    if not os.path.exists(directory) :
        os.makedirs(directory)

    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())

    return st.success('{} 에 {} 파일이 저장되었습니다.'.format(directory, file.name))


def main():
    st.title('물고기 설명🐟')
    st.markdown("""
    <style>
    h1 {
            color: blue
    }            
    </style>     
                
                
                """,unsafe_allow_html=True)
    
    st.text(name)
    st.text(dates)
    st.text(leng)
    


if __name__=='__main__' :
    main()