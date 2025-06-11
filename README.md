# Review 2: Data Visualization & Interpretation

## 📊 Objective

The goal of Review 2 is to create meaningful, well-structured, and visually engaging data visualizations that help interpret key insights from IPL match and ball-by-ball data. This builds on the cleaned and engineered dataset from Review 1.

---

## 🛠️ Tools & Libraries Used

- **Python**
- **Pandas** – Data manipulation and preparation
- **Matplotlib & Seaborn** – Static data visualizations
- **Plotly Express** – Interactive charts
- **NumPy** – Numerical operations

---

## 📁 Files Included

- `review2_visuals.py`: The main Python script for data visualizations and insights.
- `deliveries.csv` and `matches.csv`: Datasets used.
- `README.md`: This file.

---

## 📈 Visualizations & Insights

The following charts and statistics were created to meet the evaluation criteria:

1. **Top 5 Run Scorers (Bar Plot)**  
   Clear comparison of highest run-getters in the dataset.

2. **Top 5 Wicket Takers (Bar Plot)**  
   Highlights key bowlers with the most dismissals.

3. **Average Runs Per Over (Line Plot)**  
   Identifies scoring patterns across different overs.

4. **Team-Wise Total Runs (Bar Plot)**  
   Summarizes batting performance by team.

5. **Outlier Detection (IQR Method)**  
   Shows distribution anomalies in runs scored per delivery.

Each visualization includes:
- **Proper Labels**
- **Color Schemes for Clarity**
- **Legends & Titles**
- **Interactive Features** (using Plotly for deeper exploration)

---

## 🧠 Interpretation & Storytelling

- Batsmen and bowlers' performances are benchmarked to reveal standout players.
- The average run rate per over gives insights into powerplays and death overs.
- Team comparisons help identify consistently high-scoring teams.
- Outliers highlight exceptional or unusual deliveries.

Narratives are embedded within the visual flow, guiding the viewer from raw data to meaningful insight.

---

## ▶️ How to Run This Project

1. Clone the GitHub repository.
2. Open the `review2/` folder in **VS Code**.
3. Run `review2_visuals.py` using Python 3 (recommend using a virtual environment).
4. Ensure the datasets (`matches.csv`, `deliveries.csv`) are in the same directory.

```bash
python review2_visuals.py
