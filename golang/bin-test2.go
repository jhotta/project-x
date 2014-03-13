package main
 
import (
 "bytes"
 "encoding/binary"
 "fmt"
 "os"
)
 
func main() {
 // バイナリファイルを読み込む
 // バイトオーダはBigEndian
 ReadBinaryFile("test", binary.BigEndian)
}
 
/*
バイナリファイルを読み込む
*/
func ReadBinaryFile(filename string, order binary.ByteOrder) {
 // ファイルを開く
 file, err := os.Open(filename)
 
 if err != nil {
  fmt.Println("err:", err)
  return
 }
 
 // ファイルから1バイト読み出し
 b := make([]byte, 1)
 file.Read(b)
 
 // データ格納用
 var val uint8 
 // バイナリデータからuint8型の値に変換して格納する
 err2 := binary.Read(bytes.NewBuffer(b), order, &val)
 
 if err2 != nil {
  fmt.Println("err2:", err2)
  return
 }
 
 fmt.Println("read data:", val)
}