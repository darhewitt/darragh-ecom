{"filter":false,"title":"custom_storages.py","tooltip":"/custom_storages.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":43},"end":{"row":9,"column":43},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":135,"mode":"ace/mode/python"}},"hash":"4042e73c1d7f39d5d7b2e1d61534afd2becfa4a6","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":43},"action":"insert","lines":["rom django.conf import settings","from storages.backends.s3boto3 import S3Boto3Storage","","","class StaticStorage(S3Boto3Storage):","    location = settings.STATICFILES_LOCATION","","","class MediaStorage(S3Boto3Storage):","    location = settings.MEDIAFILES_LOCATION"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":2}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":43},"action":"remove","lines":["class MediaStorage(S3Boto3Storage):","    location = settings.MEDIAFILES_LOCATION"],"id":3}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":43},"action":"insert","lines":["class MediaStorage(S3Boto3Storage):","    location = settings.MEDIAFILES_LOCATION"],"id":4}]]},"timestamp":1579266297128}