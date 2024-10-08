from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEDC2A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type DC2A model. This model represents field-controlled DC commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus.  It differs from the type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to DC commutator exciters. Reference: IEEE 421.5-2005, 5.2.

    :efd1: Exciter voltage at which exciter saturation is defined (<i>E</i><i><sub>FD1</sub></i>) (&gt; 0).  Typical value = 3,05. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (<i>E</i><i><sub>FD2</sub></i>) (&gt; 0).  Typical value = 2,29. Default: 0.0
    :exclim: (<i>exclim</i>).  IEEE standard is ambiguous about lower limit on exciter output. Typical value = - 999  which means that there is no limit applied. Default: 0.0
    :ka: Voltage regulator gain (<i>K</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 300. Default: 0.0
    :ke: Exciter constant related to self-excited field (<i>K</i><i><sub>E</sub></i>).  Typical value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gain (<i>K</i><i><sub>F</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0.0
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, <i>E</i><i><sub>FD1</sub></i> (<i>S</i><i><sub>E</sub></i><i>[E</i><i><sub>FD1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,279. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, <i>E</i><i><sub>FD2</sub></i> (<i>S</i><i><sub>E</sub></i><i>[E</i><i><sub>FD2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,117. Default: 0.0
    :ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 0,01. Default: 0
    :tb: Voltage regulator time constant (<i>T</i><i><sub>B</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :tc: Voltage regulator time constant (<i>T</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :te: Exciter time constant, integration rate associated with exciter control (<i>T</i><i><sub>E</sub></i>) (&gt; 0).  Typical value = 1,33. Default: 0
    :tf: Excitation control system stabilizer time constant (<i>T</i><i><sub>F</sub></i>) (&gt; 0).  Typical value = 0,675. Default: 0
    :uelin: UEL input (<i>uelin</i>). true = input is connected to the HV gate false = input connects to the error signal. Typical value = true. Default: False
    :vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>)(&gt; ExcIEEEDC2A.vrmin).  Typical value = 4,95. Default: 0.0
    :vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0 and &lt; ExcIEEEDC2A.vrmax).  Typical value = -4,9. Default: 0.0
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "efd1": [
            cgmesProfile.DY.value,
        ],
        "efd2": [
            cgmesProfile.DY.value,
        ],
        "exclim": [
            cgmesProfile.DY.value,
        ],
        "ka": [
            cgmesProfile.DY.value,
        ],
        "ke": [
            cgmesProfile.DY.value,
        ],
        "kf": [
            cgmesProfile.DY.value,
        ],
        "seefd1": [
            cgmesProfile.DY.value,
        ],
        "seefd2": [
            cgmesProfile.DY.value,
        ],
        "ta": [
            cgmesProfile.DY.value,
        ],
        "tb": [
            cgmesProfile.DY.value,
        ],
        "tc": [
            cgmesProfile.DY.value,
        ],
        "te": [
            cgmesProfile.DY.value,
        ],
        "tf": [
            cgmesProfile.DY.value,
        ],
        "uelin": [
            cgmesProfile.DY.value,
        ],
        "vrmax": [
            cgmesProfile.DY.value,
        ],
        "vrmin": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class ExcitationSystemDynamics: \n"
        + ExcitationSystemDynamics.__doc__
    )

    def __init__(
        self,
        efd1=0.0,
        efd2=0.0,
        exclim=0.0,
        ka=0.0,
        ke=0.0,
        kf=0.0,
        seefd1=0.0,
        seefd2=0.0,
        ta=0,
        tb=0,
        tc=0,
        te=0,
        tf=0,
        uelin=False,
        vrmax=0.0,
        vrmin=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.efd1 = efd1
        self.efd2 = efd2
        self.exclim = exclim
        self.ka = ka
        self.ke = ke
        self.kf = kf
        self.seefd1 = seefd1
        self.seefd2 = seefd2
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.te = te
        self.tf = tf
        self.uelin = uelin
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEDC2A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
