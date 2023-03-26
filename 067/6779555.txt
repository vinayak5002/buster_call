package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
    "strconv"
)

const BUFSIZE = 10000000
var rdr *bufio.Reader
func readline() string { buf := make([]byte, 0, 16); for { l, p, e := rdr.ReadLine(); if e != nil { fmt.Println(e.Error()); panic(e) }; buf = append(buf, l...); if !p { break } }; return string(buf) }
func readIntSlice() []int { slice := make([]int, 0); lines := strings.Split(readline(), " "); for _, v := range lines { slice = append(slice, s2i(v)) }; return slice; }
func s2i(s string) int { v, ok := strconv.Atoi(s); if ok != nil { panic("Faild : " + s + " can't convert to int") }; return v }
func readint() int { return s2i(readline()) }

func main() {
    rdr = bufio.NewReaderSize(os.Stdin, BUFSIZE)
    n := readint()
    a := readIntSlice()
    q := readint()
    m := readIntSlice()
    flag := make([]bool, 20001)
    for i := 0; i < 2001; i++ {
        flag[i] = false
    }

    for bit := 0; bit < (1 << uint(n)); bit++ {
        sum := 0
        for j := 0; j < n; j++ {
            if ((bit >> uint(j)) & 1 ) == 1 {
                sum += a[j]
            }
        }
        if 0 <= sum && sum <= 2000 {
            flag[sum] = true
        }
    }

    for i := 0; i < q; i++ {
        if flag[m[i]] {
            fmt.Println("yes")
        } else {
            fmt.Println("no")
        }
    }
}
