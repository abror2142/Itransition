from probability_calculation import ProbabilityCalculation
from rich.table import Table
from rich.console import Console


class ProbabilityTable:

    def __init__(self, dices):
        self.dices = dices

    def print(self):
        table = Table(title="Probability of the win fоr the user:", show_lines=True)
        table.add_column("User dice v")

        # Header of the table
        for dice in self.dices:
            table.add_column(",".join(dice))

        # Row of the table
        for dice_a in self.dices:
            row = []
            for dice_b in self.dices:
                probability = ProbabilityCalculation(dice_a, dice_b)
                x = str(probability.calculate())
                if dice_a == dice_b:
                    row.append('- ('+x+')')
                else:
                    row.append(x)
            table.add_row(",".join(dice_a),*row)
        console = Console()
        console.print(table)
