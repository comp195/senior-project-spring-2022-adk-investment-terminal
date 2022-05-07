import matplotlib.pyplot as plt
import TickerScrape

solvencyLT = [TickerScrape.beta, TickerScrape.peg]
solvencyST = [TickerScrape.current, TickerScrape.quick]

plt.scatter(solvencyLT, solvencyST)
plt.show()