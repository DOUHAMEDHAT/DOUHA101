
### Install/Load the Packages Patch needed:

# Import the packages needed (Add a comma followed by the package name):
packages <-   base::list(
  'stringi', 'dplyr', 'data.table', 'ggplot2','plyr','lubridate','tidyverse','e1071',
  'PerformanceAnalytics', 'svDialogs','DBI','dbplyr','dbplyr','bizdays','plotly','corrplot','psych'
  )

# Function of packages checking:
pack <- function(pkg) {
  
  old_pkg <- packages[!(packages %in% installed.packages()[, "Package"])]
  
  for (i in old_pkg) {
    sapply(i, install.packages)
  }
  
  for (j in packages) {
    sapply(j, require, character.only = TRUE)
  }
  
  new_pkg <- packages[(packages %in% installed.packages()[, "Package"])]

    if (length(new_pkg) == length(packages)){
    print("All Packages are Installed/Loaded Successfully")
  } else {
    print("Please check pack_function (Not All Packages are loaded)")
  }
    }

# Execute the function:
pack(packages)
