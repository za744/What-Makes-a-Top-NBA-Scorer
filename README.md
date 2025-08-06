# What-Makes-a-Top-NBA-Scorer
This project uses NBA player statistics to predict Points Per Game (PPG) using machine learning models. It includes full data exploration, model training, and a simple Streamlit app.

## Project Overview

- **Goal**: Predict how many points per game an NBA player scores based on their stats and position.
- **Data Source**: NBA player season stats (CSV file).
- **Key Features Used**:
  - Minutes Played (MP)
  - Field Goal Attempts (FGA)
  - Free Throw Attempts (FTA)
  - 3-Point Attempts (3PA)
  - Assists (AST)
  - Turnovers (TOV)
  - Player Position (One-hot encoded)

## Exploratory Data Analysis (EDA)

Before modeling, I performed EDA to identify which features had the strongest correlation with PPG. I cleaned missing values and filtered out low-minute/low-game players to focus on core contributors.

**Key insights:**
- Players who shoot more (FGA, 3PA, FTA) tend to score more.
- More minutes and fewer turnovers also correlate with higher scoring.
- Position plays a role; guards vs centers score differently.

## Models Used

I trained and compared the following models:

| Model              | MAE   | RMSE  | R² Score |
|-------------------|-------|-------|----------|
| Linear Regression | 0.65  | 0.88  | 0.98     |
| Random Forest     | 0.71  | 0.99  | 0.97     |
| XGBoost           | 0.69  | 0.94  | 0.98     |

**Linear Regression performed the best**, suggesting the relationship between features and PPG is fairly linear.

### Overfitting Check

I compared R² on both train and test sets:
- Train R²: **0.999**
- Test R²: **0.979**

Since both scores are high and close, the model does **not appear overfitted**.

## Streamlit App

A simple Streamlit app was created to allow users to input player stats and receive a predicted PPG output using the trained linear regression model.

You can run the app locally:

```bash
streamlit run app.py

