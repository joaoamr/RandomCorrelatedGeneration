from pearsonspairs import pearsonspairs

#Example of the random generator of correlated values X and Y

n = 2000 #Number of pairs
p = 0.9 #Pearson's correlation coefficient
x_av = 100 #Average of X
x_sd = 200 #Standard deviation of X
y_av = -10 #Avarage of Y
y_sd = 50 #Standard deviation of Y

#Bind variable x to vector X and y to vector Y
[x,y] = pearsonspairs(n, 0.9, x_av, x_sd, y_av, y_sd)
