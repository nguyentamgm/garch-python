# GARCH Model: A quick definition
From: https://www.investopedia.com/terms/g/garch.asp 

## What Is Generalized AutoRegressive Conditional Heteroskedasticity (GARCH)?
Generalized AutoRegressive Conditional Heteroskedasticity (GARCH) is a statistical model used in analyzing time-series data where the variance error is believed to be serially autocorrelated. GARCH models assume that the variance of the error term follows an autoregressive moving average process.

- GARCH is a statistical modeling technique used to help predict the volatility of returns on financial assets.
- GARCH is appropriate for time series data where the variance of the error term is serially autocorrelated following an autoregressive moving average process. 
- GARCH is useful to assess risk and expected returns for assets that exhibit clustered periods of volatility in returns.

# References

### Docs
- https://medium.com/@corredaniel1500/forecasting-volatility-deep-dive-into-arch-garch-models-46cd1945872b (with python implementation guideline)
- https://web-static.stern.nyu.edu/rengle/GARCH101.PDF

### Codes
- https://github.com/topics/garch-models
- https://github.com/iskakovs/GARCH-models (GARCH model in R)

# How to use this repository

## Prerequisites
- Git installed
- Python & Pip installed

## Clone the repository
```
$ git clone https://github.com/nguyentamgm/garch-python.git
```

## Get into the directory
```
$ cd ./garch-python
```

## Install dependencies
```
$ pip install -r requirements.txt
```

## Run the script
```
$ python garch_model.py
```

Or with python3:
```
$ python3 garch_model.py
```

Example result:
```
python3 garch_model.py
Iteration:      1,   Func. Count:      5,   Neg. LLF: 4134.427937004846
Iteration:      2,   Func. Count:     14,   Neg. LLF: 3069.3128992011434
Iteration:      3,   Func. Count:     20,   Neg. LLF: 3281.656935484945
Iteration:      4,   Func. Count:     25,   Neg. LLF: 2411.9994535380292
Iteration:      5,   Func. Count:     30,   Neg. LLF: 2403.728258751935
Iteration:      6,   Func. Count:     34,   Neg. LLF: 2403.6973115263318
Iteration:      7,   Func. Count:     38,   Neg. LLF: 2403.6943452180794
Iteration:      8,   Func. Count:     42,   Neg. LLF: 2403.694209993054
Iteration:      9,   Func. Count:     46,   Neg. LLF: 2403.6941467812926
Iteration:     10,   Func. Count:     49,   Neg. LLF: 2403.6941467813836
Optimization terminated successfully    (Exit mode 0)
            Current function value: 2403.6941467812926
            Iterations: 10
            Function evaluations: 49
            Gradient evaluations: 10
```
