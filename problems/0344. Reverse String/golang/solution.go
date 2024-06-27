package main

func main() {
	revString := []byte("hellothere")
	reverseString(revString)
	println(string(revString))

	revString = []byte("hello")
	reverseString(revString)
	println(string(revString))
}

func reverseString(s []byte) {
	for i := 0; i <= (len(s)-1)/2; i++ {
		tmp := s[i]
		s[i] = s[len(s)-1-i]
		s[len(s)-1-i] = tmp
	}
}
