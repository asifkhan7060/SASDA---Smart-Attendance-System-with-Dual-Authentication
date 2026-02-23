# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk  # pip install pillow
# from tkinter import messagebox
# import mysql.connector  # pip install mysql-connector-python
# import cv2  # pip install opencv-python
# import os
# import numpy as np
# from time import strftime
# from datetime import datetime
# import face_recognition  # pip install face-recognition


# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np
# from time import strftime
# from datetime import datetime
# import face_recognition
# import torch
# import torchaudio
# import sounddevice as sd
# import wave
# from scipy.spatial.distance import cosine
# from speechbrain.inference import EncoderClassifier


# class Face_Recognition:
#     is_face_recognized = False
#     is_voice_reccognized = False
#     data_for_voice_recog = {"name": "", "student_id": 0, "roll": 0, "dep": ""}

#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         self.var_std_id = StringVar()
#         self.var_std_name = StringVar()

#     # Load the Speaker Recognition Model
#         self.classifier = EncoderClassifier.from_hparams(
#             source="speechbrain/spkrec-ecapa-voxceleb",
#             savedir="tmp_model"
#         )

#         # Title
#         title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
#             "times new roman", 35, "bold"), bg="white", fg="green")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         # Image 1
#         img_1 = Image.open(r"images/good.jpg")
#         img_1 = img_1.resize((650, 830), Image.LANCZOS)
#         self.photoimg_1 = ImageTk.PhotoImage(img_1)

#         bg_img1 = Label(self.root, image=self.photoimg_1)
#         bg_img1.place(x=0, y=55, width=650, height=700)

#         # Image 2
#         img_2 = Image.open(r"images/face.jpg")
#         img_2 = img_2.resize((950, 700), Image.LANCZOS)
#         self.photoimg_2 = ImageTk.PhotoImage(img_2)

#         bg_img2 = Label(self.root, image=self.photoimg_2)
#         bg_img2.place(x=650, y=55, width=950, height=700)

#         # Button
#         # b1_1 = Button(bg_img1, text="Face Recognition", command=self.face_recog,
#         #               cursor="hand2", font=("times new roman", 18, "bold"), bg="red", fg="white")
#         # b1_1.place(x=0, y=600, width=300, height=60)

#         b1_2 = Button(bg_img2, text="Voice Recognition", command=self.voice_recog,
#                       cursor="hand2", font=("times new roman", 18, "bold"), bg="red", fg="white")
#         b1_2.place(x=0, y=300, width=300, height=60)

    
#     # ====================== Attendance =====================

#     def mark_attendance(self, student_id, roll, name, department):
#         try:
#             with open("detail_saving.csv", "r+", newline="\n") as f:
#                 myDataList = f.readlines()
#                 name_list = [line.split(",")[0] for line in myDataList]

#                 if student_id not in name_list:
#                     now = datetime.now()
#                     date = now.strftime("%d/%m/%Y")
#                     time = now.strftime("%H:%M:%S")
#                     f.writelines(
#                         f"\n{student_id},{roll},{name},{department},{time},{date},Full Verified")

#                     # Step 4: Exit system after voice verification (even if failed)
#                     self.exit_system()

#         except Exception as e:
#             messagebox.showerror(
#                 "Error", f"Error marking attendance: {e}", parent=self.root)

#     def exit_system(self):
#         """Release webcam and close OpenCV window."""
#         cv2.destroyAllWindows()
#         exit()

#     # Edited Here

#     def voice_recog(self):
#         print(self.data_for_voice_recog)
#         # messagebox.showinfo("Success", f"Now give your voice sample!",parent=self.root)
#         voice_verified = self.recognize_speaker(
#             self.data_for_voice_recog['student_id'], self.data_for_voice_recog['name'])

#         # # Step 3: **Final Attendance Confirmation**
#         if voice_verified:
#             self.mark_attendance(self.data_for_voice_recog['student_id'], self.data_for_voice_recog['roll'], self.data_for_voice_recog['name'], self.data_for_voice_recog['dep'])
#             messagebox.showinfo("Success", f"Voice recognized successfully! Full Attendance Marked for {self.data_for_voice_recog['name']}!", parent=self.root)
#             return         
#         else:
#             messagebox.showwarning(
#                 "Warning", "Voice not recognized! Attendance not fully marked.", parent=self.root)
#             return  # **Exit after unsuccessful voice verification**

