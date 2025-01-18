import cv2
import face_recognition
import os
import numpy as np

# Paths
dataset_path = './data/CV_Dataset'
class_photos_path = './data'
output_file = './attendance.csv'

# Load student data
def load_student_encodings(dataset_path):
    encodings = {}
    for student_name in os.listdir(dataset_path):
        student_folder = os.path.join(dataset_path, student_name)
        if os.path.isdir(student_folder):
            student_images = os.listdir(student_folder)
            student_encodings = []
            for image_file in student_images:
                image_path = os.path.join(student_folder, image_file)
                image = face_recognition.load_image_file(image_path)
                try:
                    encoding = face_recognition.face_encodings(image)[0]
                    student_encodings.append(encoding)
                except IndexError:
                    print(f"Face not detected in {image_path}")
            if student_encodings:
                encodings[student_name] = np.mean(student_encodings, axis=0)
    return encodings

# Match faces and mark attendance
def mark_attendance(student_encodings, class_photo_path, output_file):
    class_photo = face_recognition.load_image_file(class_photo_path)
    face_locations = face_recognition.face_locations(class_photo)
    face_encodings = face_recognition.face_encodings(class_photo, face_locations)

    attendance = {student: "Absent" for student in student_encodings.keys()}
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(list(student_encodings.values()), face_encoding)
        face_distances = face_recognition.face_distance(list(student_encodings.values()), face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            matched_student = list(student_encodings.keys())[best_match_index]
            attendance[matched_student] = "Present"

    # Save attendance to file
    with open(output_file, 'w') as f:
        f.write("Student,Attendance\n")
        for student, status in attendance.items():
            f.write(f"{student},{status}\n")
    print(f"Attendance saved to {output_file}")

if __name__ == "__main__":
    print("Loading student encodings...")
    student_encodings = load_student_encodings(dataset_path)
    print("Processing class photo...")
    mark_attendance(student_encodings, os.path.join(class_photos_path, 'class_photo.jpg'), output_file)
    print("Attendance marking complete.")