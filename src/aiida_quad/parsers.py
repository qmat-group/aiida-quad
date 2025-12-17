from aiida.engine import ExitCode
from aiida.orm import SinglefileData, Float, Int
from aiida.parsers.parser import Parser

class TemplateParser(Parser):
    """
    AiiDA parser plugin template.
    Replace 'TemplateParser' with your class name.
    """
    
    def parse(self, **kwargs):
        """
        Parse outputs, store results in database.
        """
        output_filename = self.node.get_option('output_filename')

        # Check if output file exists
        if output_filename not in self.retrieved.list_object_names():
            return self.exit_codes.ERROR_MISSING_OUTPUT_FILES

        # 1. Parse the output file
        self.logger.info(f"Parsing '{output_filename}'")
        with self.retrieved.open(output_filename, 'rb') as handle:
            output_node = SinglefileData(file=handle)
            content = output_node.get_content()
        
        # Store the raw output file if needed
        self.out('output_file', output_node)
       
        # 2. Extract data and set outputs
        # try:
        #     # Example parsing logic
        #     lines = content.splitlines()
        #     result_value = float(lines[0].strip())
        #     self.out('result_x', Float(result_value))
        # except Exception as e:
        #     self.logger.error(f"Error parsing output: {e}")
        #     return self.exit_codes.ERROR_PARSING_FAILED

        return ExitCode(0)
