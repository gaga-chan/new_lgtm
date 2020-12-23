# coding = UTF-8
from lgtm.drawer import save_with_message
from lgtm.image_source import get_image

import click
# 画像のソース情報とメッセージを受け取れるようにする
@click.command()
@click.option('--message', '-m', default='@AKIRA-MEMASEN(^_^;)',
                show_default=True, help='画像に乗せる文字列')
@click.argument('keyword')
def cli(keyword, message):
    """LGTM画像生成ツール"""
    lgtm(keyword, message)
    #click.echo('lgtm') # 動作確認用

def lgtm(keyword, message):
    # ここにロジックを追加していく
    with get_image(keyword) as fp:
        save_with_message(fp, message)
    #pass
