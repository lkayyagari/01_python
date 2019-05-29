import matplotlib.pyplot as plt
%matplotlib inline

list1.append(x)
list1.extend(x)
list1.remove(x)
list1.pop(indexx)

df = pd.DataFrame()
df = pd.read_csv('file.csv',na_values=['n/a','.','--'])

df.head()
list(d.columns.values)
df.dtypes
df.info()
df.shape

df.columns = [x.upper() for x in df.columns]

df.iloc[r,c] 
df[df['x]>50]
df[df['x'].isin(['B','G',])]
df.select_dtypes(include=['object']).columns
df[df['x]==50][['y','z']]
df1 = df[['a','b'','c']]

df.drop('col1',axis=1,inplace=True)
df1 = df.reset_index()
df['index'] = df.index()

df['x].unique()
df['x'].value_counts()
df.isnull().sum()

df.fillna(0,inplace=True)
df.fillna(df.mean(),inplace=True)
df.replace(dictx)
df.replace([1,2,3],['a','b','c']

df['y'] = np.where(df['x'==0,1,0) #1 for true, 0 for false

df['xyz'] = pd.qcut(df['x'],20,labels=None,duplicates='drop')
df['xyz'] = pd.qcut(df['x'],20,labels=False,duplicates='drop')

df['date'] = pd.to_datetime(df['date'], format = '%d/%b/%Y:%H:%M:%S + 0000', utc=True)

df.groupby('var1')['var2'].sum()
df.groupby('var1')['var2'].mean().plot(kind='bar')
df.groupby('var1')['var2'].agg(['count','min',max'])
df.groupby('var1')[['var2','var3']].agg({'var2':'mean','var3':sum})

str.find(sub,start,end) #-1 if sub is not found
print('abc' + 'def' + "{0:8.2%}".format(iv)) 
