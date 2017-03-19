# ***************************************************************
# * Check to see if root CA file exists, download if not        *
# ***************************************************************

if [ ! -f ./root-CA.crt ]; then
  printf "\nDownloading AWS IoT Root CA certificate from Symantec...\n"
  curl https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem > root-CA.crt
else
  printf "\nroot CA file exists...\n"	
fi

# ***************************************************************
# * install AWS Device SDK for Python if not already installed  *
# ***************************************************************

if [ ! -d ./aws-iot-device-sdk-python ]; then
  printf "\nInstalling AWS SDK...\n"
  git clone https://github.com/aws/aws-iot-device-sdk-python.git
  cd aws-iot-device-sdk-python
  python setup.py install
fi