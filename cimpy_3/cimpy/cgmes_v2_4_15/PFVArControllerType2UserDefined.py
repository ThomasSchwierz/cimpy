from cimpy.cgmes_v2_4_15.PFVArControllerType2Dynamics import (
    PFVArControllerType2Dynamics,
)


class PFVArControllerType2UserDefined(PFVArControllerType2Dynamics):
    """
    Power Factor or VAr controller Type II function block whose dynamic behaviour is described by

    :proprietary: Behaviour is based on proprietary model as opposed to detailed model. true = user-defined model is proprietary with behaviour mutually understood by sending and receiving applications and parameters passed as general attributes false = user-defined model is explicitly defined in terms of control blocks and their input and output signals. Default: False
    :ProprietaryParameterDynamics: Parameter of this proprietary user-defined model. Default: "list"
    """

    cgmesProfile = PFVArControllerType2Dynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "proprietary": [
            cgmesProfile.DY.value,
        ],
        "ProprietaryParameterDynamics": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PFVArControllerType2Dynamics: \n"
        + PFVArControllerType2Dynamics.__doc__
    )

    def __init__(
        self, proprietary=False, ProprietaryParameterDynamics="list", *args, **kw_args
    ):
        super().__init__(*args, **kw_args)

        self.proprietary = proprietary
        self.ProprietaryParameterDynamics = ProprietaryParameterDynamics

    def __str__(self):
        str = "class=PFVArControllerType2UserDefined\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
