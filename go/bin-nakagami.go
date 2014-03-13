package main
 
import (
    "fmt"
    "bytes"
    "encoding/binary"
)
 
func int32_to_bytes(i32 int32) *bytes.Buffer {
    bs := []byte {
        byte(i32 & 0xFF),
        byte(i32 >> 8 & 0xFF),
        byte(i32 >> 16 & 0xFF),
        byte(i32 >> 24 & 0xFF),
    }
    return bytes.NewBuffer(bs)
}
 
func main() {
    fmt.Println("---string to byte[] ---")
    s := "abc 漢字"
    buffer := bytes.NewBufferString(s)
    b := buffer.Bytes()
    fmt.Println("string", s)
    fmt.Println("Buffer", buffer)
    fmt.Println("byte[]", b)
 
    fmt.Println("---byte[] to string ---")
    b[0] = b[0] - 0x20
    b[1] = b[1] - 0x20
    b[2] = b[2] - 0x20
    fmt.Println("byte[]", b)
    buffer = bytes.NewBuffer(b)
    fmt.Println("Buffer", buffer)
    s = buffer.String()
    fmt.Println("string", s)
 
    fmt.Println("--- byte[] to little endian int32 ---")
    var i32 int32
    b1 := []byte{0xFE, 0xFF, 0xFF, 0xFF}    // -2
    b2 := []byte{0xFF, 0x00, 0x00, 0x00}    // 255
    buffer = bytes.NewBuffer(b1)
    binary.Read(buffer, binary.LittleEndian, &i32)
    fmt.Println(b1, i32)
    buffer = bytes.NewBuffer(b2)
    binary.Read(buffer, binary.LittleEndian, &i32)
    fmt.Println(b2, i32)
 
    fmt.Println("--- little endian int32 to bytes---")
    fmt.Println(-3, int32_to_bytes(-3).Bytes())
    fmt.Println(254, int32_to_bytes(254).Bytes())
 
    fmt.Println("--- concat bytes---")
    b3 := []byte{1,2,3}
    b4 := []byte{4,5,6}
    fmt.Println(bytes.Join([][]byte{b3, b4}, nil))
}