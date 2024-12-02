# Stock_ML_Regressor_Models

STAT 4188 Final Project Topic Proposal

General Idea:
I plan to analyze publicly available time series stock data with the goal of building multiple regression models. I ultimately want to finetune the models and determine the optimal machine learning model for predicting stock prices. I would furthermore be interested in seeing how well my model generalizes to other stocks. I predict that generalizability will be greatest for other tech stocks and will suffer when used to predict stocks in other sectors.

I plan to get the data from NASDAQ.com or an equivalent site to get historical stock price data. I will begin the project with AAPL (Apple) stock.

After normalizing the data, I will split by data using time series specific techniques (e.g. walk-forward validation). After developing multiple regression models (linear regression, random forest, XGBoost, SVR, MLP Regressor, LSTM), I will finetune each of them, score them based on common metrics, and determine the optimal model.

Finally, I will attempt to apply the models to other stocks, first tech stocks, and then later non-tech stocks, to see the extent of generalizability.
