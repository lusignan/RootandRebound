library(tidyverse)
library(extrafont)
library(ggthemes)

df <- systeminvolvement %>% drop_na()

randr <- c( "#cb5328", "#B3B1B1", "#e2c221", "#2D76BE")

p <- ggplot(df, aes(x = Percentage, y = reorder(Systems, Percentage), fill = Systems)) +
         geom_col() +
  geom_text(aes(
    label = scales::percent(Percentage/100),
    family = "Gotham Book"),
            hjust = -.25,
    size = 8) +
  scale_fill_manual(values = randr) +
  expand_limits(x = 70) +
  labs(title = "Involvement in Other Systems",
       x = "",
       y = "") +
  theme_minimal()

p + theme(legend.position = "none",
          legend.title = element_blank(),
          plot.title = element_text(family = "Gotham Medium",
                                    size = 48),
          panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          axis.text.x = element_blank(),
          axis.text.y = element_text(family = "Gotham Book",
                                     size = 24),
          plot.margin = unit(c(3, 3, 3, 3), "mm"))
