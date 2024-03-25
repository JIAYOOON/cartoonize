# cartoonize_video
#### OpenCV 라이브러리를 사용하여 비디오를 카툰화하는 기능을 제공합니다. 입력 비디오 파일을 가져와 각 프레임에 카툰 효과를 적용하고 새로운 비디오 파일로 저장합니다.

___
스크립트에서 cartoonize_frame 함수를 수정하여 카툰 효과를 사용자 정의할 수 있습니다. 이 함수는 비디오의 각 프레임에 카툰 효과를 적용합니다.

Example:
- **input_video_path** : 입력 비디오 파일의 경로입니다.

- **output_video_path** : 출력된 카툰화된 비디오 파일을 저장할 경로입니다.

- **입력 비디오를 카툰화합니다** :
cartoonize_video(input_video_path, output_video_path, cartoonize_frame)

- **[input_video]** :
<img width="50%" src="https://github.com/JIAYOOON/cartoonize/assets/113532368/08ea6b10-02ca-4efe-9deb-bd9ecf0344e6.gif"/>

- **[cartoonized_video]** :
<img width="50%" src="https://github.com/JIAYOOON/cartoonize/assets/113532368/d4d7f5ec-a00f-40de-bc80-90fbe1422a84.gif"/>

___
- 만화 느낌이 잘 표현되지 않는 경우 : 인간의 얼굴이 가깝거나, 조명이 없어 빛과 그림자의 대비가 부족할 경우, 만화 스타일로 변환해도 원하는 만화 같은 느낌을 얻기 어려울 수 있습니다.
<img width="50%" src="https://github.com/JIAYOOON/cartoonize/assets/113532368/840a8a3e-82ff-4354-afe0-59cf1a41a122.gif"/>

___

알고리즘의 한계 :
- 알고리즘은 주어진 영상을 만화 스타일로 변환하려고 노력하지만, 실제로는 원본 만화 그림을 완벽하게 재현하는 것이 어렵습니다. 따라서 완벽한 만화 스타일 재현을 기대하기는 어렵습니다.
- 다양한 스타일에 대응할 수 있는 범용적인 알고리즘이 필요합니다.
- 만화 스타일은 주로 간결하고 단순한 텍스처를 가지고 있으나, 원본 영상에는 세부적인 텍스처가 많을 수 있습니다. 알고리즘은 이러한 세부적인 텍스처를 보존하는 데 어려움을 겪을 수 있습니다.
- 일부 알고리즘은 만화 스타일 변환 과정에서 이미지의 품질을 저하시킬 수 있습니다.
