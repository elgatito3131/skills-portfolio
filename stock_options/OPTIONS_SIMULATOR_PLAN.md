This app is an educational options trading simulator that lets users practice buying and selling call and put options, track their P&L, and learn how options work through interactive explanations and charts.

- Select underlying stock
- Choose call or put
- Set strike price and expiry date
- Simulate buying/selling options with virtual money
- Show payoff diagram
- Track open positions
- Track P&L over time

- As a user, I want to select a stock and see its historical price chart.
- As a user, I want to simulate buying a call or put option.
- As a user, I want to enter strike, premium, expiry.
- As a user, I want to see my payoff diagram.
- As a user, I want to view my open positions and profit/loss.

- User accounts and authentication
- Save trade history between sessions
- Options pricing models (Black-Scholes, Binomial)
- Real-time price data
- Educational quizzes
- Advanced Greeks (Delta, Gamma)

Backend: FastAPI or Django
Frontend: Streamlit (simple) or React
Data: yfinance or Alpha Vantage
Storage: SQLite for trades
Deployment: Streamlit Cloud or Heroku
