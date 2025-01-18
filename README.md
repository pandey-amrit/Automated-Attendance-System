# Automated Attendance System

This project implements an automated attendance system using Python and OpenCV. It leverages facial recognition to identify students in a class photo and mark their attendance. The system processes stored student images, compares them with the class photo, and generates an attendance report in a CSV file.

## Features
- **Face Detection and Recognition**: Uses the `face_recognition` library for accurate face matching.
- **Automated Attendance Marking**: Matches detected faces with student data and records attendance.
- **CSV Export**: Generates a CSV file containing the attendance record for easy integration with other systems.

## Project Structure
```
.
├── main.py               # Main script for the attendance system
├── data/
│   ├── CV_Dataset/       # Directory containing student folders with their images
│   └── class_photo.jpg   # The class photo for attendance marking
├── attendance.csv        # Output attendance file
```

## Requirements
- Python 3.8 or higher
- Required Python libraries:
  - `opencv-python`
  - `face-recognition`
  - `numpy`

Install the required libraries using:
```bash
pip install opencv-python face-recognition numpy
```

## Usage
1. **Prepare Dataset**:
   - Create a directory named `data/CV_Dataset`.
   - Add a subdirectory for each student, named after the student (e.g., `John_Doe`).
   - Place one or more images of the student in their respective subdirectory.

2. **Add Class Photo**:
   - Save the class photo as `class_photo.jpg` in the `data` directory.

3. **Run the Script**:
   ```bash
   python main.py
   ```

4. **Output**:
   - The attendance record will be saved in `attendance.csv`.

## How It Works
1. **Load Student Encodings**:
   - The script processes all images in `CV_Dataset` to extract facial encodings for each student.
   - Each student’s encodings are averaged for robust recognition.

2. **Match Faces**:
   - The class photo is analyzed to locate and encode faces.
   - Detected faces are matched against the student database using facial encodings.

3. **Mark Attendance**:
   - Matches are used to update the attendance record (Present/Absent).
   - The result is written to a CSV file.

## Example Output
A sample `attendance.csv`:
```
Student,Attendance
John_Doe,Present
Jane_Smith,Absent
Alice_Williams,Present
```

## Limitations
- Faces in the class photo must be clear and unobstructed.
- Works best with high-quality images and consistent lighting conditions.

## Future Improvements
- Add real-time attendance marking via webcam.
- Support for larger datasets with optimized performance.
- Integration with student management systems.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments
- [Face Recognition Library](https://github.com/ageitgey/face_recognition)
- [OpenCV](https://opencv.org/)
