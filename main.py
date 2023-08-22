from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

import numpy as np
import tensorflow as tf
import librosa
import os
from io import BytesIO
from skimage.transform import resize

os.environ['NUMBA_DISABLE_JIT'] = "1"

app = FastAPI()
model = tf.keras.models.load_model(
    '/Users/jaewone/developer/tensorflow/baby-cry-classification/model/resnet_v3.h5')


async def get_input_vector_from_uploadfile(byteFile) -> np.ndarray:
    y, sr = librosa.load(BytesIO(byteFile), sr=16000)
    mel_spec = librosa.feature.melspectrogram(
        y=y, sr=sr, n_mels=128, n_fft=2048, hop_length=501)
    mel_spec_dB = librosa.power_to_db(mel_spec, ref=np.max)
    RATIO = 862 / 64
    mel_spec_dB_resized = resize(mel_spec_dB, (mel_spec_dB.shape[0], mel_spec_dB.shape[1] * RATIO),
                                 anti_aliasing=True, mode='reflect')
    mel_spec_dB_stacked = np.stack([mel_spec_dB_resized] * 3, axis=-1)
    return mel_spec_dB_stacked[np.newaxis, ]


async def get_predict_class(input_vector):
    classes = ['sad', 'hug', 'diaper', 'hungry',
               'sleepy', 'awake', 'uncomfortable']
    predictions = model.predict(input_vector)[0]
    return classes[np.argmax(predictions)]
# test_vector = get_input_vector_from_file('/Users/jaewone/developer/tensorflow/baby-cry-classification/data/diaper/diaper_18.wav')


@app.get("/")
def 이름():
    return '보낼 값'


@app.post("/")
async def upload_file(file: UploadFile = None):
    if file is None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="File not provided")

    if file.filename.endswith(".wav"):
        content = await file.read()
        input_vector = await get_input_vector_from_uploadfile(content)
        state = await get_predict_class(input_vector)
        return JSONResponse(content={"filename": file.filename, state: state})
    else:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="Only .wav files are accepted")


# uvicorn main:app --reload
