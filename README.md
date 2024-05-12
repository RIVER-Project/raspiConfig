Raspberry Pi Configuration Script

This script facilitates setting up permissions and executing configuration steps for your Raspberry Pi. 
Please follow the manual instructions provided below.

Instructions:

Enable I2C:
Follow the official Raspberry Pi documentation to enable I2C manually.
Once enabled, you can communicate with the PWM hat.

Enable SSH:
Follow the official Raspberry Pi documentation to enable SSH manually.

Manual Setup:

Ensure that the user you created at startup is named "raspi".

Unzip the contents of this folder onto your Raspberry Pi.
Open the terminal and navigate to the folder containing the extracted files.

Set Permissions:

Run the following command to ensure proper permissions:
sudo chmod 777 raspiConfig.sh

Execute the configuration script by running:
./raspiConfig.sh

Follow the prompts to complete the setup process.

Troubleshooting:
If you encounter any issues during the setup process, refer to the official Raspberry Pi documentation or seek assistance from the Raspberry Pi community forums.
