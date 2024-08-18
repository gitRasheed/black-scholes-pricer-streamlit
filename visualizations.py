import plotly.graph_objects as go
import numpy as np

def create_heatmap(S_range, sigma_range, option_prices, title):
    fig = go.Figure(data=go.Heatmap(
        z=option_prices,
        x=S_range,
        y=sigma_range,
        colorscale='RdYlGn',
        hovertemplate='Price: $%{x:.2f}<br>Volatility: %{y:.2f}<br>Option Value: $%{z:.2f}<extra></extra>'
    ))
    fig.update_layout(
        title=title,
        xaxis_title='Stock Price',
        yaxis_title='Volatility',
        height=500,
        width=700,
        dragmode='pan',
        xaxis=dict(fixedrange=True),
        yaxis=dict(fixedrange=True)
    )
    return fig

def create_profit_loss_chart(S_range, pnl, break_even, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=S_range,
        y=pnl,
        mode='lines',
        name='P&L',
        line=dict(color='blue'),
        hovertemplate='Stock Price: $%{x:.2f}<br>P&L: $%{y:.2f}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=[break_even],
        y=[0],
        mode='markers',
        name='Break-even',
        marker=dict(color='red', size=10),
        hovertemplate='Break-even Price: $%{x:.2f}<extra></extra>'
    ))
    fig.update_layout(
        title=title,
        xaxis_title='Stock Price',
        yaxis_title='Profit/Loss',
        height=500,
        width=700,
        dragmode='pan',
        xaxis=dict(fixedrange=True),
        yaxis=dict(fixedrange=True)
    )
    
    fig.add_traces([
        go.Scatter(x=S_range, y=np.maximum(pnl, 0), fill='tozeroy', fillcolor='rgba(0,255,0,0.2)', line=dict(width=0), showlegend=False, name='Profit'),
        go.Scatter(x=S_range, y=np.minimum(pnl, 0), fill='tozeroy', fillcolor='rgba(255,0,0,0.2)', line=dict(width=0), showlegend=False, name='Loss')
    ])
    return fig

def create_greeks_plot(S_range, greeks, title):
    fig = go.Figure()
    greek_names = {'delta_call': 'Delta', 'delta_put': 'Delta', 'gamma': 'Gamma', 'vega': 'Vega', 'theta_call': 'Theta', 'theta_put': 'Theta', 'rho_call': 'Rho', 'rho_put': 'Rho'}
    for greek, values in greeks.items():
        fig.add_trace(go.Scatter(
            x=S_range,
            y=values,
            mode='lines',
            name=greek_names[greek],
            hovertemplate=f'{greek_names[greek]}: %{{y:.4f}}<br>Stock Price: $%{{x:.2f}}<extra></extra>'
        ))
    fig.update_layout(
        title=title,
        xaxis_title='Stock Price',
        yaxis_title='Greek Value',
        height=500,
        width=700,
        dragmode='pan',
        xaxis=dict(fixedrange=True),
        yaxis=dict(fixedrange=True)
    )
    return fig