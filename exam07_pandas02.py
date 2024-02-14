# -*- coding: utf-8 -*-
"""exam07_pandas02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sblUUjwFWGSW_YAPsd--Wi6nc6XfdR0H
"""

import pandas as pd

pd.set_option('display.max_columns',15)# 가로
pd.set_option('display.max_row',200) # 세로 :자료갯수 200개만을 보여줌.

df=pd.read_csv('./datasets/auto-mpg.csv',names=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name'])
df

df.head(10) # 앞부분 10개를 보여줘

df.tail() # 뒷부분을 보여줌

df.shape

df.info()
# 3   horsepower    398 non-null    object -> 숫자가 아닌 문자와 같은 무언가가 떴다는 의미

""""Nan" 이 나타나는 열은 주로 int, float 이렇게 뜸

"Nan" 이 안나타는 열은 object 타입으로 주로 문자열이나 혼합 데이터 타입을 가지므로 Nan 이 나타내지 않을 수도 있다.  
"""

df.dtypes

df['mpg'].dtypes

df.mpg.dtypes

df.describe()

df.describe().T

df.describe(include='all')
# origin은 2면 일본, 0이면 유럽... 이런식으로 분류해놓은 것

"""row(세로) - unique:

NaN	NaN	NaN	94	NaN	NaN	NaN	NaN	305 ->305개 나있다는 의미는 중복이 많다는 의미
"""

df.count()

unique_value=df['name'].value_counts()
print(type(unique_value))
unique_value

"""자동차 종류들을 나열한 것"""

df['model year'].value_counts() # 각 모델 연도의 등장 횟수가 반환됩니다.

df.mean# 각 열의 평균값이 반환

print(df.mpg.mean)

df.corr # 각 열 간의 상관 계수가 반환

"""cylinders 에서 -1 에서 1의 값을 가짐.
cylinders 과 mpg 가 -1이라고 한다면 10커지면 10배 작아지고
cylinders 과 mpg 가 1이라고 한다면 10배 커지면 10배 커진다는 것을 알 수 있습니다.
cylinders과 마력은 강한 상관관계를 가집니다.
displacement 배기량이 크면 클 수록 연비는 안 좋겠죠.
* 이러한 상관관계를 가지고 연비를 예측할 수 있어.
"""

df.mean

# 연비를 알아보기 위함
mpg_to_kpl = 0.425144
df['kpl'] =df['mpg'] * mpg_to_kpl
df.head(50)
# origin 은 제조국 이름이야.

"""name은 get_dummie화 할 수 없어.

# 이런식으로 column 열을 만들 수 있어
"""

# 연비를 알아보기 위함
mpg_to_kpl2 = 2
df['nice'] =df['cylinders'] * mpg_to_kpl2
df.head(50)
# origin 은 제조국 이름이야.

df['kpl']=df['kpl'].round(2) # 두 자리까지만 반올림해서 나타낼 수도 있다.
df

df['horsepower'].unique()

"""df['horsepower'].unique() 코드는 데이터프레임의 'horsepower' 열에서 중복되지 않는(unique) 값들을 배열(array) 형태로 반환합니다.

array가 나오는 이유:

unique() 메서드는 중복을 제거하고 유일한 값들을 반환합니다.
반환된 값들은 배열(array) 형태로 표현됩니다. 넘파이(Numpy) 라이브러리에서 제공되는 배열 형태를 사용합니다.
?가 나오는 이유:

데이터프레임의 'horsepower' 열에서는 숫자로 표현되어야 하는데, 어떤 이유로 인해 숫자가 아닌 값(문자열 등)이 포함되어 있을 수 있습니다.
이러한 이상한 값들 중에서 자주 보이는 것 중 하나가 '?'입니다. 이는 데이터가 제대로 입력되지 않았거나 누락된 데이터를 나타내기 위해 사용되는 특별한 기호일 수 있습니다.

문자열이 float 보다 크기때문에 string으로 맞춰줌.  '?' 때문에.
"""

import numpy as np

df['horsepower'].replace('?',np.nan, inplace=True)
df.dropna(subset=['horsepower'],axis=0,inplace=True) #
df['horsepower'] =df['horsepower'].astype('float64')
#df.info()
df.corr()

df['origin'].replace({1:'USA',2:'EU',3:'JP'},inplace=True)
print(df['origin'].unique())
print(df['origin'].head(30))
print(df['origin'].value_counts())

"""dtype: object 는 문자열 타입이야."""

df['origin']=df['origin'].astype('category')
print(df['origin'].dtypes)
print(df['origin'])

"""척도의 종류:

https://blog.naver.com/angryking/222366897282

"""

df['origin']=df['origin'].astype('str') # object로 바꾸고 싶으면 str으로 바꿔줘. astype: 타입을 바꿔줘
print(df['origin'].dtypes)
print(df['origin'])

"""df['origin'].dtypes는 'origin' 열의 데이터 타입을 반환합니다. 예를 들어, 만약 'origin' 열이 문자열로 구성되어 있다면, 결과는 object가 될 것이고, 정수형이라면 int64, 부동소수점이라면 float64 등이 될 수 있습니다.

  dtypes는 데이터프레임의 메타데이터 중 하나로, 각 열의 데이터 타입을 나타내는 속성입니다.

## 척도의 종류

서열 척도 (Ordinal Scale):

서열 척도는 데이터를 순서대로 나열할 수 있지만 간격이 일정하지 않습니다.
데이터 간의 상대적인 순서나 우선 순위를 나타냅니다.
예시: 학생들의 성적 순위 (1등, 2등, 3등), 만족도 조사에서 '매우 낮음', '보통', '매우 높음' 등.
등간 척도 (Interval Scale):

등간 척도는 데이터를 순서대로 나열할 수 있고, 간격이 일정합니다. 그러나 절대적인 영점(absolute zero)이 없습니다.
간격은 의미가 있지만 비율은 의미가 없습니다.
예시: 온도 (섭씨 0도는 물이 얼기 시작하는 지점이지만 영점은 없음).
비율 척도 (Ratio Scale):

비율 척도는 등간 척도와 유사하지만, 절대적인 영점이 존재하며 비율이 의미가 있습니다.
0이 완전한 부재를 나타내며, 비율을 계산할 수 있습니다.
예시: 무게, 키, 소득 등.
명목 척도 (Nominal Scale):

명목 척도는 데이터를 분류하는 데 사용되며, 순서나 간격이 없습니다.
단순히 분류를 위한 레이블을 제공합니다.
예시: 성별 (남성, 여성), 혈액형 (A, B, AB, O) 등.
간단히 말하면, 서열 척도는 순서를 나타내고, 등간 척도는 순서와 간격을 나타내며, 비율 척도는 순서, 간격, 비율을 나타내고, 명목 척도는 단순 분류를 위한 것입니다. 이러한 척도의 선택은 분석하려는 데이터의 특성과 목적에 따라 달라집니다.

: 어나더인코드(ordinal encoding)는 데이터를 명목 척도로 인코딩하는 방법 중 하나입니다. 그러나 어나더인코드는 명목 척도에서는 일반적으로 사용되지 않습니다. 명목 척도는 주로 원-핫 인코딩(one-hot encoding)과 같은 방법으로 다루어집니다.
"""

# 명목 척도로 바꿔보겠다.
count, bin_dividers = np.histogram(df['horsepower'],bins=3) # 히스토그램이라고 하는 막대그래프를 그려봄. bins=3 나누고자 하는 갯수.
print(count)
print(bin_dividers)

"""np.histogram(df['horsepower'], bins=3): 'horsepower' 열의 데이터를 기반으로 히스토그램을 생성합니다. bins=3는 히스토그램을 3개의 구간으로 나누라는 의미입니다.

count: 각 구간에 속하는 데이터 포인트의 수를 나타내는 배열입니다. 이 배열은 히스토그램의 각 막대에 해당하는 데이터 포인트의 개수를 순서대로 나타냅니다.
저출력 갯수:257, 보통출력 갯수:103,  고출력 갯수:32


bin_dividers: 히스토그램의 구간 경계를 나타내는 배열입니다. 이 배열은 각 구간의 시작과 끝 값을 포함합니다. 예를 들어, bin_dividers의 첫 번째 원소는 첫 번째 구간의 시작 값이고, 마지막 원소는 마지막 구간의 끝 값입니다.
 ex) 46.         107.33333333 168.66666667 230. 여기에서 46부터 107.333 까지 들어가는 값, 107.333 부터 168.666까지 들어가는 값, 168.666부터 230 까지 들어가는 값.         


결과적으로, count 배열은 각 구간에 속하는 데이터 포인트의 수를 나타내고, bin_dividers 배열은 히스토그램의 각 구간의 경계 값을 나타냅니다. 이를 출력하여 히스토그램의 구조를 확인할 수 있습니다.

[257 103  32]
 저출력, 중간 출력, 고출력
"""

bin_names=['저출력','보통출력','고출력']
df['hp_bin']=pd.cut(x=df['horsepower'],bins=bin_dividers,labels=bin_names,include_lowest=True)
# cut(),cut이라고 하는 함수가 있어. cut을 이용해서 나누면 category 별로해서 나눌 수 있어.
df[['horsepower','hp_bin']].head(30)

df.info()

df1 = df[['horsepower','hp_bin','origin']]
df1

df2 = pd.get_dummies(df1) #  pd.get_dummies()는 이를 각 범주에 대한 더미 변수로 변환하여 새로운 데이터프레임을 생성합니다. 이때, 각 범주에 해당하는 더미 변수는 1(정답이면) 또는 0(틀렸으면)의 값을 가집니다.
# hp_bin_저출력	hp_bin_보통출력	hp_bin_고출력	origin_EU	origin_JP	origin_USA 이런식으로 펼쳐지는 것을 get_dummies라고 해.

df2

df = pd.DataFrame({'c1':['a','a','b','a','b'],'c2':[1,1,1,2,2],'c3':[1,1,2,2,2]}) # pd는 pandas를 의미해
df

"""0 : 초반에니까 중복이 없지 그래서 False

1: a	1	1가 또 나오면서 중복이 있으니까 True

2: 중복 안되니까 False
"""

df_dup=df.duplicated() # duplicated()에서 중복이면 true 아니면 false
df_dup

df_dup=df['c2'].duplicated() # c2 column만 보고 확인한거야.
df_dup

"""ex) 학번의 경우 중복이 있으면 안되잖아. 그럴 경우 학번과 같은 컬럼만 따로 보고 중복을 확인 할 수도 있다."""

df2 = df.drop_duplicates()
df2

"""여기서 인덱스가 " 이빨 빠진 인덱스야"
0,2,3,4 처럼 1이 빠져있지.
"""

df2.info()

df2.iloc[1] # 우리가 정해놓은 인덱스가 아닌 자동으로 정해진 인덱스 기준

df2.loc[2] # 우리가 지정한 인덱스 기준

df2= df2.reset_index() # 인덱스가 0,2,3,4 이니까 이것을 0,1,2,3, 으로 차례대로 순서를 재정의하기 위함.
df2

df2= df2.reset_index(drop=True)
df2

"""df2.reset_index(drop=True,inplace=True)

df2

이런식으로 쳐도 같은 거야~
"""

# 내일은 다시 타이타닉 데이터를 가지고 전처리를 하겠음. pandas를 익히기 위함.