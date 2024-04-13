import numpy as np
import cv2 as cv2
from pyzbar.pyzbar import decode 
import qr_interface
import sound
import tkinter as tk

# Initialize Tkinter root window
root = qr_interface.root
root.title("QR Code Scanner")

# Label to display status
label = qr_interface.label

# Previous scanned QR code
prev_scanned_code = ""

# Button to display history
def display_history():
    history_text = ""
    for item in history:
        history_text += f"Data: {item['data']}, Status: {item['status']}\n"
    qr_interface.update_label(history_text)

history_button = tk.Button(root, text="View History", command=display_history)
history_button.pack(pady=20)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

history = []

with open("myDataFile.txt") as f:
    myDataList = f.read().splitlines()

while True:
    success, img = cap.read()
    
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData != prev_scanned_code:  # Check if new QR code is different
            if myData in myDataList:
                myOutput = "Authorized"
                myColor = (0, 255,0)
                qr_interface.update_label("Authorized")
                sound.play_sound("Authorized")
            else:
                myOutput = "Un-Authorized"
                myColor = (255, 0, 0)
                qr_interface.update_label("Un-Authorized")
                sound.play_sound("Un-Authorized")

            # Append to history
            history.append({"data": myData, "status": myOutput})

            # Log to file
            with open("log.txt", "a") as log_file:
                log_file.write(f"Scanned QR Code: {myData}, Status: {myOutput}\n")

            prev_scanned_code = myData  # Update previous scanned code

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        cv2.putText(img, myOutput, (barcode.rect[0], barcode.rect[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, myColor, 2)
    
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
root.mainloop()
