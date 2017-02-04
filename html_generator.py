import codecs
import os

#スクリプトのパスを取得
base = os.path.dirname(os.path.abspath(__file__))

#本文のパス
content_path = os.path.normpath(os.path.join(base, 'content/profile.html'))

#テンプレート(ヘッダー、サイド、フッター)のパス
head_path = os.path.normpath(os.path.join(base, 'template/head.html'))
side_path = os.path.normpath(os.path.join(base, 'template/side.html'))
foot_path = os.path.normpath(os.path.join(base, 'template/foot.html'))

#出力先のパス
output_path = os.path.normpath(os.path.join(base, 'output/content.html'))


#各種ファイルを開く
content = open( content_path, 'r' )
head = open( head_path, 'r' )
side = open( side_path, 'r' )
foot = open( foot_path, 'r' )
fout = open( output_path, 'w' )

#結合のためバッファに格納
headbuf = head.read()
sidebuf = side.read()
contentbuf = content.read()
footbuf = foot.read()

#結合
outbuf = headbuf + sidebuf + contentbuf + footbuf

#出力
fout.write(outbuf)
