from modules import cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase

@cbpi.actor
class SampleActor(ActorBase):
    #custom property 
    prop1 = Property.Text("Property1", True, "1")
    
    def on(self, power=0):
        print "SWITCH ON %s" % (self.prop1)
        
    def off(self, power=0):
        print "SWITCH OFF "


