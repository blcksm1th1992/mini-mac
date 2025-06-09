import pyrad.packet
from pyrad.client import Client
from pyrad.dictionary import Dictionary

srv = Client(server="localhost", secret=b"testing123", dict=Dictionary("dict"))
req = srv.CreateAuthPacket(code=pyrad.packet.AccessRequest, User_Name="testuser")
req["User-Password"] = req.PwCrypt("testpassword")

reply = srv.SendPacket(req)
print("Reply Code:", reply.code)
for attr in reply.keys():
    print(f"{attr}: {reply[attr]}")
