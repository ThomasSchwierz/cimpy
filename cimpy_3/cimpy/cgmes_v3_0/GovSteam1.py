from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteam1(TurbineGovernorDynamics):
    """
    Steam turbine governor, based on the GovSteamIEEE1 (with optional deadband and nonlinear valve gain added).

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :k: Governor gain (reciprocal of droop) (<i>K</i>) (&gt; 0).  Typical value = 25. Default: 0.0
    :t1: Governor lag time constant (<i>T1</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :t2: Governor lead time constant (<i>T2</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :t3: Valve positioner time constant (<i>T3) </i>(&gt; 0).  Typical value = 0,1. Default: 0
    :uo: Maximum valve opening velocity (<i>Uo</i>) (&gt; 0).  Unit = PU / s.  Typical value = 1. Default: 0.0
    :uc: Maximum valve closing velocity (<i>Uc</i>) (&lt; 0).  Unit = PU / s.  Typical value = -10. Default: 0.0
    :pmax: Maximum valve opening (<i>Pmax</i>) (&gt; GovSteam1.pmin).  Typical value = 1. Default: 0.0
    :pmin: Minimum valve opening (<i>Pmin</i>) (&gt;= 0 and &lt; GovSteam1.pmax).  Typical value = 0. Default: 0.0
    :t4: Inlet piping/steam bowl time constant (<i>T4</i>) (&gt;= 0).  Typical value = 0,3. Default: 0
    :k1: Fraction of HP shaft power after first boiler pass (<i>K1</i>).  Typical value = 0,2. Default: 0.0
    :k2: Fraction of LP shaft power after first boiler pass (<i>K2</i>).  Typical value = 0. Default: 0.0
    :t5: Time constant of second boiler pass (<i>T5</i>) (&gt;= 0).  Typical value = 5. Default: 0
    :k3: Fraction of HP shaft power after second boiler pass (<i>K3</i>).  Typical value = 0,3. Default: 0.0
    :k4: Fraction of LP shaft power after second boiler pass (<i>K4</i>).  Typical value = 0. Default: 0.0
    :t6: Time constant of third boiler pass (<i>T6</i>) (&gt;= 0).  Typical value = 0,5. Default: 0
    :k5: Fraction of HP shaft power after third boiler pass (<i>K5</i>).  Typical value = 0,5. Default: 0.0
    :k6: Fraction of LP shaft power after third boiler pass (<i>K6</i>).  Typical value = 0. Default: 0.0
    :t7: Time constant of fourth boiler pass (<i>T7</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :k7: Fraction of HP shaft power after fourth boiler pass (<i>K7</i>).  Typical value = 0. Default: 0.0
    :k8: Fraction of LP shaft power after fourth boiler pass (<i>K8</i>).  Typical value = 0. Default: 0.0
    :db1: Intentional deadband width (<i>db1</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :eps: Intentional db hysteresis (<i>eps</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :sdb1: Intentional deadband indicator. true = intentional deadband is applied false = intentional deadband is not applied. Typical value = true. Default: False
    :sdb2: Unintentional deadband location. true = intentional deadband is applied before point `A` false = intentional deadband is applied after point `A`. Typical value = true. Default: False
    :db2: Unintentional deadband (<i>db2</i>).  Unit = MW.  Typical value = 0. Default: 0.0
    :valve: Nonlinear valve characteristic. true = nonlinear valve characteristic is used false = nonlinear valve characteristic is not used. Typical value = true. Default: False
    :gv1: Nonlinear gain valve position point 1 (<i>GV1</i>).  Typical value = 0. Default: 0.0
    :pgv1: Nonlinear gain power value point 1 (<i>Pgv1</i>).  Typical value = 0. Default: 0.0
    :gv2: Nonlinear gain valve position point 2 (<i>GV2</i>).  Typical value = 0,4. Default: 0.0
    :pgv2: Nonlinear gain power value point 2 (<i>Pgv2</i>).  Typical value = 0,75. Default: 0.0
    :gv3: Nonlinear gain valve position point 3 (<i>GV3</i>).  Typical value = 0,5. Default: 0.0
    :pgv3: Nonlinear gain power value point 3 (<i>Pgv3</i>).  Typical value = 0,91. Default: 0.0
    :gv4: Nonlinear gain valve position point 4 (<i>GV4</i>).  Typical value = 0,6. Default: 0.0
    :pgv4: Nonlinear gain power value point 4 (<i>Pgv4</i>).  Typical value = 0,98. Default: 0.0
    :gv5: Nonlinear gain valve position point 5 (<i>GV5</i>).  Typical value = 1. Default: 0.0
    :pgv5: Nonlinear gain power value point 5 (<i>Pgv5</i>).  Typical value = 1. Default: 0.0
    :gv6: Nonlinear gain valve position point 6 (<i>GV6</i>).  Typical value = 0. Default: 0.0
    :pgv6: Nonlinear gain power value point 6 (<i>Pgv6</i>).  Typical value = 0. Default: 0.0
    """

    cgmesProfile = TurbineGovernorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "mwbase": [
            cgmesProfile.DY.value,
        ],
        "k": [
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
        "uo": [
            cgmesProfile.DY.value,
        ],
        "uc": [
            cgmesProfile.DY.value,
        ],
        "pmax": [
            cgmesProfile.DY.value,
        ],
        "pmin": [
            cgmesProfile.DY.value,
        ],
        "t4": [
            cgmesProfile.DY.value,
        ],
        "k1": [
            cgmesProfile.DY.value,
        ],
        "k2": [
            cgmesProfile.DY.value,
        ],
        "t5": [
            cgmesProfile.DY.value,
        ],
        "k3": [
            cgmesProfile.DY.value,
        ],
        "k4": [
            cgmesProfile.DY.value,
        ],
        "t6": [
            cgmesProfile.DY.value,
        ],
        "k5": [
            cgmesProfile.DY.value,
        ],
        "k6": [
            cgmesProfile.DY.value,
        ],
        "t7": [
            cgmesProfile.DY.value,
        ],
        "k7": [
            cgmesProfile.DY.value,
        ],
        "k8": [
            cgmesProfile.DY.value,
        ],
        "db1": [
            cgmesProfile.DY.value,
        ],
        "eps": [
            cgmesProfile.DY.value,
        ],
        "sdb1": [
            cgmesProfile.DY.value,
        ],
        "sdb2": [
            cgmesProfile.DY.value,
        ],
        "db2": [
            cgmesProfile.DY.value,
        ],
        "valve": [
            cgmesProfile.DY.value,
        ],
        "gv1": [
            cgmesProfile.DY.value,
        ],
        "pgv1": [
            cgmesProfile.DY.value,
        ],
        "gv2": [
            cgmesProfile.DY.value,
        ],
        "pgv2": [
            cgmesProfile.DY.value,
        ],
        "gv3": [
            cgmesProfile.DY.value,
        ],
        "pgv3": [
            cgmesProfile.DY.value,
        ],
        "gv4": [
            cgmesProfile.DY.value,
        ],
        "pgv4": [
            cgmesProfile.DY.value,
        ],
        "gv5": [
            cgmesProfile.DY.value,
        ],
        "pgv5": [
            cgmesProfile.DY.value,
        ],
        "gv6": [
            cgmesProfile.DY.value,
        ],
        "pgv6": [
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
        k=0.0,
        t1=0,
        t2=0,
        t3=0,
        uo=0.0,
        uc=0.0,
        pmax=0.0,
        pmin=0.0,
        t4=0,
        k1=0.0,
        k2=0.0,
        t5=0,
        k3=0.0,
        k4=0.0,
        t6=0,
        k5=0.0,
        k6=0.0,
        t7=0,
        k7=0.0,
        k8=0.0,
        db1=0.0,
        eps=0.0,
        sdb1=False,
        sdb2=False,
        db2=0.0,
        valve=False,
        gv1=0.0,
        pgv1=0.0,
        gv2=0.0,
        pgv2=0.0,
        gv3=0.0,
        pgv3=0.0,
        gv4=0.0,
        pgv4=0.0,
        gv5=0.0,
        pgv5=0.0,
        gv6=0.0,
        pgv6=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.k = k
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.uo = uo
        self.uc = uc
        self.pmax = pmax
        self.pmin = pmin
        self.t4 = t4
        self.k1 = k1
        self.k2 = k2
        self.t5 = t5
        self.k3 = k3
        self.k4 = k4
        self.t6 = t6
        self.k5 = k5
        self.k6 = k6
        self.t7 = t7
        self.k7 = k7
        self.k8 = k8
        self.db1 = db1
        self.eps = eps
        self.sdb1 = sdb1
        self.sdb2 = sdb2
        self.db2 = db2
        self.valve = valve
        self.gv1 = gv1
        self.pgv1 = pgv1
        self.gv2 = gv2
        self.pgv2 = pgv2
        self.gv3 = gv3
        self.pgv3 = pgv3
        self.gv4 = gv4
        self.pgv4 = pgv4
        self.gv5 = gv5
        self.pgv5 = pgv5
        self.gv6 = gv6
        self.pgv6 = pgv6

    def __str__(self):
        str = "class=GovSteam1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
