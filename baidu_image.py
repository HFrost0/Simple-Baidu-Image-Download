import requests
import json
from tqdm import tqdm
import os

word = input('请输入关键词：')
cnt = int(input('请输入数量：'))
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br'
}
image_urls = []
file_path = f'imgs/{word}'
if os.path.exists(file_path) is False: os.makedirs(file_path)
print('获取链接中...', end='')
for pn in range(0, cnt, 30):
    r = requests.get(url='https://image.baidu.com/search/acjson',
                     params={'tn': 'resultjson_com', 'ipn': 'rj', 'word': word, 'pn': pn, 'rn': 30, }, headers=headers)
    js = json.loads(r.text)
    for i in js['data']:
        if len(i) > 0: image_urls.append(i['thumbURL'])
print('完成')
for idx, url in tqdm(enumerate(image_urls[:cnt]), total=cnt, desc=f'正在下载{word}图片'):
    with open(f'{file_path}/{idx}.jpg', 'wb') as f:
        f.write(requests.get(url).content)
print(f'获取完成，给你存在当前目录下的 imgs/{word} 文件夹里面了哦～')
