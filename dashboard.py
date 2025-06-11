import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from sentiment_analysis import analyze_sentiment
from twitter_data import get_tweets_v2

# Initialize Dash app
app = dash.Dash(__name__)

# Function to get real-time sentiment data
def get_data(keyword):
    tweets = get_tweets(keyword, 50)
    df = pd.DataFrame(tweets, columns=["Text"])
    df["Sentiment"] = df["Text"].apply(analyze_sentiment)
    return df

# UI Layout
app.layout = html.Div([
    html.H1("Political Sentiment Analysis Dashboard", style={"textAlign": "center"}),
    
    dcc.Input(id="search_input", type="text", value="Biden", debounce=True),
    html.Button("Search", id="search_button", n_clicks=0),
    
    dcc.Graph(id="sentiment_chart")
])

@app.callback(
    dash.Output("sentiment_chart", "figure"),
    [dash.Input("search_button", "n_clicks")],
    [dash.State("search_input", "value")]
)
def update_chart(n_clicks, keyword):
    df = get_data(keyword)
    fig = px.pie(df, names="Sentiment", title=f"Sentiment Analysis of {keyword}")
    return fig

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)

