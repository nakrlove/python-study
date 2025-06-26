import pandas as pd



# 문제 
# 1)아래와 같이 데이터프레임을 만들어 보세요
#    이름  국어  영어
# 0  철수  90  85
# 1  영희  80  95
# 2  민수  70  75
df = pd.DataFrame([['철수',90,85],['영희',80,95],['민수',70,75]] ,  columns =['이름','국어','영어'])
df


# 2)국어,영어의 평균을 구하여 '평균' 칼럼을 추가해 주세요
df["평균"] = (df["국어"]+df["영어"])/2

df["평균"] = df[['국어', '영어']].mean(axis=1)
df

# df.sum(axis=1)

# 2)국어가 90점 이상이면 'A', 80점 이상이면 'B', 나머지는  'C'로 등급을 매기는 새로운 칼럼
#'국어등급'을 추가해 주세요
# 방법 1
import numpy as np
df['국어등급'] = np.where(df['국어'] >= 90 , 'A',np.where(df['국어'] >= 80 , 'B','C'))
df


# 방법 2
def jumsu(x):
    return "A" if x >= 90 else "B" if x >= 80 else "C"


df['국어'].apply(jumsu)           
df['국어'].map(jumsu)        
df[['국어','영어']].map(jumsu)  

# 방법 3
# pd.cut 
pd.cut(df['국어'],bins=[80,90])
df['등급'] = pd.cut(df['국어'],bins=[0,80,90,100],  labels=['A','B','C'] ,right=False)



import seaborn as sns
mpg = sns.load_dataset("mpg")
mpg.info()

mpg.groupby('origin').mean() #문자값 칼럼때문에 에러 발생함 
mpg.groupby('origin').iloc[:,:6] # 에러가 발생함 
mpg.groupby('origin')[['mpg','cylinders','displacement']].mean()
mpg.groupby('origin')[['mpg','cylinders','displacement']].sum()
mpg.groupby('origin').sum()
mpg.groupby('origin').sum()[['mpg','cylinders','displacement']]

mpg[['mpg','cylinders','displacement']].groupby('origin').sum() #  origin컬럼이 없어서 에러가 남


mpg.groupby('origin')[['mpg','cylinders','displacement']].apply(np.sum,axis=0)
mpg.groupby('origin')[['mpg','cylinders','displacement']].agg(np.sum,axis=0)



# 판다스 입문 책 256,257 page 참조
def test(x):
    result = x.sum()/len(x)
    return result

mpg.groupby('origin')[['mpg','cylinders','displacement']].agg(test)