#     def face_recog(self):
#         """Perform face recognition using the webcam and trigger voice recognition before closing."""
#         known_face_encodings = []
#         known_face_ids = []

#         try:
#             # Load face encodings
#             for file in os.listdir("data"):
#                 if file.endswith(".npy"):
#                     student_id = file.split(".")[1]
#                     face_encoding = np.load(os.path.join("data", file))
#                     known_face_encodings.append(face_encoding)
#                     known_face_ids.append(student_id)

#             if not known_face_encodings:
#                 messagebox.showerror(
#                     "Error", "No face encodings found in the data folder. Please add face encodings first.", parent=self.root)
#                 return

#         except Exception as e:
#             messagebox.showerror(
#                 "Error", f"Error loading face encodings: {e}", parent=self.root)
#             return

#         # Initialize webcam
#         video_cap = cv2.VideoCapture(0)

#         if not video_cap.isOpened():
#             messagebox.showerror(
#                 "Error", "Unable to access the webcam. Please check your camera.", parent=self.root)
#             return

#         confidence_threshold = 0.35  # Adjust for better accuracy

#         while True:
#             ret, frame = video_cap.read()
#             if not ret:
#                 messagebox.showerror(
#                     "Error", "Unable to capture frame from webcam.", parent=self.root)
#                 break

#             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#             rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#             face_locations = face_recognition.face_locations(rgb_small_frame)
#             face_encodings = face_recognition.face_encodings(
#                 rgb_small_frame, face_locations)

#             for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#                 face_distances = face_recognition.face_distance(
#                     known_face_encodings, face_encoding)
#                 best_match_index = np.argmin(face_distances)
#                 best_match_distance = face_distances[best_match_index]

#                 if best_match_distance <= confidence_threshold:
#                     student_id = known_face_ids[best_match_index]

#                     try:
#                         conn = mysql.connector.connect(
#                             host="localhost",
#                             username="root",
#                             password="#include<stdio.h>",
#                             database="asif_db"
#                         )
#                         my_cursor = conn.cursor()
#                         my_cursor.execute("SELECT Name, Roll, Dep FROM students WHERE Student_id=%s", (student_id,))
#                         result = my_cursor.fetchone()

#                         if result:
#                             name, roll, dep = result
#                             self.data_for_voice_recog['student_id'] = student_id
#                             self.data_for_voice_recog['name'] = name
#                             self.data_for_voice_recog['roll'] = roll
#                             self.data_for_voice_recog['dep'] = dep
#                             # self.mark_attendance(student_id, roll, name, dep)
#                             messagebox.showinfo("Success", f"Face recognized successfully! Full Attendance Marked for {name}!",parent=self.root)
#                             video_cap.release()
#                             cv2.destroyAllWindows()
#                             return  # **Exit after successful attendance**
#                     except Exception as e:
#                             messagebox.showerror("Database Error", f"Error fetching student details: {e}",parent=self.root)
#                     finally:
#                         if conn.is_connected():
#                             my_cursor.close()
#                             conn.close()
                    
                    

#                             # Step 1: **Face Recognized - Ask for Voice Sample**
#                     messagebox.showinfo("Face Recognized", f"{name} (ID: {student_id}) recognized!\nNow take a voice sample.",parent=self.root)
                    
#                     self.data_for_voice_recog['student_id'] = student_id
#                     self.data_for_voice_recog['name'] = name
#                     self.data_for_voice_recog['roll'] = roll
#                     self.data_for_voice_recog['dep'] = dep
                    
#                     print(self.data_for_voice_recog)
#                     # Step 2: **Trigger Voice Recognition**
                    
#                     # messagebox.showwarning("Warning", "Voice not recognized! Attendance not fully marked.",parent=self.root)
#                     video_cap.release()
#                     cv2.destroyAllWindows()
#                     return  # **Exit after unsuccessful voice verification**
                            

                  

#             # Display the frame until recognition is done
#             cv2.imshow("Face Recognition", frame)

#             # Exit on pressing 'q'
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         # Cleanup
#         video_cap.release()
#         cv2.destroyAllWindows()



