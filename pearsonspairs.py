from random import gauss

'''
Generate n random float pairs with a determined Pearson's correlation coefficient
*n is the number of pairs of X and Y
*p is Pearson's correlatin coefficient
*x_av is the average of X
*x_sd is the standard deviation of X
*y_av is the average of Y
*y_sd is the standard deviation of Y
'''

def pearsonspairs(n, p, x_av, x_sd, y_av, y_sd):
    x = []
    y = []

    r = 0
    cov = p * (y_sd*x_sd) / n
    cov = cov*(n+1)
    for i in range(0, n):
        m = gauss(x_av, x_sd)
        c = (cov/(m - x_av)) + y_av

        #Try again if some variable takes undesirable value
        while c > y_av + y_sd or c < y_av - y_sd or m > x_av + x_sd or m < x_av - x_sd:
            m = gauss(x_av, x_sd)
            c = (cov/(m - x_av)) + y_av
        
        x.append(m)
        y.append(c)
        r = r + (x[i] - x_av)*(y[i] - y_av)

    r = r/(n-1)    
    r = r/(y_sd*x_sd)
    #r value must be very close to p value

    return [x,y]
