from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


def configurar_regressao(data_frame):
    X = data_frame.index.values.reshape(-1, 1)

    Y = data_frame.iloc[:, 0].values

    print(f'X: {X}')
    print(f'Y: {Y}')

    regression_model = LinearRegression().fit(X, Y)

    r_squared = regression_model.score(X, Y)

    x_with_const = sm.add_constant(X)

    regression_model_sm = sm.OLS(Y, x_with_const).fit()

    regression_summary = regression_model_sm.summary()

    print(regression_summary)
