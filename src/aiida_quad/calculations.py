from aiida.common import datastructures
from aiida.engine import CalcJob
from aiida.orm import SinglefileData, Int, Float, Str
from aiida.common.datastructures import CodeInfo, CalcInfo

class TemplateCalcJob(CalcJob):
    """
    AiiDA calculation plugin template.
    Replace 'TemplateCalcJob' with your class name.
    """
    
    @classmethod
    def define(cls, spec):
        """Define inputs and outputs of the calculation."""
        super(TemplateCalcJob, cls).define(spec)

        # Define inputs here
        # spec.input('parameter_a', valid_type=Float, help='Description of parameter a.')
        # spec.input('parameter_b', valid_type=Int, help='Description of parameter b.')
        
        # Define outputs here
        # spec.output('result_x', valid_type=Float, help='Description of result x.')
        # spec.output('output_file', valid_type=SinglefileData, help='The output file.')

        # Default options
        spec.input('metadata.options.output_filename', valid_type=str, default='output.txt')
        
        # Define the parser name (must match the entry point in setup)
        # spec.inputs['metadata']['options']['parser_name'].default = 'template-parser'

        # Define exit codes
        spec.exit_code(
            300, 'ERROR_MISSING_OUTPUT_FILES', message='Calculation did not produce all expected output files.'
        )
        
    def prepare_for_submission(self, folder):
        """
        Create input files.

        :param folder: an `aiida.common.folders.Folder` where the plugin should temporarily place all files needed by
            the calculation.
        :return: `aiida.common.datastructures.CalcInfo` instance
        """
        
        # 1. Prepare input files content
        # input_content = f"{self.inputs.parameter_a.value} {self.inputs.parameter_b.value}"
        
        # 2. Write input files to the folder
        # with folder.open('input.txt', 'w') as f:
        #     f.write(input_content)

        # 3. Setup CodeInfo
        codeinfo = CodeInfo()
        # codeinfo.cmdline_params = ['input.txt'] # Arguments for the command
        codeinfo.code_uuid = self.inputs.code.uuid
        codeinfo.stdout_name = self.metadata.options.output_filename
        
        # 4. Setup CalcInfo
        calcinfo = CalcInfo()
        calcinfo.codes_info = [codeinfo]
        calcinfo.local_copy_list = []
        calcinfo.retrieve_list = [self.metadata.options.output_filename]

        return calcinfo
