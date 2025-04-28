import os
import cv2

cap = cv2.VideoCapture(0)
directory = 'Image'

# Create directories if they don't exist
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    os.makedirs(os.path.join(directory, char), exist_ok=True)

while True:
    _, frame = cap.read()
    count = {}
    for char in "abcdefghijklmnopqrstuvwxyz0123456789":
        count[char] = len(os.listdir(os.path.join(directory, char.upper())))

    cv2.putText(frame, "a : " + str(count['a']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "b : " + str(count['b']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "c : " + str(count['c']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "d : " + str(count['d']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "e : " + str(count['e']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "f : " + str(count['f']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "g : " + str(count['g']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "h : " + str(count['h']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "i : " + str(count['i']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "j : " + str(count['j']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "k : " + str(count['k']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "l : " + str(count['l']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "m : " + str(count['m']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "n : " + str(count['n']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "o : " + str(count['o']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "p : " + str(count['p']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "q : " + str(count['q']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "r : " + str(count['r']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "s : " + str(count['s']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "t : " + str(count['t']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "u : " + str(count['u']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "v : " + str(count['v']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "w : " + str(count['w']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "x : " + str(count['x']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "y : " + str(count['y']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "z : " + str(count['z']), (10, 350), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "0 : " + str(count['0']), (10, 360), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "1 : " + str(count['1']), (10, 370), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "2 : " + str(count['2']), (10, 380), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "3 : " + str(count['3']), (10, 390), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "4 : " + str(count['4']), (10, 400), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "5 : " + str(count['5']), (10, 410), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "6 : " + str(count['6']), (10, 420), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "7 : " + str(count['7']), (10, 430), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "8 : " + str(count['8']), (10, 440), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "9 : " + str(count['9']), (10, 450), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame, (0, 40), (300, 400), (255, 255, 255), 2)
    cv2.imshow("data", frame)
    cv2.imshow("ROI", frame[40:400, 0:300])
    roi = frame[40:400, 0:300]
    interrupt = cv2.waitKey(10)

    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory, 'A', str(count['a']) + '.png'), roi)
    elif interrupt & 0xFF == ord('b'):
        cv2.imwrite(os.path.join(directory, 'B', str(count['b']) + '.png'), roi)
    elif interrupt & 0xFF == ord('c'):
        cv2.imwrite(os.path.join(directory, 'C', str(count['c']) + '.png'), roi)
    elif interrupt & 0xFF == ord('d'):
        cv2.imwrite(os.path.join(directory, 'D', str(count['d']) + '.png'), roi)
    elif interrupt & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(directory, 'E', str(count['e']) + '.png'), roi)
    elif interrupt & 0xFF == ord('f'):
        cv2.imwrite(os.path.join(directory, 'F', str(count['f']) + '.png'), roi)
    elif interrupt & 0xFF == ord('g'):
        cv2.imwrite(os.path.join(directory, 'G', str(count['g']) + '.png'), roi)
    elif interrupt & 0xFF == ord('h'):
        cv2.imwrite(os.path.join(directory, 'H', str(count['h']) + '.png'), roi)
    elif interrupt & 0xFF == ord('i'):
        cv2.imwrite(os.path.join(directory, 'I', str(count['i']) + '.png'), roi)
    elif interrupt & 0xFF == ord('j'):
        cv2.imwrite(os.path.join(directory, 'J', str(count['j']) + '.png'), roi)
    elif interrupt & 0xFF == ord('k'):
        cv2.imwrite(os.path.join(directory, 'K', str(count['k']) + '.png'), roi)
    elif interrupt & 0xFF == ord('l'):
        cv2.imwrite(os.path.join(directory, 'L', str(count['l']) + '.png'), roi)
    elif interrupt & 0xFF == ord('m'):
        cv2.imwrite(os.path.join(directory, 'M', str(count['m']) + '.png'), roi)
    elif interrupt & 0xFF == ord('n'):
        cv2.imwrite(os.path.join(directory, 'N', str(count['n']) + '.png'), roi)
    elif interrupt & 0xFF == ord('o'):
        cv2.imwrite(os.path.join(directory, 'O', str(count['o']) + '.png'), roi)
    elif interrupt & 0xFF == ord('p'):
        cv2.imwrite(os.path.join(directory, 'P', str(count['p']) + '.png'), roi)
    elif interrupt & 0xFF == ord('q'):
        cv2.imwrite(os.path.join(directory, 'Q', str(count['q']) + '.png'), roi)
    elif interrupt & 0xFF == ord('r'):
        cv2.imwrite(os.path.join(directory, 'R', str(count['r']) + '.png'), roi)
    elif interrupt & 0xFF == ord('s'):
        cv2.imwrite(os.path.join(directory, 'S', str(count['s']) + '.png'), roi)
    elif interrupt & 0xFF == ord('t'):
        cv2.imwrite(os.path.join(directory, 'T', str(count['t']) + '.png'), roi)
    elif interrupt & 0xFF == ord('u'):
        cv2.imwrite(os.path.join(directory, 'U', str(count['u']) + '.png'), roi)
    elif interrupt & 0xFF == ord('v'):
        cv2.imwrite(os.path.join(directory, 'V', str(count['v']) + '.png'), roi)
    elif interrupt & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(directory, 'W', str(count['w']) + '.png'), roi)
    elif interrupt & 0xFF == ord('x'):
        cv2.imwrite(os.path.join(directory, 'X', str(count['x']) + '.png'), roi)
    elif interrupt & 0xFF == ord('y'):
        cv2.imwrite(os.path.join(directory, 'Y', str(count['y']) + '.png'), roi)
    elif interrupt & 0xFF == ord('z'):
        cv2.imwrite(os.path.join(directory, 'Z', str(count['z']) + '.png'), roi)
    elif interrupt & 0xFF == ord('0'):
        cv2.imwrite(os.path.join(directory, '0', str(count['0']) + '.png'), roi)
    elif interrupt & 0xFF == ord('1'):
        cv2.imwrite(os.path.join(directory, '1', str(count['1']) + '.png'), roi)
    elif interrupt & 0xFF == ord('2'):
        cv2.imwrite(os.path.join(directory, '2', str(count['2']) + '.png'), roi)
    elif interrupt & 0xFF == ord('3'):
        cv2.imwrite(os.path.join(directory, '3', str(count['3']) + '.png'), roi)
    elif interrupt & 0xFF == ord('4'):
        cv2.imwrite(os.path.join(directory, '4', str(count['4']) + '.png'), roi)
    elif interrupt & 0xFF == ord('5'):
        cv2.imwrite(os.path.join(directory, '5', str(count['5']) + '.png'), roi)
    elif interrupt & 0xFF == ord('6'):
        cv2.imwrite(os.path.join(directory, '6', str(count['6']) + '.png'), roi)
    elif interrupt & 0xFF == ord('7'):
        cv2.imwrite(os.path.join(directory, '7', str(count['7']) + '.png'), roi)
    elif interrupt & 0xFF == ord('8'):
        cv2.imwrite(os.path.join(directory, '8', str(count['8']) + '.png'), roi)
    elif interrupt & 0xFF == ord('9'):
        cv2.imwrite(os.path.join(directory, '9', str(count['9']) + '.png'), roi)
    elif interrupt & 0xFF == 27:  # ASCII for ESC key
        break

cap.release()
cv2
