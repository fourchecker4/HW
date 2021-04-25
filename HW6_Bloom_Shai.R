matrix1 <- matrix(c(7, 2, 9, 4, 12, 13), nrow = 2, ncol = 3)
matrix2 <- matrix(c(1, 2, 3, 7, 8, 9, 12, 13, 14, 19, 20, 21), nrow = 3, ncol = 4)
matrix1 %*% matrix2

dataframe1 <- data.frame(
  id = c(1, 2, 3, 4, 5),
  name = c('Peter', 'Amy', 'Ryan', 'Gary', 'Michelle'),
  salary = c(623.30, 515.20, 611.00, 729.00, 843.25)
)
dataframe1

department <- c('Sales', 'Human Resources', 'Marketing', 'Finance', 'Customer Service')
dataframe2 <- cbind(dataframe1, department)
dataframe2

dataframe3 <- dataframe2[-c(1, 3, 5), -c(2, 3)]
dataframe3

bar_name <- c('Peter', 'Gary', 'Michelle')
bar_salary <- c (623.30, 729.00, 843.25)
barplot(bar_salary, names.arg = bar_name)

pie_labels <- c('Average Salary', 'Largest salary', 'Lowest salary')
pie_colors <- c('yellow', 'green', 'red')
pie_data <- c(mean(dataframe1[1:5, 3]), max(dataframe1[1:5, 3]), 
              min(dataframe1[1:5, 3]))
pie(pie_data, label = pie_labels, main = 'Salaries', col = pie_colors)

score <- c('player 1\'s score is 5', 'player 2\'s score is 7')
rounds <- function(n){
  for (x in 1:n){
    print('round #', x)
    score
    print()
  }
}
rounds(10)

results <- function(){
  choices <- c('rock', 'paper')
  player1 <- choices[1]
  player2 <- choices[2]
  if (player1 == 'rock' & player2 == 'scissors'){
    print('player 1 wins, rock smashes scissors')
    winner <- 'player 1'
    return(winner)
  } else if (player1 == 'rock' & player2 == 'paper'){
    print('player 2 wins, paper covers rock')
    winner <- 'player 2'
    return(winner)
  } else if (player1 == 'paper' & player2 == 'rock'){
    print('player 1 wins, paper covers rock')
    winner <- 'player 1'
    return(winner)
  } else if (player1 == 'paper' & player2 == 'scissors'){
    print('player 2 wins, scissors cut paper')
    winner <- 'player 2'
    return(winner)
  } else if (player1 == 'scissors' & player2 == 'rock'){
    print('player 2 wins, rock smashes scissors')
    winner <- 'player 2'
    return(winner)
  } else if (player1 == 'scissors' & player2 == 'paper'){
    print('player 1 wins, scissors cut paper')
    winner <- 'player 1'
    return(winner)
  } else{
    print('both players selected the same thing, its a tie')
  }
}
results
  
  
  