#     def record_audio(self, filename, duration=3, fs=16000):
#         print("Recording... Please speak now!")
#         audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#         sd.wait()
        
#         wavefile = wave.open(filename, 'wb')
#         wavefile.setnchannels(1)
#         wavefile.setsampwidth(2)
#         wavefile.setframerate(fs)
#         wavefile.writeframes(audio.tobytes())
#         wavefile.close()
#         print(f"Recording saved as {filename}")

#     def extract_voiceprint(self, audio_path):
#         signal, fs = torchaudio.load(audio_path)
#         embeddings = self.classifier.encode_batch(signal)
#         return embeddings.squeeze().detach().numpy()

    
#     def recognize_speaker(self, student_id, student_name, threshold=0.35):
#         """Recognize the speaker and ensure voice matches the recognized face."""
#         test_wav = "test_audio.wav"
#         self.record_audio(test_wav)

#         test_voiceprint = self.extract_voiceprint(test_wav)

#         # Ensure only the recognized student's voiceprint is checked
#         expected_voiceprint_path = os.path.join("voiceprints", f"{student_id}_{student_name}.npy")
        
#         if not os.path.exists(expected_voiceprint_path):
#             messagebox.showwarning("Warning", f"No voice sample found for {student_name}. Please enroll first.",parent=self.root)
#             return False

#         stored_voiceprint = np.load(expected_voiceprint_path)
#         similarity = 1 - cosine(test_voiceprint, stored_voiceprint)

#         print(f"Comparing with {student_name}: Similarity = {similarity:.4f}")

#         if similarity >= threshold:
#             messagebox.showinfo("Success", f"Voice Verified for {student_name} (Similarity: {similarity:.4f})",parent=self.root)
#             return True
#         else:
#             messagebox.showwarning("Failure", "Voice not recognized! Attendance not marked.",parent=self.root)
#             return False
 
    




# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()































































































































# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np
# from time import strftime
# from datetime import datetime
# import face_recognition
# import torch
# import torchaudio
# import sounddevice as sd
# import wave
# from scipy.spatial.distance import cosine
# from speechbrain.inference import EncoderClassifier


# class Face_Recognition:
#     is_face_recognized = False
#     is_voice_reccognized = False
#     data_for_voice_recog = {"name": "", "student_id": 0, "roll": 0, "dep": ""}

#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         self.var_std_id = StringVar()
#         self.var_std_name = StringVar()

#         # Load the Speaker Recognition Model
#         self.classifier = EncoderClassifier.from_hparams(
#             source="speechbrain/spkrec-ecapa-voxceleb",
#             savedir="tmp_model"
#         )

#         # Title
#         title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
#             "times new roman", 35, "bold"), bg="white", fg="green")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         # Image 1
#         img_1 = Image.open(r"images/good.jpg")
#         img_1 = img_1.resize((1530, 830), Image.LANCZOS)
#         self.photoimg_1 = ImageTk.PhotoImage(img_1)

#         bg_img1 = Label(self.root, image=self.photoimg_1)
#         bg_img1.place(x=0, y=55, width=1530, height=700)

#         # Image 2
#         # img_2 = Image.open(r"images/face.jpg")
#         # img_2 = img_2.resize((950, 700), Image.LANCZOS)
#         # self.photoimg_2 = ImageTk.PhotoImage(img_2)

#         # bg_img2 = Label(self.root, image=self.photoimg_2)
#         # bg_img2.place(x=650, y=55, width=950, height=700)

#         # ================= Video Button (Face Recognition) =================
#         self.cap_face = cv2.VideoCapture("Videos/face.mp4")  # <-- apna video path dalna
#         self.face_video_label = Label(bg_img1, bd=2, relief="raised", cursor="hand2")
#         self.face_video_label.place(x=175, y=250, width=300, height=300)

#         # Click event
#         self.face_video_label.bind("<Button-1>", lambda e: self.face_recog())
#         self.update_face_video()

#         b1_1 = Button(bg_img1, text="Face Recognition", command=self.face_recog,
#                       cursor="hand2", font=("times new roman", 18, "bold"), bg="blue", fg="white")
#         b1_1.place(x=175, y=550, width=300, height=60)




