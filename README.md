# robosys2018 ROS課題2

[ロボットシステム学2018第11回](https://github.com/ryuichiueda/robosys2018/blob/master/11.md),[ロボットシステム学2018第13回](https://github.com/ryuichiueda/robosys2018/blob/master/13.md)を参照

主な目的はraspberry piを用いてrosの実行

```
$ roslaunch mypkg mypkg.launch
```
上記のコマンドで実行
```
$ rostopic echo /twice
```
上記のコマンドでパブリッシャとサブスクライバの動作確認

### ブラウザでの動作確認
ブラウザで`http://<Raspberry piのipアドレス>:8000`と入力
