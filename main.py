import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#       columns = ['lat', 'lon'])

# st.dataframe(df, width = 300, height = 200) ##またはst.writeで可能だが引数指定できない

# st.dataframe(df.style.highlight_max(axis = 0), width = 300, height = 200)

##staticな表なら
# st.table(df)

# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)

# st.map(df)

# st.write('display image')

# if st.checkbox('Show Image'):
#     img = Image.open('富士山.jpg')
#     st.image(img, caption = 'Mt.Fuji', width = 'content')

# option = st.selectbox(
#     'あなたがすきな数字を教えて',
#     list(range(1,11))
# )

# st.write('あなたの好きな数字は', option, 'です')

# st.write('Interactive widgets')
# st.sidebar.write('Sidebar Widget')
# hobby = st.sidebar.text_input('あなたの趣味を教えて')
# condition = st.sidebar.slider('あなたの今の調子は?', 0, 100, 50)


# st.write('あなたの趣味:', hobby)
# st.write('あなたの今の調子は', condition, '%ですね')


#2カラムにする

# left, right = st.columns(2)

# left.write('Sidebar Widget')
# hobby = left.text_input('あなたの趣味を教えて')
# condition = left.slider('あなたの今の調子は?', 0, 100, 50)


# right.write(f'あなたの趣味:{hobby}')
# right.write(f'あなたの今の調子は{condition}%ですね')


#プログレスバー
st.write('プログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!'

expander1 = st.expander('注文1')
expander1.write('注文1の内容')
expander2 = st.expander('注文2')
expander2.write('注文2の内容')
expander3 = st.expander('注文3')
expander3.write('注文3の内容')
