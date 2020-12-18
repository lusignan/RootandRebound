library(tidyverse)
library(waffle)

parts <- c(Yes = 75, No = 25)
waffle(parts, rows = 10,
       colors = c("#2d76be","#b3b1b1"),
       title = "Reconnected with Family",
       legend_pos = "bottom",
       ) +
  theme(plot.title = element_text(family = "Gotham Medium",
                                  size = 48),
        legend.text = element_text(family = "Gotham Book",
                                   size = 24))
