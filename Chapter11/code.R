
###### scatter
library(plotly)
set.seed(123)
x1<-rnorm(50, mean = 0, sd = 1)
x2<-rnorm(50, mean = 1, sd = 1)
data<-data.frame(x1, x2)
plot_ly(data, x = ~x1, y = ~x2, type ="scatter")


###### scatter3d
set.seed(123)
x1<-rnorm(20, mean = 0, sd = 1)
x2<-rnorm(20, mean = 1, sd = 1)
x3<-rnorm(20, mean = 2, sd = 1)
data<-data.frame(x1, x2,x3)
plot_ly(data, x = ~x1, y = ~x2,z=~x3,type ="scatter3d")


###### linear
set.seed(123)
x <- seq(1,50,1)
y <- rnorm(50, mean = 0, sd = 1)
data <- data.frame(x, y)
plot_ly(data, x = ~x, y =~ y, type = "scatter", mode = "lines")

###### mult_linear
######  method_1
library(plotly)
set.seed(123)
y1 <- rnorm(50, mean = 0, sd = 1)
y2 <- rnorm(50, mean = 3, sd = 1)
y3 <- rnorm(50, mean = 6, sd = 1)
y4 <- rnorm(50, mean = -2, sd = 1)
x <- seq(1,50,1)
data <- data.frame(x, y1, y2, y3,y4)
plot_ly(data, x = ~x, y = ~y1, name = "y1", type ="scatter", mode ="lines") %>%
add_trac1e(y = ~y2, name = "y2", mode = "lines+markers") %>%
add_trace(y = ~y3, name = "y3",mode = "markers")


######  method_2
set.seed(123)
y1 <- rnorm(50, mean = 0, sd = 1)
y2 <- rnorm(50, mean = 3, sd = 1)
y3 <- rnorm(50, mean = 6, sd = 1)
x <- seq(1,50,1)
data <- data.frame(x, y1, y2, y3)
plot_ly(data, x = ~x) %>%
add_trace(y = ~y1, name = "y1",mode = "lines") %>%
add_trace(y = ~y2, name = "y2", mode ="lines+markers") %>%
add_trace(y = ~y3, name = "y3", mode = "markers")







###### histogram
set.seed(123)
x<- rnorm(20, mean = 0, sd = 1)
y<-rnorm(20, mean =2, sd =3)
data<-data.frame(x,y)
plot_ly(data, x = ~x,type = "histogram")

plot_ly(data, x = ~x,type = "bar")

%>%
add_trace(y, type="histogram")


















