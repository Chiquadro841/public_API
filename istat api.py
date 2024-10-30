from istatapi import discovery, retrieval
import matplotlib.pyplot as plt
import pandas as pd

#print(discovery.search_dataset("House"))
#50    143_497  House prices (Ipab)  DCSP_IPAB
# initialize the dataset and get its dimensions
ds = discovery.DataSet(dataflow_identifier="143_497")

#print(ds.dimensions_info()

freq = "Q" #monthly frequency
ITTER107 = ["ITC45", "ITFG","ITE","ITC","ITD"]
abit_comprav= "ALL"
ds.set_filters(freq = freq, ITTER107=ITTER107, abit_comprav=abit_comprav)
trade_df = retrieval.get_data(ds)

df = pd.DataFrame(trade_df)


milano_df = df[(df['ITTER107'] == 'ITC45') & (df['MISURA1'] == 4)][['MISURA1', 'TIME_PERIOD', 'OBS_VALUE']]

# Reset index if needed
milano_df.reset_index(drop=True, inplace=True)

# Display the new DataFrame
#print(milano_df)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(milano_df['TIME_PERIOD'], milano_df['OBS_VALUE'], marker='o', linestyle='-', color='b', label='Observation Value')

# Add titles and labels
plt.title('Line Chart of Observation Values for ITC45 with MISURA1 = 4')
plt.xlabel('Time Period')
plt.ylabel('Observation Value')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid()  # Add gridlines for better visualization
plt.legend()  # Show legend
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels

# Show the plot

import plotly.graph_objects as go
import plotly.express as px
# Create the line chart with points using Plotly Express
'''fig = px.line(
    milano_df,
    x='TIME_PERIOD',
    y='OBS_VALUE',
    title='Line Chart of Observation Values for ITC45 with MISURA1 = 4',
    markers=True  # This adds points to the line
)

# Update the layout for better visuals
fig.update_layout(
    xaxis_title='Time Period',
    yaxis_title='Observation Value',
    xaxis_tickangle=-45  # Rotate x-axis labels for better readability
)

# Show the plot
fig.show()'''
fig = go.Figure()

# Add a line trace
fig.add_trace(go.Scatter(
    x=milano_df['TIME_PERIOD'],
    y=milano_df['OBS_VALUE'],
    mode='lines+markers',  # Show both lines and markers
    name='Observation Value',
    line=dict(color='blue'),  # Line color
    marker=dict(size=8)  # Size of the markers
))

# Update layout
fig.update_layout(
    title='Line Chart of Observation Values for ITC45 with MISURA1 = 4',
    xaxis_title='Time Period',
    yaxis_title='Observation Value',
    xaxis_tickangle=-45,  # Rotate x-axis labels for better readability
    template='plotly_white'  # Optional: Use a white background
)
fig.show()