#         # ================= Video Button (Voice Recognition) =================
#         self.cap_voice = cv2.VideoCapture("Videos/voice.mp4")  # <-- apna video path dalna
#         self.voice_video_label = Label(bg_img1, bd=2, relief="raised", cursor="hand2")
#         self.voice_video_label.place(x=700, y=250, width=300, height=300)

#         # Click event
#         self.voice_video_label.bind("<Button-1>", lambda e: self.voice_recog())
#         self.update_voice_video()
        
#         b1_2 = Button(bg_img1, text="Voice Recognition", command=self.voice_recog,
#                     cursor="hand2", font=("times new roman", 18, "bold"), bg="blue", fg="white")
#         b1_2.place(x=700, y=550, width=300, height=60)

#     # ================= Video Update Functions =================
#     def update_face_video(self):
#         ret, frame = self.cap_face.read()
#         if ret:
#             frame = cv2.resize(frame, (300, 300))
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             img = ImageTk.PhotoImage(Image.fromarray(frame))
#             self.face_video_label.config(image=img)
#             self.face_video_label.image = img
#         else:
#             self.cap_face.set(cv2.CAP_PROP_POS_FRAMES, 0)

#         self.face_video_label.after(30, self.update_face_video)

#     def update_voice_video(self):
#         ret, frame = self.cap_voice.read()
#         if ret:
#             frame = cv2.resize(frame, (300, 300))
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             img = ImageTk.PhotoImage(Image.fromarray(frame))
#             self.voice_video_label.config(image=img)
#             self.voice_video_label.image = img
#         else:
#             self.cap_voice.set(cv2.CAP_PROP_POS_FRAMES, 0)

#         self.voice_video_label.after(30, self.update_voice_video)

#     # ====================== Attendance =====================
#     def mark_attendance(self, student_id, roll, name, department):
#         try:
#             with open("detail_saving.csv", "r+", newline="\n") as f:
#                 myDataList = f.readlines()
#                 name_list = [line.split(",")[0] for line in myDataList]

#                 if student_id not in name_list:
#                     now = datetime.now()
#                     date = now.strftime("%d/%m/%Y")
#                     time = now.strftime("%H:%M:%S")
#                     f.writelines(
#                         f"\n{student_id},{roll},{name},{department},{time},{date},Full Verified")

#                     self.exit_system()

#         except Exception as e:
#             messagebox.showerror(
#                 "Error", f"Error marking attendance: {e}", parent=self.root)

#     def exit_system(self):
#         cv2.destroyAllWindows()
#         exit()

#     def voice_recog(self):
#         print(self.data_for_voice_recog)
#         voice_verified = self.recognize_speaker(
#             self.data_for_voice_recog['student_id'], self.data_for_voice_recog['name'])

#         if voice_verified:
#             self.mark_attendance(self.data_for_voice_recog['student_id'],
#                                  self.data_for_voice_recog['roll'],
#                                  self.data_for_voice_recog['name'],
#                                  self.data_for_voice_recog['dep'])
#             messagebox.showinfo("Success", f"Voice recognized successfully! Full Attendance Marked for {self.data_for_voice_recog['name']}!", parent=self.root)
#             return
#         else:
#             messagebox.showwarning(
#                 "Warning", "Voice not recognized! Attendance not fully marked.", parent=self.root)
#             return

#     def face_recog(self):
#         known_face_encodings = []
#         known_face_ids = []

#         try:
#             for file in os.listdir("data"):
#                 if file.endswith(".npy"):
#                     student_id = file.split(".")[1]
#                     face_encoding = np.load(os.path.join("data", file))
#                     known_face_encodings.append(face_encoding)
#                     known_face_ids.append(student_id)

#             if not known_face_encodings:
#                 messagebox.showerror(
#                     "Error", "No face encodings found in the data folder. Please add face encodings first.", parent=self.root)
#                 return

#         except Exception as e:
#             messagebox.showerror(
#                 "Error", f"Error loading face encodings: {e}", parent=self.root)
#             return

#         video_cap = cv2.VideoCapture(0)

#         if not video_cap.isOpened():
#             messagebox.showerror(
#                 "Error", "Unable to access the webcam. Please check your camera.", parent=self.root)
#             return

#         confidence_threshold = 0.35

