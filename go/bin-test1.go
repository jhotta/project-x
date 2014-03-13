package main
 
import (
 "bytes"
 "encoding/binary"
 "fmt"
 "os"
)
 
func main() {
 // uint8型(1バイト)の値を用意する
 val := uint8(200)
 
 // バイナリデータに変換してファイルに出力する
 // バイトオーダはBigEndianとする
 WriteBinaryFile("test", binary.BigEndian, val)
}
 
/*
バイナリデータに変換してファイルに出力する
*/
func WriteBinaryFile(filename string, order binary.ByteOrder, val interface{}){
 // バイナリデータの格納用
 buf := new(bytes.Buffer)
 // valの値をバイナリデータに変換してbufに格納する
 err := binary.Write(buf, order, val)
 
 if err != nil {
  fmt.Println("err:", err)
  return
 }
 
 // ファイル作成 
 file, err2 := os.Create(filename)
 if err2 != nil {
  fmt.Println("file create err:", err2)
  return
 }
  
 // バイナリデータをファイルに書き込み
 _, err3 := file.Write(buf.Bytes())
 if err3 != nil {
  fmt.Println("file write err:", err3)
  return
 }
  
 fmt.Println("file write ok.")
}