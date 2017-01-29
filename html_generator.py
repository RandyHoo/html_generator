import codecs

#本文のパス
content_path = 'C:/Users/Ryo/Documents/プログラミング学習関連/Python3/HTMLgenerator/content/profile.html'

#テンプレート(ヘッダー、サイド、フッター)のパス
head_path = 'C:/Users/Ryo/Documents/プログラミング学習関連/Python3/HTMLgenerator/template/head.html'
side_path = 'C:/Users/Ryo/Documents/プログラミング学習関連/Python3/HTMLgenerator/template/side.html'
foot_path = 'C:/Users/Ryo/Documents/プログラミング学習関連/Python3/HTMLgenerator/template/foot.html'

#出力先のパス
output_path = 'C:/Users/Ryo/Documents/プログラミング学習関連/Python3/HTMLgenerator/output/content.html'


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
