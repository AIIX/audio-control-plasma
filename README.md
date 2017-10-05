## Audio-control-plasma
This skill integrates Plasma 5 Desktop Audio Controls with Mycroft which enables users to Increase/Decrease Volume of Master and Capture on the Desktop.

## Description 
#### Installation of skill:
* Download or Clone Git (run: git clone https://github.com/AIIX/audio-control-plasma inside /opt/mycroft/skills)
* Create /opt/mycroft/skills folder if it does not exist
* Extract Downloaded Skill into a folder. "audio-control-plasma". (Clone does not require this step)
* Copy the audio-control-plasma folder to /opt/mycroft/skills/ folder

#### Installation of requirements:
##### Fedora: 
- sudo dnf install dbus-python
- From terminal: cp -R /usr/lib64/python2.7/site-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib64/python2.7/site-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

##### Kubuntu / KDE Neon: 
- sudo apt install python-dbus
- From terminal: cp -R /usr/lib/python2.7/dist-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib/python2.7/dist-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

* For other distributions:
- Python Dbus package is required and copying the Python Dbus folder and lib from your system python install over to /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/.

## Examples
###### Increase Volume
* "Hey Mycroft, increase the volume "
* "Hey Mycroft, increase volume "

###### Maximum Volume
* "Hey Mycroft, increase to maximum volume "
* "Hey Mycroft, maximum volume "

###### Decrease Volume
* "Hey Mycroft, decrease the volume "
* "Hey Mycroft, decrease volume "

###### Minimum Volume
* "Hey Mycroft, decrease to minimum volume "
* "Hey Mycroft, minimum volume "

###### Increase Microphone
* "Hey Mycroft, increase the microphone volume "
* "Hey Mycroft, increase microphone volume " 

###### Maximum Microphone
* "Hey Mycroft, increase microphone to maximum volume "
* "Hey Mycroft, maximum microphone volume "

###### Decrease Microphone
* "Hey Mycroft, decrease the microphone volume "
* "Hey Mycroft, decrease microphone volume "

###### Minimum Microphone
* "Hey Mycroft, decrease microphone to minimum volume "
* "Hey Mycroft, minimum microphone volume "

## Credits 
(AIX) Aditya Mehra
