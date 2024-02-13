import VITSClient
import tempfile

def write_temp_file(data, suffix, mode="w+b"):
    """
    写入临时文件

    :param data: 数据
    :param suffix: 后缀名
    :param mode: 写入模式，默认为 w+b
    :returns: 文件保存后的路径
    """
    with tempfile.NamedTemporaryFile(mode=mode, suffix=suffix, delete=False) as f:
        f.write(data)
        tmpfile = f.name
    return tmpfile

server_url = "http://192.168.2.13:23456"
api_key = "api_key"
speaker_id = 0
length = 1.2
noise = 0.667
noisew = 0.8
max = 50
timeout = 60

result = VITSClient.tts("测试", server_url, api_key, speaker_id, length, noise, noisew, max, timeout)
tmpfile = write_temp_file(result, ".wav")
print(tmpfile)