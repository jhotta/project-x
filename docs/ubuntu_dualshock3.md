#Dualshock3を利用する

AR Droneのプログラミングの概要を理解するために、Sony Dualshock3を使ってAR Droneの挙動を理解するコントロールステーションを作ってみる。

## 準備環境
- Debia系Linux OS
- WiFi(AR Droneとの通信用)
- Bluetooh(Dualshock3との通信用)
- PC or Raspberry Pi

## 事前準備

Bluetoothによる通信が出来ているか確認する。Bluetooth関連のソフトがインストール出来ていな場合はapt-getコマンドを使い次のソフトをインストールする。

```
$ sudo apt-get update
$ sudo apt-get install bluetooth bluez-utils bluez-compat bluez-hcidump
$ sudo apt-get install libusb-dev libbluetooth-dev
```
次のコマンドを使って動作を確認する。

```
$ /etc/init.d/bluetooth status
[ ok ] bluetooth is running.
```

##sxipairのインストール

Dualshock3とPCをペアリングするためのツールをダウンロードし、ビルドする。

まずは、ソースをダウンドロードする。

```
$ wget "http://www.pabr.org/sixlinux/sixpair.c" -O sixpair.c
```
次のgccコマンドを使いツールをビルドする。

```
$ gcc -o sixpair sixpair.c -lusb
```

##sixadのインストール

###UbuntuPCの場合

UbuntuPC用には、debパッケージが準備されている。今回はリポジトリーを使いして、そのdebパッケージを使用する。

debパッケージは次の手順でインストールする。

```
$ sudo apt-add-repository ppa:falk-t-j/qtsixa
$ sudo apt-get update
$ sudo apt-get install sixad
```

###Raspberry Piの場合

ARM用にビルドが必要なためソースをダウンロードしてきます。

```
$ wget https://sourceforge.net/projects/qtsixa/files/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz/download -O QtSixA-src.tar.gz
```
まずは、ファイルを解凍する。

```
$ tar zxvf QtSixA-src.tar.gz
```
解凍先のディレクトリに移動して、次の手順でソースをビルドする。

```
$ cd cd QtSixA-1.5.1/sixad
$ make
$ sudo make install
```
これでソフトのインストールが完了です。

## Dualshock3とPCのペアリング

まず、ペーアリングツール(sixpair)を使って、Dualshock3接続します。

```
$ sudo ./sixpair
Current Bluetooth master: xx:xx:xx:xx:xx:xx
Setting master bd_addr to: xx:xx:xx:xx:xx:xx
```
HEX文字列が表示されればDuealshock3とPCとのペアリングは完了です。

次に、先ほどコンパイルしたsixadを使ってDualshock3と通信を開始することにします。

```
$ sudo sixad -start
sixad-bin[2533]: started
sixad-bin[2533]: sixad started, press the PS button now
```

ここで、指示に従ってPSを長押すると、 Dualshock3が振動し、その後LEDが順次点灯を始め、どれかの番号のLEDで泊まります。

```
sixad-sixaxis[2539]: started
sixad-sixaxis[2539]: Connected 'PLAYSTATION(R)3 Controller (00:06:F7:02:87:DF)' [Battery 05]
```

Daualshock3の通信の出力は、"/dev/inupt/js0"になります。1番のLEDが点灯した場合はjs０、２番のLEDが点灯した場合はjs1という命名規則になります。

内容を確認したい場合は、js0の内容をホームディレクトリにcatで書き出すことが出来ます。このファイルをバイナリーが閲覧できるエディタで開くとsixadが出力している内容をみることができます。

```
$ cat /dev/input/js0 > ~/js0.log
```

##Sixadが出力するdataの内容（使用する部分のみ）

sixadを介して受け取ることがでこるDualshock3の信号は、8byteのバイナリーコードになります。

###各種ボタン入力の仕様:

ボタン入力信号の仕様は以下の通り。

5byte:

|HEX|00|01|
|-|-|-|
|意味|押し下げ解除|押し下げ|

7byte:

|HEX|01|
|-|-|
|意味|ボタン信号フラッグ|

8byte:

|HEX|00|01|02|03|04|05|06|07|
|-|-|-|-|-|-|-|-|-|
|ボタン種類|SELECT|L3|R3|START|↑|→|↓|←|

