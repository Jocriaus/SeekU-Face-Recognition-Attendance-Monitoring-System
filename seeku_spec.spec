# -*- mode: python -*-

block_cipher = None

face_models = [
('.\\face_recognition_models\\models\\dlib_face_recognition_resnet_model_v1.dat', './face_recognition_models/models'),
('.\\face_recognition_models\\models\\mmod_human_face_detector.dat', './face_recognition_models/models'),
('.\\face_recognition_models\\models\\shape_predictor_5_face_landmarks.dat', './face_recognition_models/models'),
('.\\face_recognition_models\\models\\shape_predictor_68_face_landmarks.dat', './face_recognition_models/models'),
]


onefile=True

a = Analysis(['login_app.py'],
             pathex=['C:\\Users\\JC Austria\\Documents\\GitHub\\Face-Recognition-Attendance-Monitoring-System'],
             binaries=face_models,
             datas=[('.\\mediapipe\\modules', 'mediapipe\\modules'),],
             hiddenimports=['babel.numbers'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher
             )


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SeekU',
          debug=False,
          strip=False,
          icon='.\\SeekU\\SeekU.ico',
          upx=True,
          runtime_tmpdir=None,
          console=False )