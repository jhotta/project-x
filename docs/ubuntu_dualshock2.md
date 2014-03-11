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


```
$ sudo sixad -start
```


```
$ cat /dev/input/js0
```

##Sixadが出力するdataの内容（使用する部分のみ）

