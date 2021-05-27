from pytest_bdd import scenarios

from step_definitions.steps_given import *
from step_definitions.steps_then import *
from step_definitions.steps_when import *
from step_definitions.steps_custom import *

scenarios('../features/functional')
