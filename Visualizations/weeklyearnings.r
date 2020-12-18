library(tidyverse)
library(extrafont)
library(ggthemes)

df <- incomeallggplot %>% drop_na()

randr <- c("#e2c221", "#2D76BE")

p <- ggplot(df, aes(x = reorder(Earnings, -Order), y = Percentage, fill = Status)) +
  geom_bar(stat = "identity", position = position_dodge2(reverse = TRUE)) +
  scale_fill_manual(values = randr) +
  scale_x_discrete(guide = guide_axis(n.dodge=2)) +
  scale_y_continuous(breaks = seq(0, 80, 10),
                     labels = function(x) paste0(x, "%")) +
  labs(title = "Weekly Earnings",
       x = "",
       y = "") +
  theme_minimal()

p + theme(legend.position = "right",
          legend.title = element_blank(),
          legend.text = element_text(family = "Gotham Book",
                                     size = 12),
          plot.title = element_text(family = "Gotham Medium",
                                    size = 36),
          axis.text.x = element_text(family = "Gotham Book",
                                     size = 12),
          axis.text.y = element_text(family = "Gotham Book",
                                     size = 12),
          plot.margin = margin(10, 10, 10, 100))