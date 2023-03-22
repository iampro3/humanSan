# -*- coding:utf-8 -*-
# 0322 part 2
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff

def main():
    st.title("Hello Streamlit World!")

    # color Picker
    color = st.color_picker('색상 선택')
    #st.write(color)

    #matplotlib
    data = np.random.normal(1,1,size=100)
    fig, ax= plt.subplots()
    ax.hist(data, bins=20, color=color) # 컬러 입력 picker 설정
    ax.set_title("Histogram Graph")    

    st.pyplot(fig)

    # plotly chart : 시각화 도구 (javascripts 기반)
    x1 = np.random.randn(200) -2
    x2 = np.random.randn(200)
    x3= np.random.randn(200) + 2

    hist_data = [x1,x2,x3]
    group_labels =['group 1', 'group 2', 'group 3']

    fig = ff.create_distplot(
        hist_data, group_labels,  bin_size=[.1,.25,.5]
    )

    st.plotly_chart(fig, use_container_width=True)


    

    

if __name__== "__main__":
    main()