|HEX|08|09|0A|0B|0C|0E|0D|0F|
|-|-|-|-|-|-|-|-|-|
|ボタン種類|L2|R2|L1|R1|△|○|×|□|

- L3 = 左Joystick
- R3 = 右Joystick

8byteの一覧表:

|1byte|2byte|3byte|4byte|5byte|6byte|7byte|8byte|ボタン|操作|
|-|-|-|-|-|-|-|-|-|-|
|xx|xx|xx|xx|01|xx|01|00|SELECT|押し|
|xx|xx|xx|xx|00|xx|01|00|SELECT|解除|
|xx|xx|xx|xx|01|xx|01|01|L3|押し|
|xx|xx|xx|xx|00|xx|01|01|L3|解除|
|xx|xx|xx|xx|01|xx|01|02|R3|押し|
|xx|xx|xx|xx|00|xx|01|02|R3|解除|
|xx|xx|xx|xx|01|xx|01|03|START|押し|
|xx|xx|xx|xx|00|xx|01|03|START|解除|
|xx|xx|xx|xx|01|xx|01|04|↑|押し|
|xx|xx|xx|xx|00|xx|01|04|↑|解除|
|xx|xx|xx|xx|01|xx|01|05|→|押し|
|xx|xx|xx|xx|00|xx|01|05|→|解除|
|xx|xx|xx|xx|01|xx|01|06|↓|押し|
|xx|xx|xx|xx|00|xx|01|06|↓|解除|
|xx|xx|xx|xx|01|xx|01|07|←|押し|
|xx|xx|xx|xx|00|xx|01|07|←|解除|
|xx|xx|xx|xx|01|xx|01|08|L2|押し|
|xx|xx|xx|xx|00|xx|01|08|L2|解除|
|xx|xx|xx|xx|01|xx|01|09|R2|押し|
|xx|xx|xx|xx|00|xx|01|09|R2|解除|
|xx|xx|xx|xx|01|xx|01|0A|L1|押し|
|xx|xx|xx|xx|00|xx|01|0A|L1|解除|
|xx|xx|xx|xx|01|xx|01|0B|R1|押し|
|xx|xx|xx|xx|00|xx|01|0B|R1|解除|
|xx|xx|xx|xx|01|xx|01|0C|△|押し|
|xx|xx|xx|xx|00|xx|01|0C|△|解除|
|xx|xx|xx|xx|01|xx|01|0D|○|押し|
|xx|xx|xx|xx|00|xx|01|0D|○|解除|
|xx|xx|xx|xx|01|xx|01|0E|×|押し|
|xx|xx|xx|xx|00|xx|01|0E|×|解除|
|xx|xx|xx|xx|01|xx|01|0F|□|押し|
|xx|xx|xx|xx|00|xx|01|0F|□|解除|

- 7byte目の"01"が、ボタンの押し下げ入力であるフラッグ
- 8byte目が、押し下げられたボタンの種類
- 5byte目が、"01は押し下げ”、“00は押し下げ解除”

### アナログティック入力の仕様:

アナログスティックの信号仕様は以下の通り。

6byte:

|HEX|XX| 
|-|-|-|
|意味|座標の値|

- 上下座標の値は、手前側が正方向
- 左右座標の値は、右側が正方向


7byte:

|HEX|02|
|-|-|
|意味|アナログスティック信号フラッグ|

8byte:

|HEX|00|01|02|03|04|05|06|
|-|-|-|-|-|-|-|-|
|アナログスティックの種類|左:前後|左:左右|右:前後|右:左右|軸傾き|軸傾き|軸傾き|

- 軸傾きに関しては今後の解析課題

8byteの一覧表:

|1byte|2byte|3byte|4byte|5byte|6byte|7byte|8byte|スティック:方向|
|-|-|-|-|-|-|-|-|-|
|xx|xx|xx|xx|xx|xx|02|00|左:前後|
|xx|xx|xx|xx|xx|xx|02|01|左:左右|
|xx|xx|xx|xx|xx|xx|02|02|右:前後|
|xx|xx|xx|xx|xx|xx|02|03|右:左右|

- 7byte目の"02"が、ボタンの押し下げ入力であるフラッグ
- 8byte目が、操作したアナログスティックの種類
- 6byte目が、座標値

### その他の信号

解析が出来いない信号。複数のボタンを同時に押した時などに表示される。

7byte:

|HEX|81|82|
|-|-|-|
|意味|不明|不明|
