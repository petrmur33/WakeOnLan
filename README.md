WakeOnLan
=========

Console utility for broadcasting Wake On Lan messages

Usage
-----

python3 -m main \<MAC address\> - sends WakeOnLan broadcast with specified MAC address
MAC address must be six bytes in hex each separated with ':' symbol. You can use both upper and lower case.
This utility doesn't verify MAC address, so invalid MAC can cause some unexpected things
