"""Assign Params to Attributes by Joel Hedlund <joel.hedlund at gmail.com>.

PyDev script for generating python code that assigns method parameter 
values to attributes of self with the same name. Activates with 'a' by 
default. Edit global constants ACTIVATION_STRING and WAIT_FOR_ENTER if this
does not suit your needs. See docs on the class AssignToAttribsOfSelf for 
more details.

Contact the author for bug reports/feature requests.

Changed:Fabio Zadrozny (binded to Ctrl+1 too)
"""

__version__ = "1.0.1"

__copyright__ = """Available under the same conditions as PyDev.

See PyDev license for details.
http://pydev.sourceforge.net

"""

# Change this if the default does not suit your needs
ACTIVATION_STRING = 'a'
WAIT_FOR_ENTER = False

# For earlier Python versions
True, False = 1,0

# Set to True to force Jython script interpreter restart on save events.
# Useful for Jython PyDev script development, not useful otherwise.
DEBUG = False

# This is a magic trick that tells the PyDev Extensions editor about the 
# namespace provided for pydev scripts:
if False:
    from org.python.pydev.editor import PyEdit #@UnresolvedImport
    cmd = 'command string'
    editor = PyEdit
    
assert cmd is not None 
assert editor is not None

if DEBUG and cmd == 'onSave':
    from org.python.pydev.jython import JythonPlugin #@UnresolvedImport
    editor.pyEditScripting.interpreter = JythonPlugin.newPythonInterpreter()

if cmd == 'onCreateActions' or (DEBUG and cmd == 'onSave'): 
    from org.python.pydev.editor.correctionassist import PythonCorrectionProcessor #@UnresolvedImport
    import assign_params_to_attributes_action as helper 
    import assign_params_to_attributes_assist as helper2
                        
    sDescription = 'Assign method params to attribs of self'
    o = helper.AssignToAttribsOfSelf(editor)
    editor.addOfflineActionListener(ACTIVATION_STRING, o, sDescription, WAIT_FOR_ENTER)
    
    ASSIGN_PARAMS_TO_ATTRIBUTES_ASSIST = 'ASSIGN_PARAMS_TO_ATTRIBUTES_ASSIST'
    if not PythonCorrectionProcessor.hasAdditionalAssist(ASSIGN_PARAMS_TO_ATTRIBUTES_ASSIST):
        assist = helper2.AssistAssignParamsToAttributes()
        PythonCorrectionProcessor.addAdditionalAssist(ASSIGN_PARAMS_TO_ATTRIBUTES_ASSIST, assist)

