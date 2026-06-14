
import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels = ['Total Rows', 'Duplicates', 'Bad Emails', 'Bad Dates', 'Neg Spend']
values = [150, 0, 13, 18, 13]
colors_issues = ['#3498db', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c']

fig = make_subplots(rows=1, cols=2, subplot_titles=('Data Issues Found', 'Customer Distribution by City'),
                    specs=[[{'type': 'bar'}, {'type': 'pie'}]])

fig.add_trace(go.Bar(x=labels, y=values, marker_color=colors_issues,
                     text=values, textposition='outside', showlegend=False), row=1, col=1)

cities = {'Pune': 42, 'Mumbai': 35, 'Delhi': 28, 'Bangalore': 22, 'Hyderabad': 15, 'Unknown': 8}
fig.add_trace(go.Pie(labels=list(cities.keys()), values=list(cities.values()),
                     marker=dict(colors=['#2ecc71','#3498db','#f39c12','#9b59b6','#e74c3c','#95a5a6']),
                     textinfo='label+percent'), row=1, col=2)

fig.update_layout(height=450, title_text='Data Cleaning Automation - Interactive')
fig.write_html('3_data_cleaning_interactive.html')
print('Saved: 3_data_cleaning_interactive.html')
