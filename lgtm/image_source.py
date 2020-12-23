import requests
import ByteIO

class LocalImage:
    """ファイルから画像を取得する"""

    def __init__(self, path):
        self._path = path

    # メソッドget_image()を呼び出すと、画像のファイルオブジェクト
    # を返す
    def get_image(self):
        return open(self._path, 'rb')

class RemoteImage:
    """URLから画像を取得する"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        print(f'{type(data)=}')
        print(f'{type(ByteIO(data.context))=}')
        # バイトデータをファイルオブジェクトに変換
        return BytesIO(data.context)