#         while True:
#             ret, frame = video_cap.read()
#             if not ret:
#                 messagebox.showerror(
#                     "Error", "Unable to capture frame from webcam.", parent=self.root)
#                 break

#             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#             rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#             face_locations = face_recognition.face_locations(rgb_small_frame)
#             face_encodings = face_recognition.face_encodings(
#                 rgb_small_frame, face_locations)

#             for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#                 face_distances = face_recognition.face_distance(
#                     known_face_encodings, face_encoding)
#                 best_match_index = np.argmin(face_distances)
#                 best_match_distance = face_distances[best_match_index]

#                 if best_match_distance <= confidence_threshold:
#                     student_id = known_face_ids[best_match_index]

#                     try:
#                         conn = mysql.connector.connect(
#                             host="localhost",
#                             username="root",
#                             password="#include<stdio.h>",
#                             database="asif_db"
#                         )
#                         my_cursor = conn.cursor()
#                         my_cursor.execute(
#                             "SELECT Name, Roll, Dep FROM students WHERE Student_id=%s", (student_id,))
#                         result = my_cursor.fetchone()

#                         if result:
#                             name, roll, dep = result
#                             self.data_for_voice_recog['student_id'] = student_id
#                             self.data_for_voice_recog['name'] = name
#                             self.data_for_voice_recog['roll'] = roll
#                             self.data_for_voice_recog['dep'] = dep
#                             messagebox.showinfo("Success", f"Face recognized successfully for {name}!", parent=self.root)
#                             video_cap.release()
#                             cv2.destroyAllWindows()
#                             return
#                     except Exception as e:
#                         messagebox.showerror("Database Error", f"Error fetching student details: {e}", parent=self.root)
#                     finally:
#                         if conn.is_connected():
#                             my_cursor.close()
#                             conn.close()

#             cv2.imshow("Face Recognition", frame)

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         video_cap.release()
#         cv2.destroyAllWindows()

#     def record_audio(self, filename, duration=3, fs=16000):
#         print("Recording... Please speak now!")
#         audio = sd.rec(int(duration * fs), samplerate=fs,
#                        channels=1, dtype='int16')
#         sd.wait()

#         wavefile = wave.open(filename, 'wb')
#         wavefile.setnchannels(1)
#         wavefile.setsampwidth(2)
#         wavefile.setframerate(fs)
#         wavefile.writeframes(audio.tobytes())
#         wavefile.close()
#         print(f"Recording saved as {filename}")

#     def extract_voiceprint(self, audio_path):
#         signal, fs = torchaudio.load(audio_path)
#         embeddings = self.classifier.encode_batch(signal)
#         return embeddings.squeeze().detach().numpy()

#     def recognize_speaker(self, student_id, student_name, threshold=0.35):
#         test_wav = "test_audio.wav"
#         self.record_audio(test_wav)

#         test_voiceprint = self.extract_voiceprint(test_wav)

#         expected_voiceprint_path = os.path.join(
#             "voiceprints", f"{student_id}_{student_name}.npy")

#         if not os.path.exists(expected_voiceprint_path):
#             messagebox.showwarning("Warning", f"No voice sample found for {student_name}. Please enroll first.", parent=self.root)
#             return False

#         stored_voiceprint = np.load(expected_voiceprint_path)
#         similarity = 1 - cosine(test_voiceprint, stored_voiceprint)

#         print(f"Comparing with {student_name}: Similarity = {similarity:.4f}")

#         if similarity >= threshold:
#             messagebox.showinfo("Success", f"Voice Verified for {student_name} (Similarity: {similarity:.4f})", parent=self.root)
#             return True
#         else:
#             messagebox.showwarning("Failure", "Voice not recognized! Attendance not marked.", parent=self.root)
#             return False


# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()





































































































































































































from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from datetime import datetime
import face_recognition
import torch
import torchaudio
import sounddevice as sd
import wave
from scipy.spatial.distance import cosine
from speechbrain.inference import EncoderClassifier


