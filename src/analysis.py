import pandas as pd
import matplotlib.pyplot as plt

# đọc dataset
df = pd.read_csv("../data/netflix_titles_nov_2019.csv")

# Biểu đồ 1 - Phân tích số lượng phim theo năm
# thống kê số lượng phim theo năm
movies_per_year = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(movies_per_year)

plt.title("Netflix Titles by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.savefig("../images/titles_by_year.png")

#Biểu đồ 2 - Số lượng Movies vs TV show
type_counts = df['type'].value_counts()

plt.figure()
type_counts.plot(kind='bar')
plt.title("Number of Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("../images/type_distribution.png")

#Biểu đồ 3 - Top 10 quốc gia có phim nhiều nhất
country_counts = df['country'].value_counts().head(10)

plt.figure()
country_counts.plot(kind='bar')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.savefig("../images/top_countries.png")

# hiển thị
plt.show()