from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST2(TurbineGovernorDynamics):
    """
    Gas turbine.

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :w: Governor gain (1/droop) on turbine rating (<i>W</i>). Default: 0.0
    :x: Governor lead time constant (<i>X</i>) (&gt;= 0). Default: 0
    :y: Governor lag time constant (<i>Y</i>) (&gt; 0). Default: 0
    :z: Governor mode (<i>Z</i>). 1 = droop 0 = isochronous. Default: 0
    :etd: Turbine and exhaust delay (<i>Etd</i>) (&gt;= 0). Default: 0
    :tcd: Compressor discharge time constant (<i>Tcd</i>) (&gt;= 0). Default: 0
    :trate: Turbine rating (<i>Trate</i>).  Unit = MW. Default: 0.0
    :t: Fuel control time constant (<i>T</i>) (&gt;= 0). Default: 0
    :tmax: Maximum turbine limit (<i>Tmax</i>) (&gt; GovGAST2.tmin). Default: 0.0
    :tmin: Minimum turbine limit (<i>Tmin</i>) (&lt; GovGAST2.tmax). Default: 0.0
    :ecr: Combustion reaction time delay (<i>Ecr</i>) (&gt;= 0). Default: 0
    :k3: Ratio of fuel adjustment (<i>K3</i>). Default: 0.0
    :a: Valve positioner (<i>A</i>). Default: 0.0
    :b: Valve positioner (<i>B</i>). Default: 0.0
    :c: Valve positioner (<i>C</i>). Default: 0.0
    :tf: Fuel system time constant (<i>Tf</i>) (&gt;= 0). Default: 0
    :kf: Fuel system feedback (<i>Kf</i>). Default: 0.0
    :k5: Gain of radiation shield (<i>K5</i>). Default: 0.0
    :k4: Gain of radiation shield (<i>K4</i>). Default: 0.0
    :t3: Radiation shield time constant (<i>T3</i>) (&gt;= 0). Default: 0
    :t4: Thermocouple time constant (<i>T4</i>) (&gt;= 0). Default: 0
    :tt: Temperature controller integration rate (<i>Tt</i>) (&gt;= 0). Default: 0
    :t5: Temperature control time constant (<i>T5</i>) (&gt;= 0). Default: 0
    :af1: Exhaust temperature parameter (<i>Af1</i>).  Unit = PU temperature.  Based on temperature in degrees C. Default: 0.0
    :bf1: (<i>Bf1</i>).  <i>Bf1</i> = <i>E</i>(1 - <i>W</i>) where <i>E</i> (speed sensitivity coefficient) is 0,55 to 0,65 x <i>Tr</i>.  Unit = PU temperature.  Based on temperature in degrees C. Default: 0.0
    :af2: Coefficient equal to 0,5(1-speed) (<i>Af2</i>). Default: 0.0
    :bf2: Turbine torque coefficient K<sub>hhv</sub> (depends on heating value of fuel stream in combustion chamber) (<i>Bf2</i>). Default: 0.0
    :cf2: Coefficient defining fuel flow where power output is 0% (<i>Cf2</i>).  Synchronous but no output.  Typically 0,23 x K<sub>hhv</sub> (23% fuel flow). Default: 0.0
    :tr: Rated temperature (<i>Tr</i>).  Unit = [SYMBOL REMOVED]C depending on parameters<i> Af1 </i>and <i>Bf1</i>. Default: 0.0
    :k6: Minimum fuel flow (<i>K6</i>). Default: 0.0
    :tc: Temperature control (<i>Tc</i>).  Unit = [SYMBOL REMOVED]F or [SYMBOL REMOVED]C depending on parameters <i>Af1</i> and <i>Bf1</i>. Default: 0.0
    """

    cgmesProfile = TurbineGovernorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "mwbase": [
            cgmesProfile.DY.value,
        ],
        "w": [
            cgmesProfile.DY.value,
        ],
        "x": [
            cgmesProfile.DY.value,
        ],
        "y": [
            cgmesProfile.DY.value,
        ],
        "z": [
            cgmesProfile.DY.value,
        ],
        "etd": [
            cgmesProfile.DY.value,
        ],
        "tcd": [
            cgmesProfile.DY.value,
        ],
        "trate": [
            cgmesProfile.DY.value,
        ],
        "t": [
            cgmesProfile.DY.value,
        ],
        "tmax": [
            cgmesProfile.DY.value,
        ],
        "tmin": [
            cgmesProfile.DY.value,
        ],
        "ecr": [
            cgmesProfile.DY.value,
        ],
        "k3": [
            cgmesProfile.DY.value,
        ],
        "a": [
            cgmesProfile.DY.value,
        ],
        "b": [
            cgmesProfile.DY.value,
        ],
        "c": [
            cgmesProfile.DY.value,
        ],
        "tf": [
            cgmesProfile.DY.value,
        ],
        "kf": [
            cgmesProfile.DY.value,
        ],
        "k5": [
            cgmesProfile.DY.value,
        ],
        "k4": [
            cgmesProfile.DY.value,
        ],
        "t3": [
            cgmesProfile.DY.value,
        ],
        "t4": [
            cgmesProfile.DY.value,
        ],
        "tt": [
            cgmesProfile.DY.value,
        ],
        "t5": [
            cgmesProfile.DY.value,
        ],
        "af1": [
            cgmesProfile.DY.value,
        ],
        "bf1": [
            cgmesProfile.DY.value,
        ],
        "af2": [
            cgmesProfile.DY.value,
        ],
        "bf2": [
            cgmesProfile.DY.value,
        ],
        "cf2": [
            cgmesProfile.DY.value,
        ],
        "tr": [
            cgmesProfile.DY.value,
        ],
        "k6": [
            cgmesProfile.DY.value,
        ],
        "tc": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class TurbineGovernorDynamics: \n"
        + TurbineGovernorDynamics.__doc__
    )

    def __init__(
        self,
        mwbase=0.0,
        w=0.0,
        x=0,
        y=0,
        z=0,
        etd=0,
        tcd=0,
        trate=0.0,
        t=0,
        tmax=0.0,
        tmin=0.0,
        ecr=0,
        k3=0.0,
        a=0.0,
        b=0.0,
        c=0.0,
        tf=0,
        kf=0.0,
        k5=0.0,
        k4=0.0,
        t3=0,
        t4=0,
        tt=0,
        t5=0,
        af1=0.0,
        bf1=0.0,
        af2=0.0,
        bf2=0.0,
        cf2=0.0,
        tr=0.0,
        k6=0.0,
        tc=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.etd = etd
        self.tcd = tcd
        self.trate = trate
        self.t = t
        self.tmax = tmax
        self.tmin = tmin
        self.ecr = ecr
        self.k3 = k3
        self.a = a
        self.b = b
        self.c = c
        self.tf = tf
        self.kf = kf
        self.k5 = k5
        self.k4 = k4
        self.t3 = t3
        self.t4 = t4
        self.tt = tt
        self.t5 = t5
        self.af1 = af1
        self.bf1 = bf1
        self.af2 = af2
        self.bf2 = bf2
        self.cf2 = cf2
        self.tr = tr
        self.k6 = k6
        self.tc = tc

    def __str__(self):
        str = "class=GovGAST2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
