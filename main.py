from msilib.schema import Condition
from optparse import Option
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit　超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df)

st.dataframe(df.style.highlight_max(axis=0), width=150, height=150)

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import munpy as np
import pandas as pd
```
"""

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

st.write('Display Image')

img = Image.open('sample.png')
st.image(img, caption='盾women', use_column_width=True)

if st.checkbox('Show Image'):
    img = Image.open('sample.png')
    st.image(img, caption='盾women', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)
'あなたの好きな数字は', option, 'です。'

st.write('Interactive Widgets')
# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は', text, 'です。'
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション', condition


# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味は', text
# 'コンディション', condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１の回答')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２の回答')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ２の回答')

st.write('プログレスバー')
'Start!!'

latest_interation =st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'