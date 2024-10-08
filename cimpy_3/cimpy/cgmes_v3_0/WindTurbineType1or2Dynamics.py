from .DynamicsFunctionBlock import DynamicsFunctionBlock


class WindTurbineType1or2Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines type 1 and type 2 and their control models.  Generator model for wind turbine of type 1 or type 2 is a standard asynchronous generator model.

    :RemoteInputSignal: Remote input signal used by this wind generator type 1 or type 2 model. Default: None
    :AsynchronousMachineDynamics: Asynchronous machine model with which this wind generator type 1 or type 2 model is associated. Default: None
    """

    cgmesProfile = DynamicsFunctionBlock.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "RemoteInputSignal": [
            cgmesProfile.DY.value,
        ],
        "AsynchronousMachineDynamics": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class DynamicsFunctionBlock: \n"
        + DynamicsFunctionBlock.__doc__
    )

    def __init__(
        self, RemoteInputSignal=None, AsynchronousMachineDynamics=None, *args, **kw_args
    ):
        super().__init__(*args, **kw_args)

        self.RemoteInputSignal = RemoteInputSignal
        self.AsynchronousMachineDynamics = AsynchronousMachineDynamics

    def __str__(self):
        str = "class=WindTurbineType1or2Dynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
