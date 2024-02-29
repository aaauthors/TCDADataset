# Teachers’ Classroom Dress Assessment Dataset (TCDADataset)

## About the dataset：

The TCDA dataset contains how teachers dress in their daily classrooms，with a total of 11,879 image samples, covering different subjects, classrooms and diverse teaching environments. The details are shown in Figure 1.

As shown in Figure 1(a), we have defined a series of clothing attributes to capture the characteristics of teacher clothing more comprehensively. Positive attribute represents the clothing attribute that the teacher recommends in the daily classroom. Negative attribute represents the
clothing attribute that the teacher does not recommend in the daily classroom. Other attribute
represents the sample that does not participate in the teacher's dress assessment, and the absent
attribute represents the attribute that the character is missing. Finally, we conduct a comprehensive
evaluation of the teacher's attire based on the positive attributes and negative attributes to form the
final score. 

In order to enhance the robustness of the dataset, we try to simulate the shooting angles in the
collected classroom teaching videos, i.e., directly behind the classroom, 45° behind the left of the
classroom, and 45° behind the right of the classroom, as shown in Figure 1(b). Considering the
limitations of the scene, the teacher's body is often partially obscured by the lectern or the
teacher's interaction with the students, etc. Therefore, as shown in Figure 1(c), we select the
teacher's viewpoint information from four directions, i.e., forward (F), backward (B), left (L), and
right (R).
