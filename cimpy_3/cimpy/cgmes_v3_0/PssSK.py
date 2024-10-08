from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssSK(PowerSystemStabilizerDynamics):
    """
    Slovakian PSS with three inputs.

    :k1: Gain <i>P</i> (<i>K</i><i><sub>1</sub></i>).  Typical value = -0,3. Default: 0.0
    :k2: Gain <i>f</i><i><sub>E</sub></i><i> </i>(<i>K</i><i><sub>2</sub></i>).  Typical value = -0,15. Default: 0.0
    :k3: Gain <i>I</i><i><sub>f</sub></i><i> </i>(<i>K</i><i><sub>3</sub></i>).  Typical value = 10. Default: 0.0
    :t1: Denominator time constant (<i>T</i><i><sub>1</sub></i>) (&gt; 0,005).  Typical value = 0,3. Default: 0
    :t2: Filter time constant (<i>T</i><i><sub>2</sub></i>) (&gt; 0,005).  Typical value = 0,35. Default: 0
    :t3: Denominator time constant (<i>T</i><i><sub>3</sub></i>) (&gt; 0,005).  Typical value = 0,22. Default: 0
    :t4: Filter time constant (<i>T</i><i><sub>4</sub></i>) (&gt; 0,005).  Typical value = 0,02. Default: 0
    :t5: Denominator time constant (<i>T</i><i><sub>5</sub></i>) (&gt; 0,005).  Typical value = 0,02. Default: 0
    :t6: Filter time constant (<i>T</i><i><sub>6</sub></i>) (&gt; 0,005).  Typical value = 0,02. Default: 0
    :vsmax: Stabilizer output maximum limit (<i>V</i><i><sub>SMAX</sub></i>) (&gt; PssSK.vsmin).  Typical value = 0,4. Default: 0.0
    :vsmin: Stabilizer output minimum limit (<i>V</i><i><sub>SMIN</sub></i>) (&lt; PssSK.vsmax).  Typical value = -0.4. Default: 0.0
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "k1": [
            cgmesProfile.DY.value,
        ],
        "k2": [
            cgmesProfile.DY.value,
        ],
        "k3": [
            cgmesProfile.DY.value,
        ],
        "t1": [
            cgmesProfile.DY.value,
        ],
        "t2": [
            cgmesProfile.DY.value,
        ],
        "t3": [
            cgmesProfile.DY.value,
        ],
        "t4": [
            cgmesProfile.DY.value,
        ],
        "t5": [
            cgmesProfile.DY.value,
        ],
        "t6": [
            cgmesProfile.DY.value,
        ],
        "vsmax": [
            cgmesProfile.DY.value,
        ],
        "vsmin": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemStabilizerDynamics: \n"
        + PowerSystemStabilizerDynamics.__doc__
    )

    def __init__(
        self,
        k1=0.0,
        k2=0.0,
        k3=0.0,
        t1=0,
        t2=0,
        t3=0,
        t4=0,
        t5=0,
        t6=0,
        vsmax=0.0,
        vsmin=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.vsmax = vsmax
        self.vsmin = vsmin

    def __str__(self):
        str = "class=PssSK\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
