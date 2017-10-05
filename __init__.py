import sys
import dbus
import math
import subprocess
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)

class AudioControlPlasmaDesktopSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(AudioControlPlasmaDesktopSkill, self).__init__(name="AudioControlPlasmaDesktopSkill")
        
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))
        
        audiocontrol_increasevolume_plasma_skill_intent = IntentBuilder("IncreaseVolumeKeywordIntent").\
            require("InternalIncreaseVolumeDesktopKeyword").build()
        self.register_intent(audiocontrol_increasevolume_plasma_skill_intent, self.handle_audiocontrol_increasevolume_plasma_skill_intent)
        
        audiocontrol_decreasevolume_plasma_skill_intent = IntentBuilder("DecreaseVolumeKeywordIntent").\
            require("InternalDecreaseVolumeDesktopKeyword").build()
        self.register_intent(audiocontrol_decreasevolume_plasma_skill_intent, self.handle_audiocontrol_decreasevolume_plasma_skill_intent)

        audiocontrol_maximumvolume_plasma_skill_intent = IntentBuilder("MaximumVolumeKeywordIntent").\
            require("InternalMaximumVolumeDesktopKeyword").build()
        self.register_intent(audiocontrol_maximumvolume_plasma_skill_intent, self.handle_audiocontrol_maximumvolume_plasma_skill_intent)
        
        audiocontrol_minimumvolume_plasma_skill_intent = IntentBuilder("MinimumVolumeKeywordIntent").\
            require("InternalMinimumVolumeDesktopKeyword").build()
        self.register_intent(audiocontrol_minimumvolume_plasma_skill_intent, self.handle_audiocontrol_minimumvolume_plasma_skill_intent)
        
        audiocontrol_increasemic_plasma_skill_intent = IntentBuilder("IncreaseMicKeywordIntent").\
            require("InternalIncreaseMicDesktopKeyword").build()
        self.register_intent(audiocontrol_increasemic_plasma_skill_intent, self.handle_audiocontrol_increasemic_plasma_skill_intent)
        
        audiocontrol_decreasemic_plasma_skill_intent = IntentBuilder("DecreaseMicKeywordIntent").\
            require("InternalDecreaseMicDesktopKeyword").build()
        self.register_intent(audiocontrol_decreasemic_plasma_skill_intent, self.handle_audiocontrol_decreasemic_plasma_skill_intent)

        audiocontrol_maximummic_plasma_skill_intent = IntentBuilder("MaximumMicKeywordIntent").\
            require("InternalMaximumMicDesktopKeyword").build()
        self.register_intent(audiocontrol_maximummic_plasma_skill_intent, self.handle_audiocontrol_maximummic_plasma_skill_intent)
        
        audiocontrol_minimummic_plasma_skill_intent = IntentBuilder("MinimumMicKeywordIntent").\
            require("InternalMinimumMicDesktopKeyword").build()
        self.register_intent(audiocontrol_minimummic_plasma_skill_intent, self.handle_audiocontrol_minimummic_plasma_skill_intent)

    def handle_audiocontrol_increasevolume_plasma_skill_intent(self, message):
        cmd = ["amixer get Capture | awk '$0~/%/{print $4}' | tr -d '[]%'"]
        get_master_volume =  subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        for line in get_master_volume.stdout:
            master_volume = line.join(line.split())
            master_volume = int(master_volume)
            flat_master_volume = self.roundup(master_volume)
            if flat_master_volume >= 0 and flat_master_volume <= 100:
                flat_master_volume += 20
                increasevol = ["amixer sset Master %s" % flat_master_volume]
                subprocess.Popen(increasevol, stdout=subprocess.PIPE, shell=True)
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.kde.plasmashell","/org/kde/osdService")
                remote_object.volumeChanged(flat_master_volume, dbus_interface = "org.kde.osdService")
                
    def handle_audiocontrol_decreasevolume_plasma_skill_intent(self, message):
        cmd = ["amixer get Master | awk '$0~/%/{print $4}' | tr -d '[]%'"]
        get_master_volume =  subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        for line in get_master_volume.stdout:
            master_volume = line.join(line.split())
            master_volume = int(master_volume)
            flat_master_volume = self.roundup(master_volume)
            if flat_master_volume >= 0 and flat_master_volume <= 100:
                flat_master_volume -= 20
                decreasevol = ["amixer sset Master %s" % flat_master_volume]
                subprocess.Popen(decreasevol, stdout=subprocess.PIPE, shell=True)
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.kde.plasmashell","/org/kde/osdService")
                remote_object.volumeChanged(flat_master_volume, dbus_interface = "org.kde.osdService")
                
    def handle_audiocontrol_maximumvolume_plasma_skill_intent(self, message):
        flat_master_volume = 100
        increasevol = ["amixer sset Master %s" % flat_master_volume]
        subprocess.Popen(increasevol, stdout=subprocess.PIPE, shell=True)
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/org/kde/osdService")
        remote_object.volumeChanged(flat_master_volume, dbus_interface = "org.kde.osdService")
        
    def handle_audiocontrol_minimumvolume_plasma_skill_intent(self, message):
        flat_master_volume = 10
        increasevol = ["amixer sset Master %s" % flat_master_volume]
        subprocess.Popen(increasevol, stdout=subprocess.PIPE, shell=True)
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/org/kde/osdService")
        remote_object.volumeChanged(flat_master_volume, dbus_interface = "org.kde.osdService")
        
    def handle_audiocontrol_increasemic_plasma_skill_intent(self, message):
        cmd = ["amixer get Capture | awk '$0~/%/{print $4}' | tr -d '[]%'"]
        get_master_volume =  subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        for line in get_master_volume.stdout:
            master_volume = line.join(line.split())
            master_volume = int(master_volume)
            flat_master_volume = self.roundup(master_volume)
            if flat_master_volume >= 0 and flat_master_volume <= 100:
                flat_master_volume += 20
                increasevol = ["amixer sset Capture %s" % flat_master_volume]
                subprocess.Popen(increasevol, stdout=subprocess.PIPE, shell=True)
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.kde.plasmashell","/org/kde/osdService") 
                remote_object.captureVolumeChanged(flat_master_volume, dbus_interface = "org.kde.osdService")
                
    def handle_audiocontrol_decreasemic_plasma_skill_intent(self, message):
        cmd = ["amixer get Capture | awk '$0~/%/{print $4}' | tr -d '[]%'"]
        get_master_volume =  subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        for line in get_master_volume.stdout:
            master_volume = line.join(line.split())
            master_volume = int(master_volume)
            flat_master_volume = self.roundup(master_volume)
            if flat_master_volume >= 0 and flat_master_volume <= 100:
                flat_master_volume -= 20
                decreasevol = ["amixer sset Capture %s" % flat_master_volume]
                subprocess.Popen(decreasevol, stdout=subprocess.PIPE, shell=True)
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.kde.plasmashell","/org/kde/osdService") 
                remote_object.captureVolumeChanged(flat_master_volume, dbus_interface = "org.kde.osdService")
                
    def handle_audiocontrol_maximummic_plasma_skill_intent(self, message):
        flat_master_volume = 100
        increasevol = ["amixer sset Capture %s" % flat_master_volume]
        subprocess.Popen(increasevol, stdout=subprocess.PIPE, shell=True)
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/org/kde/osdService") 
        remote_object.captureVolumeChanged(flat_master_volume, dbus_interface = "org.kde.osdService")
        
    def handle_audiocontrol_minimummic_plasma_skill_intent(self, message):
        flat_master_volume = 10
        increasevol = ["amixer sset Capture %s" % flat_master_volume]
        subprocess.Popen(increasevol, stdout=subprocess.PIPE, shell=True)
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/org/kde/osdService")
        remote_object.captureVolumeChanged(flat_master_volume, dbus_interface = "org.kde.osdService")
                
    def roundup(self, x):
        rem = x % 10
        if rem < 5:
            x = int(x / 10) * 10
        else:
            x = int((x + 10) / 10) * 10
        return x

    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return AudioControlPlasmaDesktopSkill()
