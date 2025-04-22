import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import plotly.io as pio
pio.renderers.default = "browser"  

# Load the Iris dataset
df = px.data.iris()

# Selecting only numerical features for PCA
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
X = df[features]

# Standardizing the data (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA (reduce to 2 components for visualization)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Create a new DataFrame with PCA results
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['species'] = df['species']  # Keep species for visualization

# Visualizing the PCA results
fig = px.scatter(df_pca, x='PC1', y='PC2', color='species', 
                 title='PCA of Iris Dataset',
                 labels={'PC1': 'Principal Component 1', 'PC2': 'Principal Component 2'})
fig.show()
