from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .record_base import (RecordBase, FieldComponent)
from .registry import (get_record_class, _register_record_type,
                       get_record_by_name)
from .areadetector import *
from .records import *
