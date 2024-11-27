# Function to calculate grade based on score
calculate_grade <- function(score) {
  if (score >= 90) {
    return("A")
  } else if (score >= 80) {
    return("B")
  } else if (score >= 70) {
    return("C")
  } else {
    return("Fail")
  }
}

score <- 85
grade <- calculate_grade(score)
print(paste("Grade:", grade))
