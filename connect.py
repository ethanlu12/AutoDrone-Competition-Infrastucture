import asyncio
import qtm
from pynput import keyboard
from rover import Rover
from random import randint


def on_packet(packet):
    """ Callback function that is called everytime a data packet arrives from QTM """
    print("Framenumber: {}".format(packet.framenumber))
    header, markers = packet.get_3d_markers()
    print("Component info: {}".format(header))
    for marker in markers:
        print("\t", marker)


async def setup(address):
    """ Main function """
    connection = await qtm.connect(address)
    if connection is None:
        return

    await connection.stream_frames(components=["3d"], on_packet=on_packet)


if __name__ == "__main__":
    address = str(input("enter QTM computer's address:"))
    asyncio.ensure_future(setup(address))
    asyncio.get_event_loop().run_forever()
    freenove = Rover()
    current_moveset = randint(0,3) #in the case that we have 4 movement set
    iterations = 5 #in the case we want rover to execute 5 movement set
    abort_flag = False
    while abort_flag == False:
        for index in range(iterations - 1):
            freenove.execute_path(current_moveset)
            current_moveset = randint(0,3)
            if keyboard.is_pressed("esc"):
                print("\nstoping the program, escaped is pressed")
                abort_flag = True

            
    
