# Asl-to-Speech

Asl-to-Speech is a wearable technology that translates American Sign Language (ASL) into speech. The goal of this project is to help people to facilitate communication using sign language. This project is able to translate numbers from 1 to 5. The code offers flexibility to add more numbers and letters if the user wishes to.

## How it works

The [Leap Motion Controller](https://www.leapmotion.com/) uses infrared cameras to track the movement of your hands and fingers. In this project, hand gestures are picked up by the Leap Motion and are translated into text. The text is then translated into speech by Nuance's speech platform.

This project also has the option to use the [Myo gesture control armband](https://myo.com) to translate arm gestures into speech.

## Demo

Click to watch a short video demo:

[![Demo video](https://i.ytimg.com/vi_webp/cIiL2D15OzA/mqdefault.webp)](https://www.youtube.com/watch?v=cIiL2D15OzA)

## Components

### Windows Machine (For now)

#### Hardware Requirements

* [Leap Motion Controller](https://www.leapmotion.com/)
* [Myo gesture control armband](https://myo.com)

#### Software Requirements

* [Python 2.7.10](https://www.python.org/downloads/)
* [Python 3.5.0](https://www.python.org/downloads/)
* [Leap Motion Installer & SDK](https://developer.leapmotion.com/downloads/skeletal-beta?platform=windows&version=2.3.1.31549)
* [Myo Client and SDK](https://developer.thalmic.com/downloads)
* [Nuance's Text-to-Speech API](https://developer.nuance.com/public/index.php?task=account)

#### Walkthrough

1. Installing Python 2.7.10 and Python 3.5.10
2. Set up Nuance's Text-to-Speech API
3. Installing Leap Motion Installer & SDK
4. Installing Myo Client and SDK
5. Starting coding

#### Python 2.7.10 and Python 3.5.1

* Go to the link https://www.python.org/downloads/ 
* Download Python **2.7.10** installer and install
* Download Python **3.5.0** installer and install
* Press *Start** and click on **Control Panel**
* Click on **System and Security** then **System**
* Click on **Advanced system settings**
* Click on **Environment Variables** in the **Advanced** tab
You should see this at this point
![Alt](http://puu.sh/lxCVS/b136c76aea.png)
* Click on the variable **Path** then click on **Edit**
* Add at the end of the **Variable value** a **;** if it does not have one
* Add **C:\Python27;C:\Python27\Scripts;C:\Python35;C:\Python35\Scripts;** after the **;**
Make sure the paths **C:\Python27**, **C:\Python27\Scripts**, **C:\Python35**, **C:\Python35\Scripts** exist on your computer
![Alt](http://puu.sh/lxD7D/0be92a4ef9.png)

#### Nuance's Text-to-Speech API

* Sign up a developper account on https://developer.nuance.com/public/index.php?task=home
* Click on **my account**
* Click on **Sandbox Credentials**
* Copy the ID from the **ANDROID section** and save it somewhere on your computer. We will need it later. The ID look something like this: "ABCDEFG_youremail_email_com_20151111002244"
* Copy the **HTTP Client Applications** key from the same page also save it somewhere on your computer. The app key looks something like this: c7db49a73431f7b33kf408abc4eba7062c339f37bd66ee2d7a3a3109fede0dc6b9566ded8865a0ba4b396510240d165040b688fd1c762b96b15c9faf3aac75f3

#### Leap Motion Installer & SDK

* Go to [Leap Motion](https://developer.leapmotion.com/downloads/skeletal-beta?platform=windows&version=2.3.1.31549)'s website and install the **SDK**.

#### Myo Client and SDK

* Go to [Myo](https://developer.thalmic.com/downloads)'s website and install the **Myo Connect** and **SDK**.

#### Setting Up the project 

* Download this [project](https://github.com/imbaky/Asl-to-Speech/archive/master.zip)
* Extract on **Desktop**
* Open command prompt (Click on **Start**, search for "**cmd**" and click on it)
* Write this command on command prompt

  ```
    cd Desktop\Asl-to-Speech
  ```
* Write this command on command prompt

  ```
    pip install -r pip_requirements.txt
  ```
  
  It is normal if you get the following error: 
  ```
    Command "python setup.py egg_info" failed with error code 1 in c:\users\[username]\appdata\local\temp\pip-build-syvzsr\aiohttp"
  ```
  
* Write this command on command prompt

  ```
    pip3 install -r pip_requirements.txt
  ```

* Write this command on command prompt to open notepad

  ```
    notepad
  ```

* Paste the following inside notepad 

  ```
    {
       "app_id": "",
       "app_key": ""
    }  
  ```

* Add the app **ID** and **key** inside the double quotes ("") that you saved before

* Press **ctrl** + **s**

* Change the **File name** "\*.txt" to **creds.json**

* Change the **Save as type** "Text Document(\*.txt)" to **All Files**

* You can now test the speech module (Make sure your speaker is turned on)

  ```
    py -3 tts.py creds.json "Hello, how are you?" output.pcm
  ```

If you hear "Hello, how are you?" then it is working

  
At this point, all the set ups should work and you can start to code.





