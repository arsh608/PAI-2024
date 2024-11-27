# Function to calculate the sum of even numbers in a list
sum_of_even_numbers <- function(numbers) {
  even_numbers <- numbers[numbers %% 2 == 0]  # Filter even numbers
  return(sum(even_numbers))
}

numbers <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_sum <- sum_of_even_numbers(numbers)
print(paste("Sum of even numbers:", even_sum))
