# performing the linear regressionnwithout using any library
# goal: finding the equation of the regression line based on the given set of points

def findingRegressionLine(x,y):
    if len(x) != len(y):
        return (False, False)

    mean_x = sum(x) / len(x)
    print(f'Mean x: {round(mean_x,2)}')
    mean_y = sum(y) / len(y)
    print(f'Mean y: {round(mean_y,2)}')
    x_xdash = [element - mean_x for element in x]
    y_dash = [element - mean_y for element in y]
    mul_xydash = [x_xdash[i]*y_dash[i] for i in range(len(x))]
    numerator = sum(mul_xydash)
    x_xsquare = [element*element for element in x_xdash]
    denominator = sum(x_xsquare)
    m = numerator / denominator
    c = mean_y - (m*mean_x)

    return (m,c)


x = [1,2,3,4,5]
y = [1.2,1.8,2.6,3.2,3.8]
m,c = findingRegressionLine(x,y)
m = round(m,2)
c = round(c,2)

if m and c:
    print('The Linear Regression Line equation: ')
    if c>= 0:
        print(f"y = {m}x + {c}")
    else:
        print(f"y = {m}x - {c}")