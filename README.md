## 청각장애인 부모를 위한 아기 울음소리 감지 및 범주 분류

[Hear-is, Hear-ease](https://github.com/Hear-is-Hear-ease/.github)의 백엔드 레포지토리.

### Hear-is Hear-ease 백엔드.

- 소속: 서울과학기술대학교 데이터청년 캠퍼스 01조

- 팀원: 권정연, 강근희, 곽재원, 고은아, 장민준, 신정아

<br>

Hear-is Hear-ease 백엔드.

청각장애 부모를 위해 아이의 울음을 감지하고 원인을 파악하는 서비스의 백엔드.

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
