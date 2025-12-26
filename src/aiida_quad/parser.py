from aiida.engine import ExitCode
from aiida.orm import SinglefileData, Float
from aiida.parsers.parser import Parser
from aiida.plugins import CalculationFactory

class QuadParser(Parser):
    def parse(self, **kwargs):
        """Parse outputs, store results in database."""
        output_filename = self.node.get_option('output_filename')

        # add output file
        self.logger.info(f"Parsing '{output_filename}'")
        with self.retrieved.open(output_filename, 'rb') as handle:
            output_node = SinglefileData(file=handle)
        self.out('quad', output_node)
       
        lines = [line.strip() for line in output_node.get_content().splitlines()]
        if lines[0] != "ERROR" and lines[0] != 'None':
            numbers = lines[0].split(',')
            x1 = float(numbers[0])
            x2 = float(numbers[1])
            self.out('x1', Float(x1))
            self.out('x2', Float(x2))
        return ExitCode(0)
