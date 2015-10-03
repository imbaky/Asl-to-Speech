import os, inspect, sys, thread, time

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

__author__ = "Edward Tran"
__version__ = "1.0.0"


class SignListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
    	print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE); 

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"    

    def on_exit(self, controller):
        print "Exited"     

	def state_string(self, state):
	    if state == Leap.Gesture.STATE_START:
	        return "STATE_START"

		if state == Leap.Gesture.STATE_UPDATE:
			return "STATE_UPDATE"

		if state == Leap.Gesture.STATE_STOP:
			return "STATE_STOP"

		if state == Leap.Gesture.STATE_INVALID:
			return "STATE_INVALID"    
			
    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
		frame = controller.frame()

		for hand in frame.hands:
			handType = "Left hand" if hand.is_left else "Right hand"
		 	
		 	# Number One
			if (is_hand_right(hand.is_right)*hand.fingers[0].direction.x) > 0\
				and hand.fingers[1].direction.y > 0\
				and hand.fingers[2].direction.y < 0\
				and hand.fingers[3].direction.y < 0\
				and hand.fingers[4].direction.y < 0:
				print "One"
			# Number Two
			elif (is_hand_right(hand.is_right)*hand.fingers[0].direction.x) > 0\
				and hand.fingers[1].direction.y > 0\
				and hand.fingers[2].direction.y > 0\
				and hand.fingers[3].direction.y < 0\
				and hand.fingers[4].direction.y < 0:
				print "Two"		
			# Number Three		
			elif (is_hand_right(hand.is_right)*hand.fingers[0].direction.x) < 0\
				and hand.fingers[0].direction.y > 0\
				and hand.fingers[1].direction.y > 0\
				and hand.fingers[2].direction.y > 0\
				and hand.fingers[3].direction.y < 0\
				and hand.fingers[4].direction.y < 0:
				print "Three"						
			# Number Four	
			elif (is_hand_right(hand.is_right)*hand.fingers[0].direction.x) > 0\
				and hand.fingers[1].direction.y > 0\
				and hand.fingers[2].direction.y > 0\
				and hand.fingers[3].direction.y > 0\
				and hand.fingers[4].direction.y > 0:
				print "Four"	
			# Number Five
			elif (is_hand_right(hand.is_right)*hand.fingers[0].direction.x) < 0\
				and hand.fingers[0].direction.y > 0\
				and hand.fingers[1].direction.y > 0\
				and hand.fingers[2].direction.y > 0\
				and hand.fingers[3].direction.y > 0\
				and hand.fingers[4].direction.y > 0:
				print "Five"	
			# Number Six
			elif (is_hand_right(hand.is_right)*hand.fingers[0].direction.x) > 0\
				and hand.fingers[0].direction.y > 0\
				and hand.fingers[1].direction.y > 0\
				and hand.fingers[2].direction.y > 0\
				and hand.fingers[3].direction.y > 0\
				and (is_hand_right(hand.is_right)*hand.fingers[4].direction.x) < 0\
				and hand.fingers[4].direction.y < 0:
				print "Six"			
			# Number Seven
			elif (is_hand_right(hand.is_right)*hand.fingers[0].direction.x) > 0\
				and hand.fingers[0].direction.y > 0\
				and hand.fingers[1].direction.y > 0\
				and hand.fingers[2].direction.y > 0\
				and hand.fingers[3].direction.y < 0\
				and hand.fingers[4].direction.y > 0:
				print "Seven"	
			# Number Eight
			elif (is_hand_right(hand.is_right)*hand.fingers[0].direction.x) > 0\
				and hand.fingers[1].direction.y > 0\
				and hand.fingers[2].direction.y < 0\
				and hand.fingers[3].direction.y > 0\
				and hand.fingers[4].direction.y > 0:
				print "Eight"	
			# Number Nine
			elif (is_hand_right(hand.is_right)*hand.fingers[0].direction.x) < 0\
				and hand.fingers[0].direction.y > 0\
				and hand.fingers[1].direction.y < 0\
				and hand.fingers[2].direction.y > 0\
				and hand.fingers[3].direction.y > 0\
				and hand.fingers[4].direction.y > 0:
				print "Nine"												
			else:
				print "Did not detect anything"

def is_hand_right(isRight):
	if isRight:
		return 1
	else:
		return -1

def main():
	# Create a sample listener and controller
	listener = SignListener()
	controller = Leap.Controller()

	# Have the sample listener receive events from the controller
	controller.add_listener(listener)

	print "Press Enter to quit..."
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)

if __name__ == "__main__":
	main()