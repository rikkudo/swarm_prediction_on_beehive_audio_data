from enum import Enum

class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c, cls))

class separation_type(ExtendedEnum):
    BY_TIME_SLICES = 0
    BY_FREQ_SLICES = 1
    WHOLE_ONE_UNIT = 2

class dani_filtering_type(ExtendedEnum):
    NEGATIVE = 0
    MEAN = 1

class norming_type(ExtendedEnum):
    Z_NORMING = 0
    SCALING = 1

class data_type(ExtendedEnum):
    MATRIX = 0
    TIMESERIE = 1

class filtering_type(ExtendedEnum):
    DANI = "dani"
    HIGHPASS = "highpass"
    LOWPASS = "lowpass"
    BANDPASS = "bandpass"
    GAUSSIAN = "gaussian"
    LAPLACIAN = "laplacian"
    GAUSSIAN_LAPLACE = "gaussian_laplace"
    MEAN = "mean"
    MEDIAN = "median"
    MEDIAN_LOG = "median_log"
    ALL = "all"
    NONE = "none"


class Feature_type(ExtendedEnum):
    STFT = "stft"
    MFCC = "mfcc"
    MFCC_DELTA = "mfcc_delta"
    CHROMA = "chroma"
    ZCR = "zcr"
    SC = "sc"
    ALL = "all"
    NONE = "none"
