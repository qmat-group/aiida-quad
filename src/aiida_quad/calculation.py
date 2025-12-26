from aiida.common import datastructures
from aiida.engine import CalcJob
from aiida.orm import SinglefileData, Int, Float
from aiida.common.datastructures import CodeInfo, CalcInfo

class QuadCalcJob(CalcJob):
    """AiiDA calculation plugin wrapping the diff executable."""
    @classmethod
    def define(cls, spec):
        """Define inputs and outputs of the calculation."""
        super(QuadCalcJob, cls).define(spec)

        # new ports
        spec.input('a', valid_type=Float, help='Parameter a.')
        spec.input('b', valid_type=Float, help='Parameter b.')
        spec.input('c', valid_type=Float, help='Parameter c.')
        
        spec.output('x1', valid_type=Float, help='Result x1.')
        spec.output('x2', valid_type=Float, help='Result x2.')
        spec.output('quad', valid_type=SinglefileData, help='Nghiem cua PT.')

        spec.input('metadata.options.output_filename', valid_type=str, default='result.quad')
        spec.inputs['metadata']['options']['parser_name'].default = 'quad-parser'

        spec.exit_code(
            300, 'ERROR_MISSING_OUTPUT_FILES', message='Calculation did not produce all expected output files.'
        )
        
    def prepare_for_submission(self, folder):
        """Create input files.

        :param folder: an `aiida.common.folders.Folder` where the plugin should temporarily place all files needed by
            the calculation.
        :return: `aiida.common.datastructures.CalcInfo` instance
        """
        codeinfo = CodeInfo()
        codeinfo.cmdline_params = [self.inputs.a.value, self.inputs.b.value, self.inputs.c.value]
        codeinfo.code_uuid = self.inputs.code.uuid
        codeinfo.stdout_name = self.metadata.options.output_filename

        # Prepare a `CalcInfo` to be returned to the engine
        calcinfo = CalcInfo()
        calcinfo.codes_info = [codeinfo]
        calcinfo.local_copy_list = []
        calcinfo.retrieve_list = [self.metadata.options.output_filename]

        return calcinfo
