## 청각장애인 부모를 위한 아기 울음소리 감지 및 범주 분류

>[Hear-is, Hear-ease](https://github.com/Hear-is-Hear-ease)의 백엔드 레포지토리.

본 프로젝트는 **기술을 통한 사회적 복지 실현**이라는 목표 아래, **청각장애인 부모**가 아기의 울음을 인지하고 적절한 솔루션을 제공받을 수 있도록 돕는 **아기 울음소리 감지 및 울음 원인 분류 어플리케이션**을 개발하는 것을 목적으로 합니다.

- **프로젝트명**: 아기 울음소리 감지 및 범주 분류 모델

  - App: [Hear-ease-App](https://github.com/Hear-is-Hear-ease/Hear-ease-App)
  - Backend: [Hear-ease-Backend](https://github.com/Hear-is-Hear-ease/Hear-ease-Backend)
  - AI: [Hear-ease-AI](https://github.com/Hear-is-Hear-ease/Hear-ease-AI)

- **소속**: 서울과학기술대학교 데이터청년 캠퍼스 01조
- **팀원**: [권정연](https://github.com/kyuleeee), 강근희, [곽재원](https://github.com/jaewonE), 고은아, [장민준](https://github.com/MinJunJA), [신정아](https://github.com/JeongaShin)
- [어플리케이션 이미지](https://github.com/Hear-is-Hear-ease/.github/blob/main/assets/screenshots)
- [시각 자료 PDF](https://github.com/Hear-is-Hear-ease/.github/blob/main/doc/poster.pdf)

<br>

FastAPI로 구성되어 있으며 '/' 주소로 Post 방식으로 wav 파일과 함께 요청이 들어올 시 아기울음 소리 범주에 따른 확률값을 JSON 형태로 반환한다.

아기울음 소리 원인은 'sad', 'hug', 'diaper', 'hungry', 'sleepy', 'awake', 'uncomfortable', 총 7가지로 분류한다.

아래는 반환되는 JSON 값의 예시이다.

```JSON
{
	"filename": "baby_cry_sound.wav",
	"stateMap": {
		"sad": 7.044649100862443e-05,
		"hug": 0.8008043611305765808,
		"diaper": 0.9160542917251587,
		"hungry": 0.0020948753226548433,
		"sleepy": 4.426829036674462e-06,
		"awake": 0.0001030488929245621,
		"uncomfortable": 0.0008684333879500628
	}
}
```