class Face_Recognition:
    is_face_recognized = False
    is_voice_reccognized = False
    data_for_voice_recog = {"name": "", "student_id": 0, "roll": 0, "dep": ""}

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.var_std_id = StringVar()
        self.var_std_name = StringVar()

        # Load the Speaker Recognition Model
        self.classifier = EncoderClassifier.from_hparams(
            source="speechbrain/spkrec-ecapa-voxceleb",
            savedir="tmp_model"
        )

        # Title
        title_lbl = Label(self.root, text="MARK ATTENDANCE", font=(
            "times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ================= Background Video =================
        self.cap_bg = cv2.VideoCapture("Videos/background-2.mp4")  # <-- apna background video path
        self.bg_label = Label(self.root)
        self.bg_label.place(x=0, y=55, width=1530, height=830)
        self.update_bg_video()

        # ================= Video Button (Face Recognition) =================
        self.cap_face = cv2.VideoCapture("Videos/face.mp4")  # <-- apna video path
        self.face_video_label = Label(self.root, bd=1, relief="raised", cursor="hand2")
        self.face_video_label.place(x=250, y=175, width=450, height=450)

        # Click event
        self.face_video_label.bind("<Button-1>", lambda e: self.face_recog())
        self.update_face_video()

        b1_1 = Button(self.root, text="Face Recognition", command=self.face_recog,
                      cursor="hand2", font=("times new roman", 18, "bold"),
                      bg="blue", fg="white")
        b1_1.place(x=250, y=625, width=450, height=60)

        # ================= Video Button (Voice Recognition) =================
        self.cap_voice = cv2.VideoCapture("Videos/voice.mp4")  # <-- apna video path
        self.voice_video_label = Label(self.root, bd=1, relief="raised", cursor="hand2")
        self.voice_video_label.place(x=850, y=175, width=450, height=450)

        # Click event
        self.voice_video_label.bind("<Button-1>", lambda e: self.voice_recog())
        self.update_voice_video()

        b1_2 = Button(self.root, text="Voice Recognition", command=self.voice_recog,
                      cursor="hand2", font=("times new roman", 18, "bold"),
                      bg="blue", fg="white")
        b1_2.place(x=850, y=625, width=450, height=60)

    # ================= Background Video Update =================
    def update_bg_video(self):
        ret, frame = self.cap_bg.read()
        if ret:
            frame = cv2.resize(frame, (1530, 830))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.bg_label.config(image=img)
            self.bg_label.image = img
        else:
            self.cap_bg.set(cv2.CAP_PROP_POS_FRAMES, 0)

        self.bg_label.after(30, self.update_bg_video)

    # ================= Face Video Update =================
    def update_face_video(self):
        ret, frame = self.cap_face.read()
        if ret:
            frame = cv2.resize(frame, (450, 450))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.face_video_label.config(image=img)
            self.face_video_label.image = img
        else:
            self.cap_face.set(cv2.CAP_PROP_POS_FRAMES, 0)

        self.face_video_label.after(30, self.update_face_video)

    # ================= Voice Video Update =================
    def update_voice_video(self):
        ret, frame = self.cap_voice.read()
        if ret:
            frame = cv2.resize(frame, (450, 450))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.voice_video_label.config(image=img)
            self.voice_video_label.image = img
        else:
            self.cap_voice.set(cv2.CAP_PROP_POS_FRAMES, 0)

        self.voice_video_label.after(30, self.update_voice_video)

    # ====================== Attendance =====================
    def mark_attendance(self, student_id, roll, name, department):
        try:
            with open("detail_saving.csv", "r+", newline="\n") as f:
                myDataList = f.readlines()
                name_list = [line.split(",")[0] for line in myDataList]

                if student_id not in name_list:
                    now = datetime.now()
                    date = now.strftime("%d/%m/%Y")
                    time = now.strftime("%H:%M:%S")
                    f.writelines(
                        f"\n{student_id},{roll},{name},{department},{time},{date},Full Verified")

                    self.exit_system()

        except Exception as e:
            messagebox.showerror(
                "Error", f"Error marking attendance: {e}", parent=self.root)

    def exit_system(self):
        cv2.destroyAllWindows()
        exit()

    def voice_recog(self):
        print(self.data_for_voice_recog)
        voice_verified = self.recognize_speaker(
            self.data_for_voice_recog['student_id'], self.data_for_voice_recog['name'])

        if voice_verified:
            self.mark_attendance(self.data_for_voice_recog['student_id'],
                                 self.data_for_voice_recog['roll'],
                                 self.data_for_voice_recog['name'],
                                 self.data_for_voice_recog['dep'])
            messagebox.showinfo("Success",
                                f"Voice recognized successfully! Full Attendance Marked for {self.data_for_voice_recog['name']}!",
                                parent=self.root)
            return
        else:
            messagebox.showwarning(
                "Warning", "Voice not recognized! Attendance not fully marked.", parent=self.root)
            return

    def face_recog(self):
        known_face_encodings = []
        known_face_ids = []

        try:
            for file in os.listdir("data"):
                if file.endswith(".npy"):
                    student_id = file.split(".")[1]
                    face_encoding = np.load(os.path.join("data", file))
                    known_face_encodings.append(face_encoding)
                    known_face_ids.append(student_id)

            if not known_face_encodings:
                messagebox.showerror(
                    "Error", "No face encodings found in the data folder. Please add face encodings first.", parent=self.root)
                return

        except Exception as e:
            messagebox.showerror(
                "Error", f"Error loading face encodings: {e}", parent=self.root)
            return

        video_cap = cv2.VideoCapture(0)

        if not video_cap.isOpened():
            messagebox.showerror(
                "Error", "Unable to access the webcam. Please check your camera.", parent=self.root)
            return

        confidence_threshold = 0.35

        while True:
            ret, frame = video_cap.read()
            if not ret:
                messagebox.showerror(
                    "Error", "Unable to capture frame from webcam.", parent=self.root)
                break

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                best_match_distance = face_distances[best_match_index]

                if best_match_distance <= confidence_threshold:
                    student_id = known_face_ids[best_match_index]

                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            password="#include<stdio.h>",
                            database="asif_db"
                        )
                        my_cursor = conn.cursor()
                        my_cursor.execute(
                            "SELECT Name, Roll, Dep FROM students WHERE Student_id=%s", (student_id,))
                        result = my_cursor.fetchone()

                        if result:
                            name, roll, dep = result
                            self.data_for_voice_recog['student_id'] = student_id
                            self.data_for_voice_recog['name'] = name
                            self.data_for_voice_recog['roll'] = roll
                            self.data_for_voice_recog['dep'] = dep
                            messagebox.showinfo("Success", f"Face recognized successfully for {name}!", parent=self.root)
                            video_cap.release()
                            cv2.destroyAllWindows()
                            return
                    except Exception as e:
                        messagebox.showerror("Database Error", f"Error fetching student details: {e}", parent=self.root)
                    finally:
                        if conn.is_connected():
                            my_cursor.close()
                            conn.close()

            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def record_audio(self, filename, duration=3, fs=16000):
        print("Recording... Please speak now!")
        audio = sd.rec(int(duration * fs), samplerate=fs,
                       channels=1, dtype='int16')
        sd.wait()

        wavefile = wave.open(filename, 'wb')
        wavefile.setnchannels(1)
        wavefile.setsampwidth(2)
        wavefile.setframerate(fs)
        wavefile.writeframes(audio.tobytes())
        wavefile.close()
        print(f"Recording saved as {filename}")

    def extract_voiceprint(self, audio_path):
        signal, fs = torchaudio.load(audio_path)
        embeddings = self.classifier.encode_batch(signal)
        return embeddings.squeeze().detach().numpy()

    def recognize_speaker(self, student_id, student_name, threshold=0.35):
        test_wav = "test_audio.wav"
        self.record_audio(test_wav)

        test_voiceprint = self.extract_voiceprint(test_wav)

        expected_voiceprint_path = os.path.join(
            "voiceprints", f"{student_id}_{student_name}.npy")

        if not os.path.exists(expected_voiceprint_path):
            messagebox.showwarning("Warning", f"No voice sample found for {student_name}. Please enroll first.", parent=self.root)
            return False

        stored_voiceprint = np.load(expected_voiceprint_path)
        similarity = 1 - cosine(test_voiceprint, stored_voiceprint)

        print(f"Comparing with {student_name}: Similarity = {similarity:.4f}")

        if similarity >= threshold:
            messagebox.showinfo("Success", f"Voice Verified for {student_name} (Similarity: {similarity:.4f})", parent=self.root)
            return True
        else:
            messagebox.showwarning("Failure", "Voice not recognized! Attendance not marked.", parent=self.root)
            return False


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
