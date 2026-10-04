import pandas as pd
import plotly.express as px


def keyword_chart(keywords):

    df = pd.DataFrame({
        "Keyword": keywords,
        "Count": list(range(len(keywords), 0, -1))
    })

    fig = px.bar(
        df,
        x="Keyword",
        y="Count",
        title="Top Keywords"
    )

    return fig