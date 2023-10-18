# answerCall.py
# by _______

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function defintion: answerCall()
def answerCall(caller_code, sameAreaCode, cur_time):
    response = False
    time = cur_time.split(":")
    hour = int(time[0])
    if hour <= 6 or hour >= 22: 
        return False
    if caller_code == "T":
        return False 
    if sameAreaCode: 
        return True
    if caller_code== "F" or caller_code== "R":
        return True
    return response
    
    

# Make sure it returns a value

if __name__ == '__main__':
    answerCall(sameAreaCode=True)
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
