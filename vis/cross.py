import pandas as pd
import plotly.express as px
df = px.data.iris()
df['Petal-more-than-1.0'] = (df['petal_width'] > 1.0).astype(int)
print(pd.crosstab(df['petal_length'], df['Petal-more-than-1.0']))
