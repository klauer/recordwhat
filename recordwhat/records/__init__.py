# NOTE: 3 record exceed 255 components and are not imported here
# CPython limitation that there can only be 255 arguments to a function,
# so NamedTuple creation for devices fails for: mca, sscan

from .aai import AaiRecord
from .aao import AaoRecord
from .acalcout import AcalcoutRecord
from .ai import AiRecord
from .ao import AoRecord
from .asub import AsubRecord
from .asyn import AsynRecord
from .bi import BiRecord
from .bo import BoRecord
from .busy import BusyRecord
from .calcout import CalcoutRecord
from .calc import CalcRecord
from .compress import CompressRecord
from .dfanout import DfanoutRecord
from .digitel import DigitelRecord
from .epid import EpidRecord
from .event import EventRecord
from .fanout import FanoutRecord
from .histogram import HistogramRecord
from .longin import LonginRecord
from .longout import LongoutRecord
from .mbbidirect import MbbidirectRecord
from .mbbi import MbbiRecord
from .mbbodirect import MbbodirectRecord
from .mbbo import MbboRecord
from .mca import McaRecord
from .motor import MotorRecord
from .permissive import PermissiveRecord
from .scalcout import ScalcoutRecord
from .scaler import ScalerRecord
from .scanparm import ScanparmRecord
from .sel import SelRecord
from .seq import SeqRecord
# from .sscan import SscanRecord
from .sseq import SseqRecord
from .state import StateRecord
from .stringin import StringinRecord
from .stringout import StringoutRecord
from .subarray import SubarrayRecord
from .sub import SubRecord
from .swait import SwaitRecord
from .table import TableRecord
from .timestamp import TimestampRecord
from .transform import TransformRecord
from .vme import VmeRecord
from .vs import VsRecord
from .waveform import WaveformRecord
