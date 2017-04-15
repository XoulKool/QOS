# QOS
Here we implement control with Ryu using a Quality-of-Service(QOS) technique

Much like the previous two tests, we will be using five terminals at a time.  The Pica8 OVS terminal, grnlntrn, and servers5-7.  
Again, before starting this test be sure to delete flow table entries using the command specified prior.  

##This test uses OpenFlow 1.3
So, be sure to use the command 

`ovs-vsctl set Bridge br0 protocols=OpenFlow13`

In this Pica8 terminal to allow the switch to use the controller applications we will be using.

What this test does is implements bandwidth control using flow-queueing.  The 'test' is more or less just using wireshark to ensure that we can in fact demonstrate bandwidth control using an Ryu controller on this switch.  This test also demonstrates how flawlessly we can call functions at any time to implement this control, which is extremely useful in a commercial setting.

To start, activate both server python files on server5 and server7.  That is run command

`python PServer1.py`

on server5 and 

`python PServer2.py`

on server6

Then on the grnlntrn terminal run

`ryu-manager --verbose qos13.py`

Once the terminal sas it has entered main mode, activate parclient.py on server7 by running

`python parclient.py`

Now we can analyze what goes on by running wireshark as a background process on the servers which are getting information.

