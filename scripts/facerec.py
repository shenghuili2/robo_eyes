import face_recognition
import cv2


def facereco(img_path):
  7
  8     known_image = face_recognition.load_image_file("downey.jpg")
  9     unknown_image = face_recognition.load_image_file(img_path)
 10
 11     biden_encoding = face_recognition.face_encodings(known_image)[0]
 12     unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
 13
 14     results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
 15     message = 'unKnown'
 16     if results == [True]:
 17         message = 'Downey'
 18     else:
 19         known_image = face_recognition.load_image_file("andy.jpg")
 20         andy_encoding = face_recognition.face_encodings(known_image)[0]
 21         results = face_recognition.compare_faces([andy_encoding], unknown_encoding)
 22         if results == [True]:
 23             message = 'Andy'
 24
 25     unknown_image = cv2.imread(img_path)
 26     small_image = cv2.resize(unknown_image, (0, 0), fx=0.25, fy=0.25)
 27     rgb_pic = small_image[:, :, ::-1]
 28     face_location = face_recognition.face_locations(rgb_pic)[0]
 29     # face_encoding = face_recognition.face_encodings(rgb_pic, face_location)[0]
 30     (top, right, bottom, left) = face_location
 31     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
 32     top *= 4
 33     right *= 4
 34     bottom *= 4
 35     left *= 4
 36
 37     # Draw a box around the face
 38     cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 0, 255), 2)
 39
 40     # Draw a label with a name below the face
 41     cv2.rectangle(unknown_image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
 42     font = cv2.FONT_HERSHEY_DUPLEX
 43     cv2.putText(unknown_image, message, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
 44
 45     # Display the resulting image
 46     cv2.imwrite(img_path, unknown_image)
 47     # cv2.imshow('Video', unknown_image)
 48     if cv2.waitKey(1) & 0xFF == ord('q'):
 49         return message
 50     return message

if __name__ == '__main__':
    #res = facereco('upload_img.jpg')
    res = facereco('upload_img.jpg')
    print(res)
