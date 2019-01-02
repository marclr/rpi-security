# rpi-security
Raspberry Pi detection with Telegram messaging


# Install
1. Install Raspbian (https://www.raspbian.org/)
3. Connect via ssh to the Raspberry
2. (Optional) Assign a static ip
    1. `sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.bak`
    2. `sudo nano /etc/dhcpcd.conf`
    3. Define your static ip, for example:
    ```
        interface wlan0
        static ip_address=192.168.1.50/24
        static routers=192.168.1.1
     ```
4. Download and install the motion software
    1. `wget https://github.com/Motion-Project/motion/releases/download/release-4.1.1/pi_stretch_motion_4.1.1-1_armhf.deb`
    2. `sudo apt-get install gdebi-core`
    3. `sudo gdebi pi_stretch_motion_4.1.1-1_armhf.deb`
4. Load the raspicam module
    1. `sudo nano /etc/modules`
    2. put `bcm2835-v4l2`
    3. save and exit the file
    4. `sudo reboot`
5. Backup the original motion.conf file
    1. `cd /etc/motion`
    2. `cp motion.conf motion.conf.bak`
    3. Modify the parameters as suggested: 
        - Uncomment the `mmalcam_name vc.ril.camera` parameter.
        - Uncomment `target_dir` and change it's associated value to `/tmp/motion`
        - Ensure that `ffmpeg_output_movies` is set to `off`
        - Set `stream_localhost` to `off`
        - Set `webcontrol_localhost` to `off`
        - Additional parameters on the [website](https://motion-project.github.io/motion_config.html)
     4. Add motion as a background service
        - `sudo nano /etc/default/motion`
        - change the value of `start_motion_daemon` to `yes`
 6. Clone this sourcecode and install dependencies
    1. `git clone https://github.com/marclr/rpi-security.git`
    2. `cd rpi-security`
    3. `pip3 install -r requirements`
    4. Modify the `config/rpi-security.conf` to set your token and your chat_id
 7. Create the service
    1. Copy the file in `service` folder to `/etc/systemd/system`
    2. Execute `service rpi start`
    
 8. Reboot and check it's working   
