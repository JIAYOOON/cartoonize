# cartoonize_video
#### OpenCV 라이브러리를 사용하여 비디오를 카툰화하는 기능을 제공합니다. 입력 비디오 파일을 가져와 각 프레임에 카툰 효과를 적용하고 새로운 비디오 파일로 저장합니다.

___
스크립트에서 cartoonize_frame 함수를 수정하여 카툰 효과를 사용자 정의할 수 있습니다. 이 함수는 비디오의 각 프레임에 카툰 효과를 적용합니다.

___
**input_video_path** : 입력 비디오 파일의 경로입니다.
___
**output_video_path** : 출력된 카툰화된 비디오 파일을 저장할 경로입니다.
__
**입력 비디오를 카툰화합니다**
cartoonize_video(input_video_path, output_video_path, cartoonize_frame)


<img width="50%" src="https://github.com/JIAYOOON/cartoonize/assets/113532368/08ea6b10-02ca-4efe-9deb-bd9ecf0344e6.gif"/>
[input_video]

<img width="50%" src="https://github.com/JIAYOOON/cartoonize/assets/113532368/d4d7f5ec-a00f-40de-bc80-90fbe1422a84.gif"/>
[cartoonized_video]
