import pandas as pd
df = pd.read_excel('Testing Data.xlsx')
a=df.head(5)
print(a)
x=df['CGPA'].values 
y=df['Attandance'].values
x_mean=sum(x)/len(x)
y_mean=sum(y)/len(y)
num=sum((xi-x_mean)*(yi-y_mean)for xi,yi in zip(x,y))
deno=sum((xi-x_mean)**2 for xi in x)
theta_1=num/deno
theta_0=y_mean-theta_1 * x_mean
def predict(x_values):
    return [theta_0 + theta_1 *xi for xi in x_values]
x_test=[30,40,50]
y_pred=predict(x_test)
print(f"slope (theta_1):{theta_1}")
print(f"Intercept(theta_0):{theta_0}")
print(f"Predicted values: {y_pred}")
import matplotlib.pyplot as plt
plt.scatter(x,y,color='blue',label='Original data')
x_line=range(min(x),max(x)+1)
y_line=predict(x_line)
plt.plot(x_line,y_line,color='green',label='Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()