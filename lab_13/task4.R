# Function to calculate income tax based on income
calculate_tax <- function(income) {
  if (income < 30000) {
    return(0)
  } else if (income >= 30000 && income <= 70000) {
    return(income * 0.10)  # 10% tax
  } else if (income > 70000 && income <= 100000) {
    return(income * 0.15)  # 15% tax
  } else {
    return(income * 0.20)  # 20% tax
  }
}

income <- 80000
tax <- calculate_tax(income)
print(paste("Tax to be paid:", tax))
