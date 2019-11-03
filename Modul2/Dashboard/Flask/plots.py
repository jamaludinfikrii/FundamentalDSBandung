import plotly
import plotly.graph_objects  as go
import plotly.express as px
from cleaning_data import data_pokemon
import json

def count_type1():
    df = data_pokemon()
    df_group= df['Type 1'].value_counts()
    
    fig = go.Figure([
        go.Bar(x=df_group.index , y= df_group.values)
    ])
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    # fig.show()

def dist_total():
    df= data_pokemon()
    fig = px.box(df,x='Generation' , y='Total')
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
