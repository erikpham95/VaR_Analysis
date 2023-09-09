# VaR Analysis
Calculate portfolio’s VaR using Historical, Monte Carlo &amp; Parametric Method

### 1.  VaR Fundamentals

#### a.  General

-   \~ quantifies the extent of possible financial losses within a firm, portfolio, or position

    -   over a specific time frame

    -   on a specified confidence level

-   Key elements

    -   Specified amount of loss in value or percentage (usually 5%)

    -   Time period over which the risk is assessed (usually 1 day / 30 days / 250 days)

    -   Confidence interval

        -   Firm-wide capital requirement → \~ 99% / 99.9%

        -   Risk limit setting / reporting → \~ 95% / 99%

-   E.g.: Fund determine an asset has a 3% one-month VaR of 2%  → there's 3% chance of the asset declining in value by 2% during the 1-month time frame

-   Advantages

    -   Widely used by all financial institutions (commercial / investment banks, hedge funds, etc.)

    -   Easy to understand

-   Disadvantages

    -   Input is subjective / not standardized (based on modeller's assumption)

    -   Don't account for black swan events

    -   VaR is not a coherent risk measure

#### b.  Calculation Methodologies

-   Historical Methods

    -   Use historical data to predict future behaviours

    -   Pros: Data-driven, easy to understand / implement

    -   Cons: Become inaccurate under changing market dynamics

-   Monte Carlo Methods

    -   Uses computational models to simulate projected returns over 1000s of possible iterations

    -   Utilizes random sampling and statistical modelling

    -   Pros 1: Flexible (Can incorporate complex relationships and various distribution assumptions)

    -   Pros 2: Robust (Can capture nonlinear relationships & provide a detailed view of potential outcomes)

    -   Cons: Requires significant computing resources for large simulations

-   Variance-Covariance (Parametric) Method

    -   Assumes asset returns are normally distributed

    -   Uses the mean and standard deviation of returns to calculate VaR

    -   Pros: Computationally efficient, provides a closed-form solution

    -   Cons: "Normal Distribution" assumption may not valid


### 2.  Project Descriptions

#### a.  Objectives & Setups

-   Aim: Find the portfolio's VaR value of the specified portfolio

    -   over a specific time frame (set at 30 days in the simulation)

    -   on a specified confidence level (set at 95% in the imulation)

-   Portfolio used for simulation

    -   Tickers: [XLK, XLC, XLY, XLE, XLI, XLB, XLF, XLRE, XLP, LU, XLV, FXI, GDX]

    -   Allocation: [0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.13, 0.1]

-   VaR will be calculated using all 3 methods

    -   Historical Methods: Use 5 years of historical data (2018/08/10 -- 2023/08/10)

    -   Monte Carlo Methods: Use 5 years of historical data + 10000 simulations

    -   Variance-Covariance (Parametric) Method

#### b.  Implementation Highlights

-   Programming details

    -   Required Python packages: yfinance, numpy, pandas, matplotlib, scipy

    -   Program outputs: VaR value + Graph plotting the distributed return of portfolio

-   Execution Guidelines (for Linux & VS code)

    -   S1: Go to your project folder that you store the script (assuming located at **/folder\_locations**) using **cd /folder\_locations**

    -   S2: Create & activate virtual environment

        -   **\> virtualenv -p python3.9 var\_analysis**

        -   **\> source /folder\_locations/var\_analysis/bin/activate**

    -   S3: Install libraries & provide permissions

        -   **\> pip install yfinance pandas matplotlib numpy scipy**

        -   **\> sudo chmod -R 777 Var\_Historical\_Method.py**

    -   S4: Run the script with the "Run Python file" button in VS Code

### 3.  Results

#### a.  Simulation Outputs

-   Historical Method

    -   VaR value: 8.61%

    -   Portfolio Return Visualization

![Use this template](https://github.com/erikpham95/VaR_Analysis/blob/main/Pic/VaR_Historical_Method.png)

-   Monte Carlo Method

    -   VaR value: 9.64%

    -   Portfolio Return Visualization

![Use this template](https://github.com/erikpham95/VaR_Analysis/blob/main/Pic/VaR_Monte_Carlo_Method.png)

-   Parametric Method

    -   VaR value: 12.53%

    -   Portfolio Return Visualization

![Use this template](https://github.com/erikpham95/VaR_Analysis/blob/main/Pic/VaR_Parametric_Method.png)

#### b.  Observations

-   There are notable difference in results for each calculation methods

-   Historical method still produce "roughly normally distributed return"

-   Parametric method produce result that's most far-off

-   Historical & Monte Carlo method seems to produce "better" result
