from q1.vehicle_classes import Motorised, Aircraft

ford = Motorised("Ford", 4, None) # Put none as the engine type as one was not given

boeing = Aircraft("Boeing", 3 , "Kerosene")
boeing.switchOn()
boeing.takeOff()
