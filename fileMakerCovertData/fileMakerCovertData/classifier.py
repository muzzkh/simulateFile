import pandas as pd
import json
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
# Load JSON data from file
with open("./normal.json", 'r') as file:
    data = json.load(file)

# Convert JSON to a format suitable for pandas
formatted_data = []
for item in data:
    row = {**item['access'], 'filepath': item['filepath']}
    formatted_data.append(row)

# Create a pandas DataFrame
df = pd.DataFrame(formatted_data)
columns_order = ['filepath', 'CREATE', 'MODIFY', 'DELETE']
df = df.reindex(columns=columns_order)
df.fillna(0,inplace=True)
print(df)
features = df[['CREATE', 'MODIFY', 'DELETE']]

# Normalize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply K-means clustering
# The choice of 'n_clusters' depends on your specific requirements
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(scaled_features)

# Add cluster labels to your original DataFrame
df['cluster'] = kmeans.labels_
grouped_df = df.groupby('cluster')

# Iterate over each group
for cluster_label, group in grouped_df:
    print(f"Cluster {cluster_label}:")
    print(group)


# Assuming you're using 'CREATE', 'MODIFY', 'DELETE' as features
sns.scatterplot(data=df, x='CREATE', y='MODIFY', hue='cluster', palette='viridis')
plt.title("K-means Clustering")
plt.savefig("kmeans_clustering_plot.png")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for CREATE, MODIFY, DELETE with cluster-based coloring
sc = ax.scatter(df['CREATE'], df['MODIFY'], df['DELETE'], c=df['cluster'], cmap='viridis')

# Adding labels and title
ax.set_xlabel('CREATE')
ax.set_ylabel('MODIFY')
ax.set_zlabel('DELETE')
plt.title("3D K-means Clustering")

# Adding a color bar to understand cluster colors
plt.colorbar(sc)


plt.savefig("3d_kmeans_clustering_plot.png")  # To save the plot
# plt.show()  # Uncomment to display the plot